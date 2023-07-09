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
from .views import SingUpView, ProfileUpdate, EmailUpdate

app_name = 'registration'
urlpatterns = [
    path('signup/', SingUpView.as_view(), name='signup'),
    path('profile/', ProfileUpdate.as_view(), name='profile'),
    path('profile/email/', EmailUpdate.as_view(), name='profile_email'),

]
