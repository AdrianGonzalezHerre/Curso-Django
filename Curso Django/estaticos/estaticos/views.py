
from django.shortcuts import render

def estatico (request):
    return render (request,'estatico.html',{})