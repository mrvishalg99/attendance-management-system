from django.shortcuts import render, redirect, HttpResponseRedirect

def home(request):
    return render(request, 'home.html')
