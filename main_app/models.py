from django.db import models
from django.forms import IntegerField
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


HOURS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
)

class Pokeball(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pokeballs_detail', kwargs={'pk': self.id})



class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    ability = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    pokeballs = models.ManyToManyField(Pokeball)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})


class Training(models.Model):
    time = models.CharField(
        max_length=1,
        choices=HOURS,
        default=HOURS[0][0]
    )
    type = models.CharField(max_length=200)

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()}"



class Photo(models.Model):
    url = models.CharField(max_length=200)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for pokemon_id: {self.pokemon_id} @{self.url}"
        