from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Leprechaun
from django.http import HttpResponse

# Define the home view
def home(request):
  return HttpResponse('Home')

def about(request):
    return render(request, 'about.html')

def leprechauns_index(request):
    leprechauns = Leprechaun.objects.all()
    return render(request, 'leprechauns/index.html', { 'leprechauns': leprechauns })

def leprechauns_detail(request, leprechaun_id):
  leprechaun = Leprechaun.objects.get(id=leprechaun_id)
  return render(request, 'leprechauns/detail.html', { 'leprechaun': leprechaun })

class LeprechaunCreate(CreateView):
  model = Leprechaun
  fields = '__all__'
  success_url = '/leprechauns/'

class LeprechaunUpdate(UpdateView):
  model = Leprechaun
  # Let's disallow the renaming of a leprechaun by excluding the name field!
  fields = ['power', 'description', 'age']

class LeprechaunDelete(DeleteView):
  model = Leprechaun
  success_url = '/leprechauns/'