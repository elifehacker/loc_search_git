from datetime import datetime
from area_cordgen import getdata, saveids
import os 

if __name__ == '__main__':
    now = datetime.now()
    current_time = now.strftime("%d%m%Y%H%M%S")

    #slat = -37.8075933
    #slong = 144.9667701
    #elat = -37.8378826
    #elong = 144.9823664
    slat = -33.724413
    slong = 151.2049313
    elat = -33.756292
    elong = 151.2411793
    dist = 0.004
    h = slat
    v = slong
    radius = 250
    count = 0
    cords = list()
    while h > elat:
        while v < elong:
            print(h, v)
            cords.append((h,v))
            v = v + dist
            count+=1
        v = slong
        h = h - dist

    now = datetime.now()
    current_time = now.strftime("%Y%m%d%H%M%S")
    print(current_time)
    print(count)
    input("Press Enter to continue...") 

    APIKEY = "xxxx" # four season key
    
    type = 'shops'
    os.mkdir(current_time) 
    saveids(cords,current_time, radius, APIKEY)

#mp_handler(ids)
