import random
from collections import defaultdict
from spendata.models import ELFRequestData, MobileAppLocationData

RESOLUTION = 10**4 # ~10m

def get_home_circles():
    
    data = MobileAppLocationData.objects.all().values('user_latitude', 'user_longitude')
    
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
            
            # if count > 1:
                # print latitude, longitude, count
        
            if count > highest_count:
                home_circle = latitude, longitude
                highest_count = count
    
    print home_circle, highest_count
    
    return home_circle
    

def generate_random_data(centre_point=None, num_random_locations=10000, sigma=0.001):
    
    MobileAppLocationData.objects.all().delete()
    
    if centre_point is None:
        centre_point = 47.37, -122.20
        
    objects = []

    for i in range(num_random_locations):
        x = random.normalvariate(centre_point[0], sigma)
        y = random.normalvariate(centre_point[1], sigma)
        
        objects.append(MobileAppLocationData (
            user_latitude = x,
            user_longitude = y
        ))
        
    MobileAppLocationData.objects.bulk_create(objects)