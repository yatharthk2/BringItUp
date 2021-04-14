from django.urls import path
from . import views

urlpatterns = [

   path('',views.index, name='index'),
   path('login',views.login, name='login'),  
   path('postsign',views.postsign, name='postsign'), 
   path('postsignup',views.postsignup, name='postsignup'), 
   path('logout',views.logout, name="log")
   
    
]