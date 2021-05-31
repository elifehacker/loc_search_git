import requests 
import re
from area_cordgen import get_emails
if __name__ == '__main__':
    path = '18122020204521_sydn4_web/'
    get_emails(path+'websites.txt')