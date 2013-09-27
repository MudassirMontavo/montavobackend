from django.dispatch import Signal

import logging

logger = logging.getLogger(__name__)

def post_save_add_user_id(sender, instance, created, raw, **kwargs):
    if created and not raw:
        try:
            instance.user_id = instance.mobile_device.mobile_user.user_id
            instance.save()
        except AttributeError as e:
            logger.warning("Could not find user from custom field: %s" % instance.custom_fields)
