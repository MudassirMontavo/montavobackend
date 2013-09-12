import random
from collections import defaultdict
from spendata.models import MobileAppLocationData, MobileAppUserData, MobileAppMobileData, MobileAppUserHomeCircle

RESOLUTION = 10**4 # ~10m

def save_home_circle(user_id):
    
    home_circle, weighting = get_home_circle(user_id)
    
    user_data = MobileAppUserData.objects.get(user_id=user_id)
    
    home_circle, created = MobileAppUserHomeCircle.objects.get_or_create(
        user_data = user_data,
        defaults = {
            'latitude':  home_circle[0],
            'longitude': home_circle[1],
            'weighting': weighting
        }
    )

def get_home_circle(user_id='test'):
    
    data = MobileAppLocationData.objects.filter(device_data__user_id=user_id).values('user_latitude', 'user_longitude')
    
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
        
            if count > highest_count:
                home_circle = latitude, longitude
                highest_count = count
    
    # print home_circle, highest_count, len(data)
    
    if not data:
        return (None, None), None
    
    return home_circle, float(highest_count)/len(data)

def generate_random_data(centre_point=None, num_random_locations=1000, sigma=0.0001):
    
    MobileAppLocationData.objects.filter(device_data__user_id='test').delete()
    
    if centre_point is None:
        centre_point = 47.37, -122.20 # Seattle
        
    objects = []
    
    testuser, created = MobileAppUserData.objects.get_or_create(user_id='test')
    testuserdevice, created = MobileAppMobileData.objects.get_or_create(user_id='test', defaults = {'user_data': testuser})

    for i in range(num_random_locations):
        x = random.normalvariate(centre_point[0], sigma)
        y = random.normalvariate(centre_point[1], sigma)
        
        objects.append(MobileAppLocationData (
            user_latitude = x,
            user_longitude = y,
            device_data = testuserdevice
        ))
        
    MobileAppLocationData.objects.bulk_create(objects)