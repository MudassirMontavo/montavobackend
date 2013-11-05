import logging
import gzip
import csv
from cStringIO import StringIO

from spendata.models import ELFRequestData, ELFImpressionData, ELFClickData, ELFConversionData
from spendata.openx import OpenXDataRetriever

logger = logging.getLogger(__name__)


class ELFLogDialect(csv.Dialect):
    delimiter = '\t'
    quotechar = '"'
    doublequote = False
    skipinitialspace = False
    lineterminator = '\n'
    quoting = 0

# Which model to store each type of data in
ELFDATATYPE = {
    'request':    ELFRequestData,
    'click':      ELFClickData,
    'impression': ELFImpressionData,
    'conversion': ELFConversionData,
}

# Serial to start with if nothing in DB
ELF_FIRST_SERIAL = {
    'request': 152100,
    'click': 111100,
    'impression': 137400,
    'conversion': 118250,
}


class ELFDataRetriever(OpenXDataRetriever):

    EVENT_URL = '/a/eventfeed?type={type}&range={serial}&format=json&pretty=true'

    def get_elf_data(self, datatype='request'):

        for datatype in ['request', 'click', 'impression', 'conversion']:

            serial = get_latest_serial(datatype)

            try:
                logger.info(
                    'Requesting eventfeed for type: {}, serial: {}'.format(datatype, serial))
                url = self.EVENT_URL.format(type=datatype, serial=serial)
                logger.debug('Requesting URL {!r}'.format(url))
                dataset = self.ox.get(url).get('dataset', [])

                if dataset:
                    logger.info('Eventfeed length: {}, ranges from serials {} to {}'.format(
                        len(dataset),
                        dataset[-1].get('serial'),
                        dataset[0].get('serial')
                    ))
                else:
                    logger.warning('Eventfeed is empty')

            except Exception as e:
                logger.error(
                    'Eventfeed for type {} throws an error'.format(datatype))
                logger.exception(e)
                continue

            # Reverse order - oldest to newest
            for row in dataset[::-1]:
                logger.debug('Processing serial {}'.format(row.get('serial')))

                # Only unzip non-zero records
                if int(row['@recordCount']) == 0:
                    continue

                # TODO handle multiple parts? Why is this a dict?
                if not isinstance(row['parts'], dict):
                    raise NotImplementedError('Parts is not a dict')

                filename = parse_filename(row['parts']['part']['@locator'])

                data = self.get_gzipped_data(filename)
                self.save_elf_data(data, row, datatype)

    def get_gzipped_data(self, url):
        data = self.ox.request(self.ox._resolve_url(url), method='GET')
        buf = StringIO(data.read())
        f = gzip.GzipFile(fileobj=buf)
        reader = csv.DictReader(f, dialect=ELFLogDialect)
        return list(reader)

    def save_elf_data(self, data, row, datatype):

        if int(row['@revision']) > 1:
            raise NotImplementedError('Revision incremented')

        for d in data:
            try:
                # #event_time -> event_time
                d['event_time'] = d.pop('#event_time')
                d['revision'] = row['@revision']
                d['serial_number'] = row['serial']
                d['part_id'] = row['parts']['part']['@id']

                # Remove empty items
                d = {k: v for k, v in d.iteritems() if v is not None and v != ''}

                # Get model for this datatype
                model = ELFDATATYPE[datatype]
                obj = model.objects.create(**d)

                logger.info('ELF data id {} saved'.format(obj.id))

            except KeyError as e:
                logger.exception(e)
                logger.info(d)


def parse_filename(filename):
    """ E.g. 'http://montavo-ui3.openxenterprise.com/ox/3.0/a/eventfeed/fetch?file=/blah.txt.gz' to -> /a/eventfeed/... """
    # TODO check
    pos = filename.find('/ox/3.0/a/')  # should be ~38
    return filename[pos + 7:]


def get_latest_serial(datatype):
    model = ELFDATATYPE[datatype]

    try:
        serial = model.objects.latest('pk').serial_number
    except model.DoesNotExist:
        serial = ELF_FIRST_SERIAL.get(datatype, 0)
        logger.warning(
            'No serial for {}, starting at {}'.format(datatype, serial))

    return serial
