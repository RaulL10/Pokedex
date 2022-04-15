from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Pokemon, Pokeball, Photo
from .forms import TrainingForm
import boto3
import uuid
import os


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def pokemons_index(request):
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemon/index.html', {'pokemons': pokemons})


@login_required
def pokemons_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    id_list = pokemon.pokeballs.all().values_list('id')
    pokeballs_pokemon_doesnt_have = Pokeball.objects.exclude(id__in=id_list)
    training_form = TrainingForm()
    return render(request, 'pokemon/detail.html', {
        'pokemon': pokemon, 'training_form': training_form, 'pokeballs': pokeballs_pokemon_doesnt_have
    })


@login_required
def add_training(request, pokemon_id):
    form = TrainingForm(request.POST)
    if form.is_valid():
        new_training = form.save(commit=False)
        new_training.pokemon_id = pokemon_id
        new_training.save()
        return redirect('detail', pokemon_id=pokemon_id)


@login_required
def assoc_pokeball(request, pokemon_id, pokeball_id):
    Pokemon.objects.get(id=pokemon_id).pokeballs.add(pokeball_id)
    return redirect('detail', pokemon_id=pokemon_id)



@login_required
def add_photo(request, pokemon_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(url=url, pokemon_id=pokemon_id)
        except Exception as e:
            print('An error occured uploading file to S3')
            print(e)
    return redirect('detail', pokemon_id=pokemon_id)


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



class PokemonCreate(LoginRequiredMixin, CreateView):
    model = Pokemon
    fields = ['name', 'type', 'ability', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)


class PokemonUpdate(LoginRequiredMixin, UpdateView):
    model = Pokemon
    fields = ['type', 'ability', 'description']

class PokemonDelete(LoginRequiredMixin, DeleteView):
    model = Pokemon
    success_url = '/pokemons/'

class PokeballList(LoginRequiredMixin, ListView):
    model = Pokeball

class PokeballDetail(LoginRequiredMixin, DetailView):
    model = Pokeball

class PokeballCreate(LoginRequiredMixin, CreateView):
    model = Pokeball
    fields = '__all__'

class PokeballUpdate(LoginRequiredMixin, UpdateView):
    model = Pokeball
    fields = ['name', 'color']

class PokeballDelete(LoginRequiredMixin, DeleteView):
    model = Pokeball
    success_url = '/pokeballs/'

