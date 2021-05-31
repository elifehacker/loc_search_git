import requests 
import re
import multiprocessing
from itertools import repeat
import os
import json
from multiprocessing import Pool, Process, Lock
from datetime import datetime
def get_email(website, current_time):
    global contact
    website = website.rstrip('\n')
    if website[-1]!='/':
        website+='/'
    ems = set()
    for cont in contact:
        try:
            print(website+cont)
            r = requests.get(url = website+cont, timeout=3)
            #print(r.text)
            new_emails = set(re.findall(r"[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*", r.text, re.I))
            new_emails = {p for p in new_emails if 'webp' not in str(p)}
            new_emails = {p for p in new_emails if '@2x' not in str(p)}
            ems = ems|new_emails
        except:
            pass
    with open(current_time+'/emails.txt', 'a') as f:
        print(ems)
        for e in ems:
            f.write(e+';\n')

def get_emails(file):
    now = datetime.now()
    current_time = now.strftime("%d%m%Y%H%M%S")
    os.mkdir(current_time)
    print(current_time)
    with open(file, 'r') as f:
        with Pool(processes=4)as pool:
            pool.starmap(get_email, zip(f, repeat(current_time)))
        

            
def get_web(place_id, current_time):
    PARAMS_details = {'place_id':place_id, 'fields':'name,rating,formatted_phone_number,website', 'key':APIKEY}
    rd = requests.get(url = URL_details, params = PARAMS_details) 
    dd = rd.json() 
    #print(place_id, URL_details)
    #print(dd)
    if 'website' not in dd['result']:
        return
    website = dd['result']['website']
    print(website)
    os.mkdir(current_time+'/'+place_id) 
    with open(current_time+'/'+place_id+'/websites.json', 'w') as f:
        json.dump(dd, f)
    with open(current_time+'/'+'websites.txt', 'a') as f:
        f.write(website+'\n')

        
POSTCODE = 0
STATE = 2
LAT = 5
LON = 6

#APIKEY = "xxxx" #steven key
APIKEY = "xxxx" # four season key
URL_details = "https://maps.googleapis.com/maps/api/place/details/json"
radius = 500
type = 'shop'
emails = set()
target_state = 'VIC'
# https://www.training.nsw.gov.au/about_us/postcodes_byregion.html
input_file = "vic.txt"
contact = []
contact.append('')
contact.append('contact')
contact.append('contactus.html')
contact.append('contactus')
contact.append('contact-us')

def getdata(lat, lon, radius, type, APIKEY):
    URL = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    # https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8612266,151.2099422&radius=500&types=food&key=AIzaSyC1wet9G4qkNFzOD9TKE48G5ueToMWg_GQ 
    PARAMS = {'location':str(lat)+','+str(lon), 'radius':str(radius), 'types':type, 'key':APIKEY} 
    r = requests.get(url = URL, params = PARAMS) 
    return r.json() 

def saveids(cords, current_time, radius, APIKEY):
    ids = set()
    with open(current_time+"/ids.txt", "a") as f:
        for i in range(0,len(cords)): 
            cord = cords[i]
            print(i, cord)
            data = getdata(cord[0], cord[1], radius, type, APIKEY)
            for result in data['results']:
                place_id = result['place_id']
                # print(place_id)
                if place_id not in ids:
                    ids.add(place_id)
                    f.write(place_id+'\n')  

if __name__ == '__main__':

    now = datetime.now()
    current_time = now.strftime("%d%m%Y%H%M%S")
    os.mkdir(current_time) 
    visited=set()
    cords = list()
    with open(input_file, "r")as f:
        for line in f:
            print(line)
            arr = line.rstrip().split(',');
            post = arr[POSTCODE][1:-1]
            lat = arr[LAT][1:-1]
            lon = arr[LON][1:-1]
            state = arr[STATE][1:-1]
            if lat+lon in visited:
                continue
            if state != target_state:
                continue
            visited.add(lat+lon)
            cords.append((lat,lon))
    saveids(cords,current_time, radius)
          
                    
    #print("place_id is "+place_id)
    # https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJZ934S0KuEmsR_0lxV3PTR4M&fields=name,rating,formatted_phone_number,website&key=AIzaSyC1wet9G4qkNFzOD9TKE48G5ueToMWg_GQ

	#print(ids)
	#mp_handler(ids)
