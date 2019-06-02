from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from college import views
from django.conf.urls import url
from django.views.generic.base import RedirectView
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework import routers

router = routers.DefaultRouter() 
router.register(r'movie', views.MovieViewSet)

urlpatterns = [ 
    path('home/', views.home),
    path('about/', views.about),   
    path('contact/', views.contact),  
    path('notallow/', views.notallow), 
    path('movie/', views.MovieList.as_view()),     
    path('movie/create/', views.MovieCreate.as_view()), 
    url('movie/(?P<pk>[0-9]+)$', views.MovieDetails.as_view()), 
    url('movie/edit/(?P<pk>[0-9]+)$', views.MovieUpdate.as_view()), 
    url('movie/delete/(?P<pk>[0-9]+)$', views.MovieDelete.as_view()), 
    url(r'^api/', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token),        
    url('^$', RedirectView.as_view(url="home/"))        
]
