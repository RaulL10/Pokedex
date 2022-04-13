from django.shortcuts import render, redirect
from .models import Pokeball, Pokemon, Pokeball
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import TrainingForm



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemons_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'pokemons': pokemons})

def pokemons_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    training_form = TrainingForm()
    return render(request, 'pokemon/detail.html', {
        'pokemon': pokemon, 'training_form': training_form
    })

def add_training(request, pokemon_id):
    form = TrainingForm(request.POST)
    if form.is_valid():
        new_training = form.save(commit=False)
        new_training.pokemon_id = pokemon_id
        new_training.save()
        return redirect('detail', pokemon_id=pokemon_id)

class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'

class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ['type', 'ability', 'description']

class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = '/pokemons/'

class PokeballList(ListView):
    model = Pokeball

class PokeballDetail(DetailView):
    model = Pokeball

class PokeballCreate(CreateView):
    model = Pokeball
    fields = '__all__'

class PokeballUpdate(UpdateView):
    model = Pokeball
    fields = ['name', 'color']

class PokeballDelete(DeleteView):
    model = Pokeball
    success_url = '/pokeballs/'

