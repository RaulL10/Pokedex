from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',  views.about, name='about'),
    path('pokemons/', views.pokemons_index, name='index'),
    path('pokemons/<int:pokemon_id>/', views.pokemons_detail, name='detail'),
    path('pokemons/create/', views.PokemonCreate.as_view(), name='pokemons_create'),
    path('pokemons/<int:pk>/update', views.PokemonUpdate.as_view(), name='pokemons_update'),
    path('pokemons/<int:pk>/delete', views.PokemonDelete.as_view(), name='pokemons_delete'),
    path('pokemons/<int:pokemon_id>/add_training/', views.add_training, name='add_training'),
    path('pokeballs/', views.PokeballList.as_view(), name='pokeballs_index'),
    path('pokeballs/<int:pk>/', views.PokeballDetail.as_view(), name='pokeballs_detail'),
    path('pokeballs/create/', views.PokeballCreate.as_view(), name='pokeballs_create'),
    path('pokeballs/<int:pk>/update/', views.PokeballUpdate.as_view(), name='pokeballs_update'),
    path('pokeballs/<int:pk>/delete/', views.PokeballDelete.as_view(), name='pokeballs_delete'),
    path('pokemons/<int:pokemon_id>/assoc_pokeball/<int:pokeball_id>/', views.assoc_pokeball, name='assoc_pokeball'),
]
