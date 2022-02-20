from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('search-for-food-calories/',views.search,name='search'),
    path('your-meals/',views.meals,name='meals'),
    path('update-your-image/',views.update,name='update'),
]
