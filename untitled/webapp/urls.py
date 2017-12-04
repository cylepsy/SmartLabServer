from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api', views.receive, name='index'),
    
url(r'^chart', views.chart, name= 'chart'),
    
    url(r'^index', views.index, name= 'index'),
    url(r'^about', views.about, name= 'about'),
    url(r'^getmotion', views.getMotion, name= 'getMotion'),
    url(r'^gettemp', views.gettemp, name= 'getdata'),
    url(r'^gethum', views.gethum, name= 'getdata'),
    url(r'^getlight', views.getlight, name= 'getdata'),
    url(r'^getweather', views.getWeather, name= 'getweather'),
    url(r'^sendactivity', views.sendMotion, name= 'sendMotion'),
    url(r'^sendweather', views.sendWeather, name= 'sendWeather'),
    url(r'^sendzone', views.sendZone, name= 'sendZone'),
    url(r'^getzone', views.getZone, name= 'getZone'),
    url(r'^showzone', views.zone, name= 'zone'),
    url(r'^showactivity', views.activity, name='activity'),
    url(r'^lighton', views.lightOn, name='lightOn'),




    

    
]
