from django.shortcuts import render, redirect
from .models import Pokemon
# Create your views here.
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import TrainingForm

# class Pokemon:
#     def __init__(self, name, type, ability, description):
#         self.name = name
#         self.type = type
#         self.ability = ability
#         self.description = description

# pokemons = [
#     Pokemon('Bulbasaur', 'Grass', 'Razor Leaf', 'There is a plant seed on its back right from the day its born. The see slowly grows larger.'),
#     Pokemon('Charmander', 'Fire', 'Ember', 'It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.'),
#     Pokemon('Squirtle', 'Water', 'Water Gun', 'When it retracts its long neck into its shell, it squirts out water with vigorous force.'),
#     Pokemon('Pikachu', 'Electric', 'Thunderbolt', 'Pikachu that can generate powerful electricity and have cheek sacs that are extra soft and super stretchy.'),
# ]



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