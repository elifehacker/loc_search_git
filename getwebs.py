from area_cordgen import get_web
import os
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%d%m%Y%H%M%S")
os.mkdir(current_time) 

with open('20201218201612_sydn4/ids.txt', "r")as f:
    counter = 0
    ids = set()
    for id in f:
        id = id.rstrip("\n")
        print(counter, id)
        ids.add(id)
        counter+=1
input("Press Enter to continue...")       
counter = 0
for id in ids:
    try:
        get_web(id, current_time)
        counter+=1
        print(counter, id)
    except:
        pass
