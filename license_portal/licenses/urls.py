from django.urls import path
from django.conf.urls import include

from licenses.views import *

urlpatterns = [
    path('', HomeView, name='HomeView'),
]