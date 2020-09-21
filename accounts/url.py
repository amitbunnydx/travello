from django.urls import path
from . import views
urlpatterns = [
    path('register', views.register, name="register"),
    path('login',views.login, name="login"),
    path('logout',views.logout, name="logout"),
    path('Mumbai',views.Mumbai, name="Mumbai"),
    path('pune',views.pune, name="pune"),
    path('Hydrabad',views.Hydrabad, name="Hydrabad"),
    path('Bangalore',views.Bangalore, name="Bangalore"),
   
   
]
