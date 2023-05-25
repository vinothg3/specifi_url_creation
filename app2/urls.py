from app2.views import *
from django.urls import path

app_name='app2'

urlpatterns=[
    path('app2_string/',app2_string,name='app2_string'),
    path('app2_htpage/',app2_htpage,name='app2_htpage'),
]