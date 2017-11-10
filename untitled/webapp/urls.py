from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api', views.receive, name='index'),
    
url(r'^chart', views.chart, name= 'chart'),
    
    url(r'^index', views.index, name= 'index'),
    url(r'^about', views.about, name= 'about'),
    url(r'^get', views.get, name= 'get'),
    url(r'^getmotion', views.getmotion, name= 'about'),
    

    
]
