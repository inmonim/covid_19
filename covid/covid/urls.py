"""covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project.views import index, index2, index3
from project.views import baro1, baro2, baro3, baro4
from project.views import movement1, movement2, movement3
from project.views import vaccine1, vaccine2, vaccine3, vaccine1_2, vaccine1_3
from project.views import mask1, mask2
from project.views import line_graph

from project.views import test

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index2', index2),
    path('index3', index3),

    path('baro1', baro1),
    path('baro2', baro2),
    path('baro3', baro3),
    path('baro4', baro4),

    path('movement1', movement1),
    path('movement2', movement2),
    path('movement3', movement3),

    path('vaccine1', vaccine1),
    path('vaccine2', vaccine2),
    path('vaccine3', vaccine3),
    path('vaccine1_2', vaccine1_2),
    path('vaccine1_3', vaccine1_3),

    path('mask1', mask1),
    path('mask2', mask2),

    path('line', line_graph),

    path('test', test)
]
