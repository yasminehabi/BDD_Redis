import json
from django.conf import settings
import redis
from django.shortcuts import render


# Connect to our Redis instance
redis_instance = redis.StrictRedis(host=settings.REDIS_HOST,
                                  port=settings.REDIS_PORT, db=1)


    


def home(request):
        items = {}



        count = 0
        #wordlist = ["TSLA","AAPL","MSFT","GOOGL","AMZN","BRK-A","NVDA","TSM","META","NKE","MSFT","CSCO","MCD","KO","EURUSD=X","USD","JPY=X","GBPUSD=X","NZDUSD=X","AUDUSD=X","SGD=X","DZDUSD=X","KWDUSD=X"]
        #for word in wordlist:
        for key in redis_instance.keys("*"):
             #k=str(key)
            
             #if word in k :
              items[key.decode("utf-8")] = redis_instance.get(key)
              #count += 1
              


              

          
        response = {
            'count': count,
            'msg': f"Found {count} items.",
            'items':items
            
        }
       
        #return Response(response, template_name="api/Templates/show.html",status=200)
        return render(request,'home.html',response) 
    
def action(request):
    return render(request,'action.html')


def home_view(request):
    l=request.GET
    if 'your_name' in l: 
       print(request.GET)
       l=request.GET
       redis_instance.set(l['your_name'], l['your_name'])
    

    

    return render(request, "show.html")

