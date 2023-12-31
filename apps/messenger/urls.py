"""
URL configuration for playground project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from .views import ThreadDetail, ThreadList, add_message, start_thread


app_name = 'messenger'
urlpatterns = [
    path('', ThreadList.as_view(), name='list'),
    path('detail/<int:pk>/', ThreadDetail.as_view(), name='detail'),
    path('thread/<int:pk>/add/', add_message, name='add'),
    path('thread/start/<username>/', start_thread, name='start'),
]
