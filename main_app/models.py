from django.db import models
from django.forms import IntegerField
from django.urls import reverse
# Create your models here.


HOURS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening'),
)


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    ability = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

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
    date = models.DateField()

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()}"