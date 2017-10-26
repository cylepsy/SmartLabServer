from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.hello, name='hello'),
    
url(r'^/chart/', views.chart, name='chart'),
    url(r'^/nchart/', views.nchart, name ='nchart'),
    url(r'^/index/', views.index, name= 'index'),
    url(r'^/about/', views.about, name= 'about')
    

    ]
