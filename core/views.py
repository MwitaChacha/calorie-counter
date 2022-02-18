from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import requests
from decouple import config
# @login_required(login_url='/accounts/login/')
def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('/accounts/login/')
    return render(request, 'index.html')


def search(request):
    url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
    
    querystring = {"query":"chips"}
    
    headers = {
        'x-rapidapi-host': "calorieninjas.p.rapidapi.com",
        'x-rapidapi-key': config("calorie_key")
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring).json()
    
    print(response)
    return render(request, 'search.html')