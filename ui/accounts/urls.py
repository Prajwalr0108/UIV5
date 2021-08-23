from ui.views import logout
from django.urls import path

from . import views

urlpatterns = [

    path("login", views.login, name='login'),
    path("register", views.register, name="register"),
 
   
    path("logout",views.logout,name="logout"),
    path("accounts/logout",views.logout,name="logout")
    ]
