from django.shortcuts import render
from django.http import  HttpResponse

# Create your views here.

def index (request) :
    return  HttpResponse("<H1> Music App Home Page </H1>")


