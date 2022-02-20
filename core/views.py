from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import requests
from decouple import config
from django.contrib.auth.models import User
from .forms import *
from .models import *



def index(request):

    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile = User.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('update')

    return render(request, 'index.html',{"profile":profile})



@login_required(login_url='/accounts/login/')
def update(request):
    current_user = request.user
    form = ProfileForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            prof = form.save(commit=False)
            prof.user = request.user
            prof.save()
            return redirect('index')
        else:
            form = ProfileForm()
    return render(request, 'update.html', {'form': form})


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
        name=items[0]['name']
        fat=items[0]['fat_total_g']
        calories=items[0]['calories']
        cholesterol=items[0]['cholesterol_mg']
        protein=items[0]['protein_g']
        carbs=items[0]['carbohydrates_total_g']
        context = {
            'items':items,'sugar':sugar,'fibre':fibre,'serving':serving,'sodium':sodium,'fat':fat,'calories':calories,'cholesterol':cholesterol,'protein':protein,'carbs':carbs,'name':name
        }
        print(items)
    return render(request, 'search.html', context)


def meals(request):
    current_user = request.user
    form = MealForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect('index')
        else:
            form = MealForm()
    return render(request, 'meals.html',{'form':form})