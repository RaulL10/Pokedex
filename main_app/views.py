from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Pokemon:
    def __init__(self, name, type, ability, description):
        self.name = name
        self.type = type
        self.ability = ability
        self.description = description

pokemons = [
    Pokemon('Bulbasaur', 'Grass', 'Razor Leaf', 'There is a plant seed on its back right from the day its born. The see slowly grows larger.'),
    Pokemon('Charmander', 'Fire', 'Ember', 'It has a preference for hot things. When it rains, steam is said to spout from the tip of its tail.'),
    Pokemon('Squirtle', 'Water', 'Water Gun', 'When it retracts its long neck into its shell, it squirts out water with vigorous force.'),
    Pokemon('Pikachu', 'Electric', 'Thunderbolt', 'Pikachu that can generate powerful electricity and have cheek sacs that are extra soft and super stretchy.'),
]



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def pokemon_index(request):
    return render(request, 'pokemon/index.html')
