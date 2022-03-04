from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
import requests
from decouple import config
from django.contrib.auth.models import User
from .forms import *
from .models import *
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    foods = Food.objects.filter(user_id = current_user.id).all()
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user = request.user
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('update')

    return render(request, 'index.html',{"profile":profile,'foods':foods})



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

def profile(request, pk):
    user = User.objects.get(pk=pk)
    profile = Profile.objects.filter(user=user).all()
    current_user = request.user
   
    return render(request, 'profile.html', {'profile':profile,'user':user})


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
        current_user = request.user
        saved_food = Food.objects.create(user_id=current_user.id,name=name,calories=calories,fat=fat,sugar=sugar,sodium=sodium,protein=protein,carbs=carbs,fibre=fibre,serving=serving)
        saved_food.save()
        context = {
            'items':items,'sugar':sugar,'fibre':fibre,'serving':serving,'sodium':sodium,'fat':fat,'calories':calories,'cholesterol':cholesterol,'protein':protein,'carbs':carbs,'name':name
        }
        print(items)
    return render(request, 'search.html', context)


def delete(request, pk):
    Food.objects.filter(id=pk).delete()
    food = Food.objects.all() 
    context = {'food':food}
    return render(request, 'index.html', context) 