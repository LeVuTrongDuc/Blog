from django.urls import path
from . import views
urlpatterns = [ 
    path('', views.index),
    path('contact/', views.contact),
    
]
from django.urls import path 
from . import views 
from django.contrib.auth import views as auth_views

urlpatterns = [ 
    #HOME
    path('', views.index),
    path('contact/', views.contact,name='contact'),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path("register/", views.register, name="register"),
]


