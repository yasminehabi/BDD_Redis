import redis


# Connect to our Redis instance
redis_instance = redis.StrictRedis(host='localhost',
                                  port=6370, db=0)   
redis_inst = redis.StrictRedis(host='localhost',
                                  port=6370, db=1)  
        
def setlastdata():
        
        items = {}
        iteems = {}
        sortedval={}


        wordlist = ["TSLA","AAPL","MSFT","GOOGL","AMZN","BRK-A","NVDA","TSM","META","NKE","MSFT","CSCO","MCD","KO","EURUSD=X","USD","JPY=X","GBPUSD=X","NZDUSD=X","AUDUSD=X","SGD=X","DZDUSD=X","KWDUSD=X"]
        for word in wordlist:
          for key in redis_instance.keys("*"):
             k=str(key)
            
             if word in k :
              items[key.decode("utf-8")] = redis_instance.get(key)

              
          keysword=list(items.keys())
          keysword.sort()
          for j in keysword:
              sortedval[j]=redis_instance.get(j)
          iteems[word]=redis_instance.get(j)
          items={}
          sortedval={}
       
          val=redis_instance.get(j)
          
          
          redis_inst.set(name=word,value=val)

if __name__=="__main__":
    setlastdata()
          