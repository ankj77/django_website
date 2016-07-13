from django.conf.urls import  url
from . import views


app_name = 'music'

urlpatterns = [

# /music
     url(r'^$',views.index),

# /music/34/

     url(r'^(?P<album_id>[0-9]+)/$' ,views.detail,name='detail'),

# /music/34/favorite

     url(r'^(?P<album_id>[0-9]+)/favorite/$' ,views.favorite,name='favorite'),

]