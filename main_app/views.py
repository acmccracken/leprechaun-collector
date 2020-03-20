from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Leprechaun, Weapon
from .forms import FeedingForm

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def leprechauns_index(request):
    leprechauns = Leprechaun.objects.filter(user=request.user)
    return render(request, 'leprechauns/index.html', { 'leprechauns': leprechauns })

@login_required
def leprechauns_detail(request, leprechaun_id):
  leprechaun = Leprechaun.objects.get(id=leprechaun_id)
  weapons_leprechaun_doesnt_have = Weapon.objects.exclude(id__in = leprechaun.weapons.all().values_list('id'))
  feeding_form = FeedingForm()
  return render(request, 'leprechauns/detail.html', {
    'leprechaun': leprechaun, 'feeding_form': feeding_form,
    'weapons': weapons_leprechaun_doesnt_have
  })

@login_required
def add_feeding(request, leprechaun_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.leprechaun_id = leprechaun_id
    new_feeding.save()
  return redirect('detail', leprechaun_id=leprechaun_id)

@login_required
def assoc_weapon(request, leprechaun_id, weapon_id):
  # Note that you can pass a weapon's id instead of the whole object
  Leprechaun.objects.get(id=leprechaun_id).weapons.add(weapon_id)
  return redirect('detail', leprechaun_id=leprechaun_id)

@login_required
def unassoc_weapon(request, leprechaun_id, weapon_id):
  Leprechaun.objects.get(id=leprechaun_id).weapons.remove(weapon_id)
  return redirect('detail', leprechaun_id=leprechaun_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class LeprechaunCreate(LoginRequiredMixin, CreateView):
  model = Leprechaun
  fields = ['name', 'power', 'description', 'age']
  success_url = '/leprechauns/'
  def form_valid(self, form):
    form.instance.user = self.request.user  # form.instance is the leprechaun
    return super().form_valid(form)

class LeprechaunUpdate(LoginRequiredMixin, UpdateView):
  model = Leprechaun
  # Let's disallow the renaming of a leprechaun by excluding the name field!
  fields = ['power', 'description', 'age']

class LeprechaunDelete(LoginRequiredMixin, DeleteView):
  model = Leprechaun
  success_url = '/leprechauns/'

class WeaponList(LoginRequiredMixin, ListView):
  model = Weapon

class WeaponDetail(LoginRequiredMixin, DetailView):
  model = Weapon

class WeaponCreate(LoginRequiredMixin, CreateView):
  model = Weapon
  fields = '__all__'

class WeaponUpdate(LoginRequiredMixin, UpdateView):
  model = Weapon
  fields = ['name', 'special']

class WeaponDelete(LoginRequiredMixin, DeleteView):
  model = Weapon
  success_url = '/weapons/'