from django.http import HttpResponse
from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    # app_id=f41e59c8
    # app_key=782e86637272347046762cec77812fef	
    # url=https://api.edamam.com/api/recipes/v2?type=public&q=bananas&app_id=f41e59c8&app_key=782e86637272347046762cec77812fef
    response_data=requests.get("https://api.edamam.com/api/recipes/v2?type=public&q=pizza&app_id=f41e59c8&app_key=782e86637272347046762cec77812fef")
    json_response=response_data.json()
    recipes=json_response["hits"]
    return render(request,'recipes/index.html',{'recipes':recipes})


def search(request):
    if request.method=='POST':
        user_text=request.POST.get('userText')
        response_data=requests.get("https://api.edamam.com/api/recipes/v2?type=public&q="+user_text+"&app_id=f41e59c8&app_key=782e86637272347046762cec77812fef")
        json_response=response_data.json()
        recipes=json_response["hits"]
        return render(request,'recipes/index.html',{'recipes':recipes})
    else: 
        return render(request,'recipes/index.html',)
    
def contact(request):
    return render(request,'recipes/contact.html')
def about(request):
    return render(request,'recipes/about.html')

