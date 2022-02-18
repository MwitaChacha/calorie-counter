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
    context = None
    if 'food' in request.GET:
        food = request.GET.get('food')
        url = "https://calorieninjas.p.rapidapi.com/v1/nutrition"
        
        querystring = {"query":food}
        
        headers = {
            'x-rapidapi-host': "calorieninjas.p.rapidapi.com",
            'x-rapidapi-key': config("calorie_key")
            }
        
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        items=response['items']
        sugar=items[0]['sugar_g']
        fibre=items[0]['fiber_g']
        serving=items[0]['serving_size_g']
        sodium=items[0]['sodium_mg']
        fat=items[0]['fat_total_g']
        calories=items[0]['calories']
        cholesterol=items[0]['cholesterol_mg']
        protein=items[0]['protein_g']
        carbs=items[0]['carbohydrates_total_g']
        context = {
            'items':items,'sugar':sugar,'fibre':fibre,'serving':serving,'sodium':sodium,'fat':fat,'calories':calories,'cholesterol':cholesterol,'protein':protein,'carbs':carbs
        }
        print(items)
    return render(request, 'search.html', context)