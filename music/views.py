from django.shortcuts import render
from django.http import  HttpResponse
from .models import Album
# Create your views here.

def index (request) :
    albums = Album.objects.all()
    html = "<h1>Welcome to Music Album Page</h1>"
    for album in albums :
        url = '/music/'+str(album.id)
        html+=  '<a href="'+url+'">'+album.album_title+' By : '+ album.artist +'</a> <br>'
    return HttpResponse(html)



def detail(request,album_id):

    html = ""
    return HttpResponse("<h2> Detail of Album Id : "+str(album_id)+"</h2>")
