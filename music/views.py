from django.shortcuts import render
from django.http import  HttpResponse
from .models import Album
# Create your views here.

def index (request) :
	albums = Album.objects.all()
	html = ""
	return  HttpResponse(html)

# for a in albums 
# 	url = "/music/"+str(a.id) 
# 	html+= '<a href = "'+url+'">' + url+ ' </a>'


def detail(request,album_id):

	html = ""
	return HttpResponse("<h2>detail of album_id "+str(album_id)+"</h2>")
	