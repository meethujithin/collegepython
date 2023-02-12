from .import views
from django.urls import path

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name="login"),
    path('logout',views.logout,name='logout'),
    path('next',views.next,name='next'),
    path('order',views.order,name='order'),
    path('message',views.message,name="message"),

]