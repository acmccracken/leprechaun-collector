from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('Home')

def about(request):
    return render(request, 'about.html')

def leprechauns_index(request):
    return render(request, 'leprechauns/index.html', { 'leprechauns': leprechauns })