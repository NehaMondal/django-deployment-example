from django.conf.urls import url,include
from django.urls import path
from basic_app import views

app_name = 'basic_app'
urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.user_login, name = 'user_login'),
]
