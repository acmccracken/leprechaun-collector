from django.db import models

# Create your models here.

class Leprechaun:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, power, description, age):
    self.name = name
    self.power = power
    self.description = description
    self.age = age

leprechauns = [
  Leprechaun('Frederick', 'tabby', 'foul little demon', 3),
  Leprechaun('Ohoulihan', 'tortoise shell', 'diluted tortoise shell', 0),
  Leprechaun('McGill', 'black tripod', '3 legged leprechaun', 4)
]