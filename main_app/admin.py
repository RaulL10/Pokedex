from django.contrib import admin
from .models import Pokemon, Training, Pokeball
# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Training)
admin.site.register(Pokeball)