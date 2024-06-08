from django.urls import path
from . import views

urlpatterns =[
    path('', views.shortenLink, name='shortenLink'),
    path('short/<str:pk>', views.redirecttoURL, name='redirecttoURL'),
    path('checkLabel/<str:pk>', views.checkUrlLabel, name='checkLabel'),
]