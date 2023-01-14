import csv
import redis
import json
import pandas_datareader as web
from matplotlib import pyplot as plt
import yfinance as yf
import matplotlib  as mat
import datetime as dt
from datetime import timedelta

def connectredis(database):
     redis_client=redis.Redis(host='localhost',port=6370,db=database)
     return redis_client

def getdata(tickers,int):
   
   start=dt.date.today()- timedelta(days=7)
   
   end=dt.date.today()
   #get data from yfinance
   data = yf.download(tickers, start, end,interval = int)
   #print(data)
   
   return data

def datatocsv(data,tickers):
     #put data extracted from the api in a csv file
    data['High'].to_csv(f'django_redis_demo/Functions/stock_data/{tickers}.csv')
    


def setdataredis(redis_client,tickers):
        #get data from csv file
        f="django_redis_demo/Functions/stock_data/"+tickers+".csv"
        file = open(f)
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)
        
        #turn rows of csv to list
        rows = []
        for row in csvreader:
                rows.append(row)
        
        
        lst=[]
        for i in rows:
            y=0
            #generate the redis keys for the data
            i[y]=i[y].replace("-","")
            i[y]=i[y].replace(":","")
            i[y]=i[y].replace(" ","")+tickers
            y=y+1
            lst.append(i)
        #print(lst)
            
        #set data'list in redis
        for row in lst:
            for r in rows:
             if(r==row):
                 break
             else:
                _key=row[0]
                _val=row[1]
                redis_client.set(name=_key,value=_val)

        
        
        return lst

def filter(rows,redis):
    for row in rows:
        last=redis.get(row[1])
        
        for key in redis.keys("*"):
            data=redis.get(key)
            if (data==last) :

                break
            else:
             _key=row[0]
             _val=row[1]
             redis.set(name=_key,value=_val)
                
        

    
if __name__=="__main__":
    tickers=["TSLA","AAPL","MSFT","GOOGL","AMZN","BRK-A","NVDA","TSM","META","NKE","MSFT","CSCO","MCD","KO","EURUSD=X","USD","JPY=X","GBPUSD=X","NZDUSD=X","AUDUSD=X","SGD=X","DZDUSD=X","KWDUSD=X"]
    
    
    for ticker in tickers:
        rc=connectredis(0)
        data=getdata(ticker,"1m")
        datatocsv(data,ticker)
        lst=setdataredis(rc,ticker)
        
 
        

    