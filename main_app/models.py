from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

MEALS = (
    ('G', 'Guinness'),
    ('C', 'Cookies'),
    ('L', 'Lucky Charms')
)

class Weapon(models.Model):
  name = models.CharField(max_length=50)
  special = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('weapons_detail', kwargs={'pk': self.id})

class Leprechaun(models.Model): 
    name = models.CharField(max_length=100)
    power = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    weapons = models.ManyToManyField(Weapon)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def fed_for_today(self):
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('feeding date')
  meal = models.CharField( 
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )
  leprechaun = models.ForeignKey(Leprechaun, on_delete=models.CASCADE)
def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"  
class Meta:
    ordering = ['-date']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'leprechaun_id': self.id})