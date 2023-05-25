from app.views import *
from django.urls import path 

app_name='app'

urlpatterns=[
    path('app_string/',app_string,name='app_string'),
    path('app_htpage/',app_htpage,name='app_htpage')
]