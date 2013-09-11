from collections import defaultdict
from spendata.models import ELFRequestData

RESOLUTION = 10**5

def get_home_circles():
    
    data = ELFRequestData.objects.all().values('user_latitude', 'user_longitude')
    
    histogram = defaultdict(lambda: defaultdict(int))
    
    for row in data:
        
        if row['user_latitude'] is None:
            continue
        
        x = int(row['user_latitude'] * RESOLUTION)
        y = int(row['user_longitude'] * RESOLUTION)
        
        histogram[x][y] += 1
    
    highest_count = 0
    home_circle = 0, 0
    
    for x,v in histogram.iteritems():
        for y,count in v.iteritems():
            
            latitude = float(x)/RESOLUTION
            longitude = float(y)/RESOLUTION
            print latitude, longitude, count
        
            if count > highest_count:
                home_circle = latitude, longitude
                highest_count = count
    
    return home_circle
    

def generate_random_data():
    pass