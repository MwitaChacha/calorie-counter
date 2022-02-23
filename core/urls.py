from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('search-for-food-calories/',views.search,name='search'),
    path('update-your-image/',views.update,name='update'),
    path('your-profile/<pk>',views.profile,name='profile'),
    path('delete/<int:food_id>',views.delete,name='delete'),
]
