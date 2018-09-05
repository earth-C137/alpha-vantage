"""
This is a simple Python3 api module/function for alphavantage, that retrieves data in csv format and saves it.
I'm new to programming so it may not be perfect, but does what I want.
I'll add features as I get time.
"""

#You need requests for this, see: http://docs.python-requests.org/en/master/
import requests
#For csv files
import csv
import sqlite_query
#Needed for timer to not exceed free downloads
import time
#For file paths
import os

#variables

#Replace /your/file/path.sqlite with the appropriate path
save_to = '/your/file/path/'
table_name = 'Stock_List'
#Put your alphavantage api key here
api_key = 'Your API Key'
#needed for timer
start_time = time.time()
#not needed, but great way to feed stocks to the api
#I use a list generated from a sqlite database or a csv file
stock_list = []

#alphavantage api for reference
"""
https://www.alphavantage.co/query?
function=TIME_SERIES_DAILY_ADJUSTED
symbol=MSFT
datatype=csv
apikey=
outputsize=full
"""

def get_ticker(save_to, stock_list):
    #counter is so if something happens you know where you are in your list and can resume at that location(manually)
    counter = 0
    for each in stock_list:
        print(counter)
        print(each)
        counter+=1
        payload = {'function':'TIME_SERIES_DAILY_ADJUSTED', 'symbol': '{}'.format(each), 'datatype':'csv',\
        'apikey': '{}'.format(api_key), 'outputsize':'full'}
        r = requests.get('https://www.alphavantage.co/query?', params=payload)
        if r.raise_for_status() is None:
        #this will make a response object called r
        #print(r.url)#for testing that is constructed correctly
            #Saves each downloaded file as csv to save_to folder as stock.csv
            file = open('{}{}.csv'.format(save_to, each), 'w+')
            file.write(r.text)
            file.close()
            time.sleep(13 -((time.time() - start_time) % 13))
        else:
            print(r.raise_for_status)


if __name__=='__main__':
    get_ticker(save_to, stock_list)
