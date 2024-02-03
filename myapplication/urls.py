
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.homepage,name='Homepage'),
    path("submit",views.submit_btn,name='submit'),
    path("register",views.register,name='Register'),
    path("login",views.login_page,name='Login'),
    path("dashboard",views.dashboard,name='Dashboard')
]
