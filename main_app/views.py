from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Leprechaun, Weapon
from .forms import FeedingForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def leprechauns_index(request):
    leprechauns = Leprechaun.objects.all()
    return render(request, 'leprechauns/index.html', { 'leprechauns': leprechauns })

def leprechauns_detail(request, leprechaun_id):
  leprechaun = Leprechaun.objects.get(id=leprechaun_id)
  feeding_form = FeedingForm()
  return render(request, 'leprechauns/detail.html', {
    'leprechaun': leprechaun, 'feeding_form': feeding_form
  })
def add_feeding(request, leprechaun_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.leprechaun_id = leprechaun_id
    new_feeding.save()
  return redirect('detail', leprechaun_id=leprechaun_id)

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

class WeaponList(ListView):
  model = Weapon

class WeaponDetail(DetailView):
  model = Weapon

class WeaponCreate(CreateView):
  model = Weapon
  fields = '__all__'

class WeaponUpdate(UpdateView):
  model = Weapon
  fields = ['name', 'special']

class WeaponDelete(DeleteView):
  model = Weapon
  success_url = '/weapons/'