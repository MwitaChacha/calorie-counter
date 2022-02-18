from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# @login_required(login_url='/accounts/login/')
def index(request):
    # if not request.user.is_authenticated:
    #     return redirect('/accounts/login/')
    return render(request, 'index.html')