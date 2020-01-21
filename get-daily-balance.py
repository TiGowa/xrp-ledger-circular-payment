import urllib.request, requests, json, io, sys, datetime, time
from urllib.request import Request, urlopen
from datetime import datetime, timedelta, timezone, tzinfo

wallet = input ("Enter your wallet address:")

def get_balance(date):
    PARAMS = {"date": date , "currency": "XRP", "limit": 1}
    get = requests.get ('http://data.ripple.com/v2/accounts/{}/balances'.format(wallet), params=PARAMS).json()
    xrp_balance = get['balances'][0]['value']
    print(xrp_balance)

curr_date_time = datetime.now()

new_curr_date_time = curr_date_time.strftime("%Y-%m-%dT%H:%M:%SZ")

i=1

while i<=365:
    time_diff = timedelta(hours=-24)
    pre_date_time = curr_date_time + time_diff
    iso_date_time = pre_date_time.strftime("%Y-%m-%dT%H:%M:%SZ")
    #print (iso_date_time)
    get_balance(iso_date_time)
    curr_date_time = pre_date_time 
    i+=1
    time.sleep(0.5)
