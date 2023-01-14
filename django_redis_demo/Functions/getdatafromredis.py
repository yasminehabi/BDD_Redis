import redis
import pandas as pd

def tickers (word,number):
    #number numero de la base de donnée 0 pour les action , 1 pour la devise

    redis_client=redis.Redis(host='localhost',port=6370,db=number)
    keys= redis_client.keys()
    
    #get all keys
    keys= redis_client.keys()
    y=0
    #list of company's values
    lst=[]
    lstDate=[]
    for key in keys:
            k=str(key)
            
            if word in k :
                
                val = redis_client.get(k[2:len(k)-1])
                val=str(val)
                lstDate.append(k[2:10])
                lst.append(val[2:len(val)-1])
                
    
    return lst,lstDate
    
if __name__=="__main__":
    wordlist = ["Tsla","AAPL","MSFT","GOOGL","AMZN","BRK-A","NVDA","TSM","META","NKE","MSFT","CSCO","MCD","KO"]
    for word in wordlist:
         listAct,listDAte=tickers(word,0)
         print("\n\n")
         print(listAct)
         print(listDAte)
         
    devises=["EURUSD","USD","JPY","GBPUSD","NZDUSD","AUDUSD","SGD","DZDUSD","KWDUSD"]
    for word in devises:
         listDvse,listDAte=tickers(word,1)
         print("\n\n")
         print(listDvse)
         print(listDAte)
         