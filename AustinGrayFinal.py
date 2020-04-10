# INF360 - Programming in Python
# Austin Gray
# Midterm

"""
This is my take on a text-based collaboration of all the generation 1 Pokémon games 
"""
#Imports
import pickle
import time
import bisect
import sys
import pprint
import random
import math
import os

'Information Dictionaries/Lists'
#All pokemon currently implimented
pokemon = {
    'Bulbasaur':{'type':'Grass', 'hp':45, 'attack':49, 'defense':49, 'special':65, 'speed':45, 'level':1, 'evolve':16},
    'Ivysaur':{'type':'Grass', 'hp':60, 'attack':62, 'defense':63, 'special':80, 'speed':60, 'level':1, 'evolve':32},
    'Venusaur':{'type':'Grass', 'hp':80, 'attack':82, 'defense':83, 'special':100, 'speed':80, 'level':1},
    'Charmander':{'type':'Fire', 'hp':39, 'attack':52, 'defense':43, 'special':50, 'speed':65, 'level':1, 'evolve':16},
    'Charmeleon':{'type':'Fire', 'hp': 58, 'attack':64, 'defense':58, 'special':65, 'speed':80, 'level':1, 'evolve':36},
    'Charizard':{'type':'Fire', 'hp':78, 'attack':84, 'defense': 78, 'special':85, 'speed':100, 'level':1},
    'Squirtle':{'type':'Water', 'hp':44, 'attack':48, 'defense':65, 'special':50, 'speed':43, 'level':1, 'evolve':16},
    'Wartortle':{'type':'Water', 'hp':59, 'attack':63, 'defense':80, 'special':65, 'speed':58, 'level':1, 'evolve':36},
    'Blastoise':{'type':'Water', 'hp':79, 'attack':83, 'defense':100, 'special':85, 'speed':78, 'level':1},
    'Caterpie':{'type':'Bug', 'hp':45, 'attack':30, 'defense':35, 'special':20, 'speed':45, 'level':1, 'evolve':7},
    'Metapod':{'type':'Bug', 'hp':50, 'attack':20, 'defense':55, 'special':25, 'speed':30, 'level':1, 'evolve':10},
    'Butterfree':{'type':'Bug', 'hp':60, 'attack':45, 'defense':50, 'special':80, 'speed':70, 'level':1},
    'Pidgey':{'type':'Flying', 'hp':40, 'attack':45, 'defense':40, 'special':35, 'speed':56, 'level':1, 'exp':0, 'evolve':18},
    'Pidgeotto':{'type':'Flying', 'hp':63, 'attack':65, 'defense':60, 'special':50, 'speed':71, 'level':1, 'exp':0, 'evolve':36},
    'Pidgeot':{'type':'Flying', 'hp':83, 'attack':80, 'defense':75, 'special':70, 'speed':91, 'level':1, 'exp':0},
    'Weedle':{'type':'Bug', 'hp':40, 'attack':35, 'defense':30, 'special':20, 'speed':50, 'level':1, 'evolve':7},
    'Kakuna':{'type':'Bug', 'hp':45, 'attack':25, 'defense':50, 'special':25, 'speed':35, 'level':1, 'evolve':10}, 
    'Beedrill':{'type':'Bug', 'hp':65, 'attack':80, 'defense':80, 'special':45, 'speed':75, 'level':1},
    'Paras':{'type':'Bug', 'hp':35, 'attack':70, 'defense':55, 'special':45, 'speed':25, 'level':1, 'evolve':24},
    'Parasect':{'type':'Bug', 'hp':60, 'attack':95, 'defense':80, 'special':80, 'speed':30, 'level':1},
    'Scyther':{'type':'Bug', 'hp':70, 'attack':110, 'defense':80, 'special':55, 'speed':105, 'level':1},
    'Venonat':{'type':'Bug', 'hp':60, 'attack':55, 'defense':50, 'special':40, 'speed':45, 'level':1, 'evolve':31},
    'Venomoth':{'type':'Bug', 'hp':70, 'attack':65, 'defense':60, 'special':90, 'speed':90, 'level':1},
    'Pinsir':{'type':'Bug', 'hp':65, 'attack':125, 'defense':100, 'special':55, 'speed':85, 'level':1},
    'Ekans':{'type':'Poison',  'hp':35, 'attack':60, 'defense':44, 'special':40, 'speed':40, 'level':1, 'evolve':22},
    'Arbok':{'type':'Poison', 'hp':60, 'attack':85, 'defense':69, 'special':65, 'speed':80, 'level':1},
    'Nidoran (F)':{'type':'Poison',  'hp':55, 'attack':47, 'defense':52, 'special':40, 'speed':41, 'level':1, 'evolve':16},
    'Nidorina':{'type':'Poison', 'hp':70, 'attack':62, 'defense':67, 'special':55, 'speed':56, 'level':1, 'evolve':26},
    'Nidoqueen':{'type':'Ground', 'hp':90, 'attack':82, 'defense':87, 'special':75, 'speed':76, 'level':1},
    'Nidoran (M)':{'type':'Poison', 'hp':46, 'attack':57, 'defense':40, 'special':40, 'speed':50, 'level':1, 'evolve':16},
    'Nidorino':{'type':'Poison', 'hp':61, 'attack':72, 'defense':57, 'special':55, 'speed':65, 'level':1, 'evolve':26},
    'Nidoking':{'type':'Poison', 'hp':81, 'attack':92, 'defense':77, 'special':75, 'speed':85, 'level':1},
    'Grimer':{'type':'Poison', 'hp':80, 'attack':80, 'defense':50, 'special':40, 'speed':25, 'level':1, 'evolve':38},
    'Muk':{'type':'Poison', 'hp':105, 'attack':105, 'defense':70, 'special':65, 'speed':50, 'level':1},
    'Koffing':{'type':'Poison', 'hp':40, 'attack':65, 'defense':95, 'special':60, 'speed':35, 'level':1, 'evolve':35},
    'Wheezing':{'type':'Poison', 'hp':65, 'attack':90, 'defense':120, 'special':85, 'speed':60, 'level':1},
    'Spearow':{'type':'Flying', 'hp':40, 'attack':60, 'defense':30, 'special':31, 'speed':70, 'level':1, 'evolve':20},
    'Fearow':{'type':'Flying', 'hp':65, 'attack':90, 'defense':65, 'special':61, 'speed':100, 'level':1},
    "Farfetche'd":{'type':'Flying', 'hp':52, 'attack':65, 'defense':55, 'special':58, 'speed':60, 'level':1},
    'Doduo':{'type':'Flying', 'hp':35, 'attack':85, 'defense':45, 'special':35, 'speed':75, 'level':1, 'evolve':31},
    'Dodrio':{'type':'Flying', 'hp':60, 'attack':110, 'defense':70, 'special':60, 'speed':100, 'level':1},
    'Zubat':{'type':'Flying', 'hp':40, 'attack':45, 'defense':35, 'special':40, 'speed':55, 'level':1, 'evolve':22},
    'Golbat':{'type':'Flying', 'hp':75, 'attack':80, 'defense':70, 'special':75, 'speed':90, 'level':1},
    'Aerodactyl':{'type':'Flying', 'hp':80, 'attack':105, 'defense':65, 'special':60, 'speed':130, 'level':1},
    'Rattata':{'type':'Normal', 'hp':30, 'attack':56, 'defense':35, 'special':25, 'speed':72, 'level':1, 'evolve':20},
    'Raticate':{'type':'Normal', 'hp':55, 'attack':81, 'defense':70, 'special':50, 'speed':97, 'level':1},
    'Clefairy':{'type':'Normal', 'hp':70, 'attack':45, 'defense':48, 'special':60, 'speed':35, 'level':1, 'evolve':22},
    'Clefable':{'type':'Normal', 'hp':95, 'attack':70, 'defense':73, 'special':85, 'speed':60, 'level':1},
    'Jigglypuff':{'type':'Normal', 'hp':115, 'attack':45, 'defense':20, 'special':25, 'speed':20, 'level':1, 'evolve':32},
    'Wigglytuff':{'type':'Normal', 'hp':140, 'attack':70, 'defense':45, 'special':50, 'speed':45, 'level':1},
    'Meowth':{'type':'Normal', 'hp':40, 'attack':45, 'defense':35, 'special':40, 'speed':90, 'level':1, 'evolve':28},
    'Persian':{'type':'Normal', 'hp':65, 'attack':70, 'defense':60, 'special':65, 'speed':115, 'level':1},
    'Lickitung':{'type':'Normal', 'hp':90, 'attack':55, 'defense':75, 'special':60, 'speed':30, 'level':1},
    'Chansey':{'type':'Normal', 'hp':250, 'attack':5, 'defense':5, 'special':105, 'speed':50, 'level':1},
    'Kangaskhan':{'type':'Normal', 'hp':105, 'attack':95, 'defense':80, 'special':40, 'speed':90, 'level':1},
    'Tauros':{'type':'Normal', 'hp':75, 'attack':100, 'defense':95, 'special':70, 'speed':110, 'level':1},
    'Ditto':{'type':'Normal', 'hp':48, 'attack':48, 'defense':48, 'special':48, 'speed':48, 'level':1},
    'Eevee':{'type':'Normal', 'hp':55, 'attack':55, 'defense':50, 'special':65, 'speed':65, 'level':1},
    'Jolteon':{'type':'Electric', 'hp':65, 'attack':65, 'defense':60, 'special':110, 'speed':130, 'level':1},
    'Flareon':{'type':'Fire','hp':65, 'attack':130, 'defense':60, 'special':110, 'speed':65, 'level':1},
    'Vaporeon':{'type':'Water', 'hp':130, 'attack':65, 'defense':60, 'special':110, 'speed':65, 'level':1},
    'Porygon':{'type':'Normal', 'hp':65, 'attack':60, 'defense':70, 'special':75, 'speed':40, 'level':1},
    'Snorlax':{'type':'Normal', 'hp':160, 'attack':110, 'defense':65, 'special':65, 'speed':30, 'level':1},
    'Pikachu':{'type':'Electric', 'hp':35, 'attack':55, 'defense':30, 'special':50, 'speed':90, 'level':1, 'evolve':28},
    'Raichu':{'type':'Electric', 'hp':60, 'attack':90, 'defense':55, 'special':90, 'speed':100, 'level':1},
    'Magnemite':{'type':'Electric', 'hp':25, 'attack':35, 'defense':70, 'special':95, 'speed':45, 'level':1},
    'Magneton':{'type':'Electric', 'hp':50, 'attack':60, 'defense':95, 'special':120, 'speed':70, 'level':1},
    'Voltorb':{'type':'Electric', 'hp':40, 'attack':30, 'defense':50, 'special':55, 'speed':100, 'level':1, 'evolve':30},
    'Electrode':{'type':'Electric', 'hp':60, 'attack':50, 'defense':70, 'special':80, 'speed':140, 'level':1},
    'Electabuzz':{'type':'Electric', 'hp':65, 'attack':83, 'defense':57, 'special':85, 'speed':105, 'level':1},
    'Zapdos':{'type':'Electric', 'hp':90, 'attack':90, 'defense':85, 'special':125, 'speed':100, 'level':1},
    'Sandshrew':{'type':'Ground', 'hp':50, 'attack':75, 'defense':85, 'special':30, 'speed':40, 'level':1, 'evolve':22},
    'Sandslash':{'type':'Ground', 'hp':75, 'attack':100, 'defense':110, 'special':55, 'speed':65, 'level':1},
    'Diglett':{'type':'Ground', 'hp':10, 'attack':55, 'defense':25, 'special':45, 'speed':95, 'level':1, 'evolve':26},
    'Dugtrio':{'type':'Ground', 'hp':35, 'attack':80, 'defense':50, 'special':70, 'speed':120, 'level':1},
    'Cubone':{'type':'Ground', 'hp':50, 'attack':50, 'defense':95, 'special':40, 'speed':35, 'level':1, 'evolve':28},
    'Marowak':{'type':'Ground', 'hp':60, 'attack':80, 'defense':110, 'special':50, 'speed':95, 'level':1},
    'Rhyhorn':{'type':'Ground', 'hp':80, 'attack':85, 'defense':95, 'special':30, 'speed':25, 'level':1, 'evolve':42},
    'Rhydon':{'type':'Rock', 'hp':105, 'attack':130, 'defense':120, 'special':45, 'speed':40, 'level':1},
    'Geodude':{'type':'Rock', 'hp':40, 'attack':80, 'defense':100, 'special':30, 'speed':20, 'level':1, 'evolve':25},
    'Graveler':{'type':'Rock', 'hp':55, 'attack':95, 'defense':115, 'special':45, 'speed':35, 'level':1, 'evolve':42},
    'Golem':{'type':'Rock', 'hp':80, 'attack':110, 'defense':130, 'special':55, 'speed':45, 'level':1},
    'Onix':{'type':'Rock', 'hp':35, 'attack':45, 'defense':160, 'special':30, 'speed':70, 'level':1},
    'Kabuto':{'type':'Rock', 'hp':30, 'attack':80, 'defense':90, 'special':45, 'speed':55, 'level':1, 'evolve':40},
    'Kabutops':{'type':'Rock', 'hp':60, 'attack':115, 'defense':105, 'special':70, 'speed':80, 'level':1},
    'Vulpix':{'type':'Fire', 'hp':38, 'attack':41, 'defense':40, 'special':65, 'speed':65, 'level':1, 'evolve':32},
    'Ninetales':{'type':'Fire', 'hp':73, 'attack':76, 'defense':75, 'special':100, 'speed':100, 'level':1},
    'Growlithe':{'type':'Fire', 'hp':55, 'attack':70, 'defense':45, 'special':50, 'speed':60, 'level':1, 'evolve':36},
    'Arcanine':{'type':'Fire', 'hp':90, 'attack':110, 'defense':80, 'special':80, 'speed':95, 'level':1},
    'Ponyta':{'type':'Fire', 'hp':50, 'attack':85, 'defense':55, 'special':65, 'speed':90, 'level':1, 'evolve':40},
    'Rapidash':{'type':'Fire', 'hp':65, 'attack':100, 'defense':70, 'special':80, 'speed':105, 'level':1},
    'Magmar':{'type':'Fire', 'hp':65, 'attack':95, 'defense':57, 'special':85, 'speed':93, 'level':1},
    'Moltres':{'type':'Fire', 'hp':90, 'attack':100, 'defense':90, 'special':125, 'speed':90, 'level':1},
    'Oddish':{'type':'Grass', 'hp':45, 'attack':50, 'defense':65, 'special':75, 'speed':30, 'level':1, 'evolve':21},
    'Gloom':{'type':'Grass', 'hp':60, 'attack':65, 'defense':70, 'special':85, 'speed':40, 'level':1, 'evolve':42},
    'Vileplume':{'type':'Grass', 'hp':75, 'attack':80, 'defense':85, 'special':100, 'speed':50, 'level':1},
    'Bellsprout':{'type':'Grass', 'hp':50, 'attack':75, 'defense':35, 'special':70, 'speed':40, 'level':1, 'evolve':21},
    'Weepinbell':{'type':'Grass', 'hp':65, 'attack':90, 'defense':50, 'special':85, 'speed':55, 'level':1, 'evolve':38},
    'Victreebel':{'type':'Grass', 'hp':80, 'attack':105, 'defense':65, 'special':100, 'speed':70, 'level':1},
    'Exeggcute':{'type':'Grass', 'hp':60, 'attack':40, 'defense':80, 'special':60, 'speed':40, 'level':1, 'evolve':38},
    'Exeggutor':{'type':'Grass', 'hp':95, 'attack':95, 'defense':85, 'special':125, 'speed':55, 'level':1},
    'Tangela':{'type':'Grass', 'hp':65, 'attack':55, 'defense':115, 'special':100, 'speed':60, 'level':1},
    'Psyduck':{'type':'Water', 'hp':50, 'attack':52, 'defense':48, 'special':50, 'speed':55, 'level':1, 'evolve':33},
    'Golduck':{'type':'Water', 'hp':80, 'attack':82, 'defense':78, 'special':80, 'speed':85, 'level':1},
    'Poliwag':{'type':'Water', 'hp':40, 'attack':50, 'defense':40, 'special':40, 'speed':90, 'level':1, 'evolve':21},
    'Poliwhirl':{'type':'Water', 'hp':65, 'attack':65, 'defense':65, 'special':50, 'speed':90, 'level':1, 'evolve':32},
    'Poliwrath':{'type':'Fighting', 'hp':90, 'attack':85, 'defense':95, 'special':70, 'speed':70, 'level':1},
    'Tentacool':{'type':'Water', 'hp':40, 'attack':40, 'defense':35, 'special':100, 'speed':70, 'level':1, 'evolve':30},
    'Tentacruel':{'type':'Water', 'hp':80, 'attack':70, 'defense':65, 'special':120, 'speed':100, 'level':1},
    'Slowpoke':{'type':'Water', 'hp':90, 'attack':65, 'defense':65, 'special':40, 'speed':15, 'level':1, 'evolve':37},
    'Slowbro':{'type':'Water', 'hp':95, 'attack':75, 'defense':110, 'special':80, 'speed':30, 'level':1},
    'Seel':{'type':'Water', 'hp':65, 'attack':45, 'defense':55, 'special':70, 'speed':45, 'level':1, 'evolve':34},
    'Dewgong':{'type':'Ice', 'hp':90, 'attack':70, 'defense':80, 'special':95, 'speed':70, 'level':1},
    'Shellder':{'type':'Water', 'hp':30, 'attack':65, 'defense':100, 'special':45, 'speed':40, 'level':1, 'evolve':40},
    'Cloyster':{'type':'Ice', 'hp':50, 'attack':95, 'defense':180, 'special':85, 'speed':70, 'level':1},
    'Krabby':{'type':'Water', 'hp':30, 'attack':105, 'defense':90, 'special':25, 'speed':50, 'level':1, 'evolve':28},
    'Kingler':{'type':'Water', 'hp':55, 'attack':130, 'defense':115, 'special':50, 'speed':75, 'level':1},
    'Horsea':{'type':'Water', 'hp':30, 'attack':40, 'defense':70, 'special':70, 'speed':60, 'level':1, 'evolve':32},
    'Seadra':{'type':'Water', 'hp':55, 'attack':65, 'defense':95, 'special':95, 'speed':85, 'level':1},
    'Goldeen':{'type':'Water', 'hp':45, 'attack':67, 'defense':60, 'special':50, 'speed':63, 'level':1, 'evolve':33},
    'Seaking':{'type':'Water', 'hp':80, 'attack':92, 'defense':65, 'special':80, 'speed':68, 'level':1},
    'Staryu':{'type':'Water', 'hp':30, 'attack':45, 'defense':55, 'special':70, 'speed':85, 'level':1, 'evolve':33},
    'Starmie':{'type':'Water', 'hp':60, 'attack':75, 'defense':85, 'special':100, 'speed':115, 'level':1},
    'Magikarp':{'type':'Water', 'hp':20, 'attack':10, 'defense':55, 'special':20, 'speed':80, 'level':1, 'evolve':20},
    'Gyarados':{'type':'Flying', 'hp':95, 'attack':125, 'defense':79, 'special':100, 'speed':81, 'level':1},
    'Omanyte':{'type':'Water', 'hp':35, 'attack':35, 'defense':100, 'special':90, 'speed':35, 'level':1, 'evolve':40},
    'Omastar':{'type':'Water', 'hp':70, 'attack':70, 'defense':125, 'special':115, 'speed':55, 'level':1},
    'Mankey':{'type':'Fighting', 'hp':40, 'attack':80, 'defense':35, 'special':35, 'speed':70, 'level':1, 'evolve':28},
    'Primeape':{'type':'Fighting', 'hp':65, 'attack':105, 'defense':60, 'special':60, 'speed':95, 'level':1},
    'Machop':{'type':'Fighting', 'hp':70, 'attack':80, 'defense':50, 'special':35, 'speed':35, 'level':1, 'evolve':28},
    'Machoke':{'type':'Fighting', 'hp':80, 'attack':100, 'defense':70, 'special':50, 'speed':45, 'level':1, 'evolve':42},
    'Machamp':{'type':'Fighting', 'hp':90, 'attack':130, 'defense':80, 'special':65, 'speed':55, 'level':1},
    'Hitmonlee':{'type':'Fighting', 'hp':50, 'attack':120, 'defense':53, 'special':35, 'speed':87, 'level':1},
    'Hitmonchan':{'type':'Fighting', 'hp':50, 'attack':105, 'defense':79, 'special':35, 'speed':76, 'level':1},
    'Abra':{'type':'Psychic', 'hp':25, 'attack':20, 'defense':15, 'special':105, 'speed':90, 'level':1, 'evolve':16},
    'Kadabra':{'type':'Psychic', 'hp':40, 'attack':35, 'defense':30, 'special':120, 'speed':105, 'level':1, 'evolve':42},
    'Alakazam':{'type':'Psychic', 'hp':55, 'attack':50, 'defense':45, 'special':135, 'speed':120, 'level':1},
    'Drowzee':{'type':'Psychic', 'hp':60, 'attack':48, 'defense':45, 'special':90, 'speed':42, 'level':1, 'evolve':26},
    'Hypno':{'type':'Psychic', 'hp':85, 'attack':73, 'defense':70, 'special':115, 'speed':67, 'level':1},
    'Mr. Mime':{'type':'Psychic', 'hp':40, 'attack':45, 'defense':65, 'special':100, 'speed':90, 'level':1},
    'Gastly':{'type':'Ghost', 'hp':30, 'attack':35, 'defense':30, 'special':100, 'speed':80, 'level':1, 'evolve':25},
    'Haunter':{'type':'Ghost', 'hp':45, 'attack':50, 'defense':45, 'special':115, 'speed':95, 'level':1, 'evolve':42},
    'Gengar':{'type':'Ghost', 'hp':60, 'attack':65, 'defense':60, 'special':130, 'speed':110, 'level':1},
    'Jynx':{'type':'Ice', 'hp':65, 'attack':65, 'defense':35, 'special':95, 'speed':95, 'level':1},
    'Lapras':{'type':'Ice', 'hp':130, 'attack':85, 'defense':80, 'special':90, 'speed':60, 'level':1},
    'Articuno':{'type':'Ice', 'hp':90, 'attack':85, 'defense':100, 'special':125, 'speed':85, 'level':1},
    'Dratini':{'type':'Dragon', 'hp':41, 'attack':64, 'defense':45, 'special':50, 'speed':50, 'level':1, 'evolve':30},
    'Dragonair':{'type':'Dragon', 'hp':61, 'attack':84, 'defense':65, 'special':70, 'speed':70, 'level':1, 'evolve':55},
    'Dragonite':{'type':'Dragon', 'hp':91, 'attack':134, 'defense':95, 'special':100, 'speed':80, 'level':1},
    'Mew':{'type':'Psychic', 'hp':100, 'attack':100, 'defense':100, 'special':100, 'speed':100, 'level':1},
    'Mewtwo':{'type':'Psychic', 'hp':106, 'attack':110, 'defense':90, 'special':154, 'speed':130, 'level':1}
    }

#To determin the amount of damage one type does to another
#Key is Attacking, Values are defending
# Bug, Dragon, Electric, Fighting, Fire, Flying, Ghost, Grass, Ground, Ice, Normal, Poison, Psychic, Rock, Water
type_chart = {
    'Bug':{'Bug':1, 'Dragon':1, 'Electric':1, 'Fighting':1, 'Fire':0.5, 'Flying':0.5, 'Ghost':1, 'Grass':2, 'Ground':1, 'Ice':1, 'Normal':1, 'Poison':2, 'Psychic':2, 'Rock':0.5, 'Water':1},
    'Dragon':{'Bug':1, 'Dragon':1, 'Electric':1, 'Fighting':1, 'Fire':1, 'Flying':1, 'Ghost':1, 'Grass':1, 'Ground':1, 'Ice':1, 'Normal':1, 'Poison':1, 'Psychic':1, 'Rock':1, 'Water':1},
    'Electric':{'Bug':1, 'Dragon':1, 'Electric':0.5, 'Fighting':1, 'Fire':1, 'Flying':2, 'Ghost':1, 'Grass':0.5, 'Ground':0, 'Ice':1, 'Normal':1, 'Poison':1, 'Psychic':1, 'Rock':1, 'Water':2},
    'Fighting':{'Bug':1, 'Dragon':1, 'Electric':1, 'Fighting':1, 'Fire':1, 'Flying':0.5, 'Ghost':0, 'Grass':1, 'Ground':1, 'Ice':2, 'Normal':2, 'Poison':1, 'Psychic':0.5, 'Rock':2, 'Water':1},
    'Fire':{'Bug':2, 'Dragon':1, 'Electric':1, 'Fighting':1, 'Fire':1, 'Flying':1, 'Ghost':1, 'Grass':2, 'Ground':1, 'Ice':2, 'Normal':1, 'Poison':1, 'Psychic':1, 'Rock':0.5, 'Water':0.5},
    'Flying':{'Bug':2, 'Dragon':1, 'Electric':0.5, 'Fighting':2, 'Fire':1, 'Flying':1, 'Ghost':1, 'Grass':2, 'Ground':1, 'Ice':1, 'Normal':1, 'Poison':1, 'Psychic':1, 'Rock':0.5, 'Water':1},
    'Ghost':{'Bug':1, 'Dragon':1, 'Electric':1, 'Fighting':1, 'Fire':1, 'Flying':1, 'Ghost':1, 'Grass':1, 'Ground':1, 'Ice':1, 'Normal':0, 'Poison':1, 'Psychic':0, 'Rock':1, 'Water':1},
    'Grass':{'Bug':0.5, 'Dragon':1, 'Electric':1, 'Fighting':1, 'Fire':0.5, 'Flying':0.5, 'Ghost':1, 'Grass':0.5, 'Ground':2, 'Ice':1, 'Normal':1, 'Poison':0.5, 'Psychic':1, 'Rock':2, 'Water':2},
    'Ground':{'Bug':1, 'Dragon':1, 'Electric':2, 'Fighting':1, 'Fire':2, 'Flying':0, 'Ghost':1, 'Grass':0.5, 'Ground':1, 'Ice':1, 'Normal':1, 'Poison':2, 'Psychic':1, 'Rock':2, 'Water':1},
    'Ice':{'Bug':1, 'Dragon':2, 'Electric':1, 'Fighting':1, 'Fire':1, 'Flying':2, 'Ghost':1, 'Grass':2, 'Ground':2, 'Ice':0.5, 'Normal':1, 'Poison':1, 'Psychic':1, 'Rock':1, 'Water':0.5},
    'Normal':{'Bug':1, 'Dragon':1, 'Electric':1, 'Fighting':1, 'Fire':1, 'Flying':1, 'Ghost':0, 'Grass':1, 'Ground':1, 'Ice':1, 'Normal':1, 'Poison':1, 'Psychic':1, 'Rock':1, 'Water':1},
    'Poison':{'Bug':2, 'Dragon':1, 'Electric':1, 'Fighting':1, 'Fire':1, 'Flying':1, 'Ghost':1, 'Grass':2, 'Ground':0.5, 'Ice':1, 'Normal':1, 'Poison':0.5, 'Psychic':1, 'Rock':0.5, 'Water':1},
    'Psychic':{'Bug':1, 'Dragon':1, 'Electric':1, 'Fighting':2, 'Fire':1, 'Flying':1, 'Ghost':1, 'Grass':1, 'Ground':1, 'Ice':1, 'Normal':1, 'Poison':2, 'Psychic':0.5, 'Rock':1, 'Water':1},
    'Rock':{'Bug':2, 'Dragon':1, 'Electric':1, 'Fighting':0.5, 'Fire':2, 'Flying':2, 'Ghost':1, 'Grass':1, 'Ground':1, 'Ice':2, 'Normal':1, 'Poison':1, 'Psychic':1, 'Rock':0.5, 'Water':1},
    'Water':{'Bug':1, 'Dragon':1, 'Electric':1, 'Fighting':1, 'Fire':2, 'Flying':1, 'Ghost':1, 'Grass':0.5, 'Ground':2, 'Ice':0.5, 'Normal':1, 'Poison':1, 'Psychic':1, 'Rock':2, 'Water':1}
    }

#Level exp amounts
levels = [0, 8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744,
    3375, 4096, 4913, 5832, 6859, 8000, 9261, 10648, 12167, 13824, 15625, 17576,
    19683, 21952, 24389, 27000, 29791, 32768, 35937, 39304, 42875, 46656, 50653,
    54653, 59319, 64000, 68921, 74088, 79507, 85184, 91125, 97336, 103823, 110592,
    117649, 125000, 132651, 140608, 148877, 157464, 166375, 175616, 185193, 195112,
    205379, 216000, 226981, 238328, 250047, 262144, 274625, 287496, 300763, 314432,
    328509, 343000, 357911, 373248, 389017, 405224, 421875, 438976, 456533, 474552,
    493039, 512000, 531441, 551368, 571787, 592704, 614125, 636056, 658503, 681472,
    704969, 729000, 753571, 778688, 804357, 830584, 857375, 884736, 912673, 941192,
    970299, 1000000]

'''#Moves
physical_moves = {'Barrage':{'type': 'Normal', 'power':15, 'accuracy':85, 'pp':20, 'min hits':2, 'max hits':5},
                'Bind':{'type':'Normal', 'power':15, 'aaccuracy':85, 'pp':20, 'min turns': 4, 'max turns':5},
                'Body Slam':{'type':'Normal', 'power':85, 'accuracy':100, 'pp':15},  #30% chance of paralysis (CAN'T paralyze normal types)
                'Comet Punch':{'type': 'Normal', 'power':18, 'accuracy':85, 'pp':15, 'min hits':2, 'max hits':5},
                'Constrict':{'type': 'Normal', 'power': 10, 'accuracy':100, 'pp':35}
    }
'''
#Global Veriables
"""
name
pstart
"""

#Yes or no question checks
yes = ('Y', 'y', 'yes', 'Yes')
no = ('N', 'n', 'no', 'No')

#Team and stored pokemon
#Note: Can only have 6 Pokemon in a party
team = {}
pc = {}

#Tracking
location = []
badges = []

#Functions
#Title
def title():
    game = "Pokemon FireRed - Text Edition"
    instructions = "Press 'Enter' to continue anytime!"
    loading = '"..." means loading'
    buffer = '#'*32
    print ('''
                         .\"-,.__            
                         `.     `.  ,            
                      .--'  .._,'\"-' `.            
                     .    .'         `'            
                     `.   /          ,'            
                       `  '--.   ,-\"'            
                        `\"`   |  \\            
                           -. \\, |            
                            `--Y.'      ___.            
                                 \\     L._, \\            
                       _.,        `.   <  <\\                _            
                     ,' '           `, `.   | \\            ( `            
                  ../, `.            `  |    .\\`.           \\ \\_            
                 ,' ,..  .           _.,'    ||\\l            )  '\".            
                , ,'   \\           ,'.-.`-._,'  |           .  _._`.            
              ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\            
            .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.            
            |  '          ..         `-...-\"  |  `-'      / /        . `.            
            | /           |L__           |    |          / /          `. `.            
           , /            .   .          |    |         / /             ` `            
          / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\            
         / .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.            
        .  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\            
        ' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`            
        |'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\            
        ||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|            
        ||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||            
        || '              V      / /           `   | `   ,'   ,' '.    !  `. ||            
        ||/            _,-------7 '              . |  `-'    l         /    `||            
        . |          ,' .-   ,' ||               | .-.        `.      .'     ||            
         `'        ,'    `\".'    |               |    `.        '. -.'       `'            
                  /      ,'      |               |,'    \\-.._,.'/'            
                  .     /        .               .       \\    .''            
                .`.    |         `.             /         :_,'.'            
                  \\ `...\\   _     ,'-.        .'         /_.-'            
                   `-.__ `,  `'   .  _.>----''.  _  __  /            
                        .'        /\"'          |  \"'   '_            
                       /_|.-'\\ ,\".             '.'`__'-( \\            
                         / ,\"'\"\\,'               `/  `-.|\"          ''')

    print (buffer.center(75) + '\n' + game.center(75) + '\n' + 
        instructions.center(75) + '\n' + loading.center(75) + '\n' + buffer.center(75))
    input()

#Introduction
def intro():
    global name
    print ('Hello there!\n' + 'Welcome to the world of Pokémon!')
    input()
    print ('My name is Oak, But people affectionately refer to me as the Pokémon professor.')
    input()
    print ('This world is inhabited, far and wide, by creatures called Pokémon!')
    input()
    print ('For some people, Pokémon are pets; others use them for battling.')
    input()
    print ('As for myself, I study Pokémon as a profession.')
    input()
    print ("Let's begin with your name.")
    time.sleep(.75)
    x = True
    while x == True:
        name = input ('What is it?\n')
        y = True
        while y == True:
            print ('\nSo your name is ' + name + '!')
            time.sleep(.75)
            q = input ('Is that correct? (y/n)\n')
            if q in yes:
                x = False
                y = False
                break
            elif q in no:
                y = False
                break
            else:
                print ('Please give a real answer!')
    print ('\n' + name + ', your very own Pokémon legend is about to unfold!')
    input()
    print ("A world of dreams and adventures with Pokémon awaits! Let's go!")
    input()
    starter()

#Starter Pokemon
def starter():
    global pstart
    #Loading Dots
    for _ in range (3):
        for _ in range (3):
            #Prints "..."
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(.75)
        #Deletes "..."
        sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
        sys.stdout.flush()

    print ("\n \nThe next day, you wander into Professor Oak's lab.")
    location.clear()
    location.append('Pallet Town')
    input()
    print ('Prof. Oak:')
    time.sleep(1)
    print ('"When I was young, I was a serious Pokémon trainer."')
    input()
    print ('"But now, in my old age, I only have these three left."')
    input()
    print ('"You may have one!"\n')

    #Loading Dots
    for _ in range (2):
        for _ in range (3):
            #Prints "..."
            sys.stdout.write(".")
            sys.stdout.flush()
            time.sleep(.75)
        #Deletes "..."
        sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
        sys.stdout.flush()
    
    #Choosing Starter
    x = True
    while x == True:
        print ('\nChoose 1,2, or 3')
        starter = input ('1 | 2 | 3 \n')
        y = True
        while y == True:
            try:
                #Bulbasaur
                if int(starter) == 1:
                    print ('Please wait till a question is ask to give input!')
                    time.sleep (1.5)
                    print ('\n1. Bulbasaur')
                    print ('The Seed Pokémon')
                    print (pokemon['Bulbasaur'])
                    time.sleep (3)
                    print('''
                                                _,.------....___,.' ',.-.            
                                            ,-'          _,.--\"        |            
                                        ,'         _.-'              .            
                                        /   ,     ,'                   `            
                                        .   /     /                     ``.            
                                        |  |     .                       \\.\\            
                            ____      |___._.  |       __               \\ `.            
                            .'    `---\"\"       ``\"-.--\"'`  \\               .  \\            
                            .  ,            __               `              |   .            
                            `,'         ,-\"'  .               \\             |    L            
                        ,'          '    _.'                -._          /    |            
                        ,`-.    ,\".   `--'                      >.      ,'     |            
                        . .'\\'   `-'       __    ,  ,-.         /  `.__.-      ,'            
                        ||:, .           ,'  ;  /  / \\ `        `.    .      .'/            
                        j|:D  \\          `--'  ' ,'_  . .         `.__, \\   , /            
                        / L:_  |                 .  \"' :_;                `.'.'            
                        .    \"\"'                  \"\"\"\"\"'                    V            
                        `.                                 .    `.   _,..  `            
                        `,_   .    .                _,-'/    .. `,'   __  `            
                            ) \\`._        ___....----\"'  ,'   .'  \\ |   '  \\  .            
                        /   `. \"`-.--\"'         _,' ,'     `---' |    `./  |            
                        .   _  `\"\"'--.._____..--\"   ,             '         |            
                        | .\" `. `-.                /-.           /          ,            
                        | `._.'    `,_            ;  /         ,'          .            
                        .'          /| `-.        . ,'         ,           ,            
                        '-.__ __ _,','    '`-..___;-...__   ,.'\\ ____.___.'       ''')
                    time.sleep (3)
                    z = True
                    while z == True:
                        q = input('Would you like to choose Bulbasaur? (y/n)\n')
                        if q in yes:
                            #Copies bulbasaur from pokemon to team
                            team.update({key: pokemon[key] for key in pokemon.keys() & {'Bulbasaur'}})
                            pstart = team['Bulbasaur']
                            adjust()
                            x = False
                            y = False
                            z = False
                            break
                        elif q in no:
                            y = False
                            z = False
                            break
                        else:
                            print ('Please Give a proper answer!')
                #Charmander
                elif int(starter) == 2:
                    print ('Please wait till a question is ask to give input!')
                    time.sleep (1.5)
                    print ('\n2. Charmander')
                    print ('The Lizard Pokémon')
                    print (pokemon['Charmander'])
                    time.sleep (3)
                    print('''
                                    _.--\"\"`-..            
                                    ,'          `.            
                                ,'          __  `.            
                                /|          \" __   \\            
                                , |           / |.   .            
                                |,'          !_.'|   |            
                            ,'             '   |   |            
                            /              |`--'|   |            
                            |                `---'   |            
                            .   ,                   |                       ,\".            
                            ._     '           _'  |                    , ' \\ `            
                        `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|            
                        |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\            
                        -:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .            
                        `,         \"\"\"\"'     `.              ,'         |   |  ',,            
                            `.      '            '            /          '    |'. |/            
                            `.   |              \\       _,-'           |       ''            
                                `._'               \\   '\"\\                .      |            
                                |                '     \\                `._  ,'            
                                |                 '     \\                 .'|            
                                |                 .      \\                | |            
                                |                 |       L              ,' |            
                                `                 |       |             /   '            
                                    \\                |       |           ,'   /            
                                ,' \\               |  _.._ ,-..___,..-'    ,'            
                                /     .             .      `!             ,j'            
                                /       `.          /        .           .'/            
                            .          `.       /         |        _.'.'            
                                `.          7`'---'          |------\"'_.'            
                            _,.`,_     _'                ,''-----\"'            
                        _,-_    '       `.     .'      ,\\            
                        -\" /`.         _,'     | _  _  _.|            
                            \"\"--'---\"\"\"\"\"'        `' '! |! /            
                                                    `\" \" -'       ''')                   
                    time.sleep (3)
                    z = True
                    while z == True:
                        q = input('Would you like to choose Charmander? (y/n)\n')
                        if q in yes:
                            #Copies Charmander from pokemon to team
                            team.update({key: pokemon[key] for key in pokemon.keys() & {'Charmander'}})
                            pstart = team['Charmander']
                            adjust()
                            x = False
                            y = False
                            z = False
                            break
                        elif q in no:
                            y = False
                            z = False
                            break
                        else:
                            print ('Please Give a proper answer!')            
                #Squirtle
                elif int(starter) == 3:
                    print ('Please wait till a question is ask to give input!')
                    time.sleep (1.5)
                    print ('\n3. Squirtle')
                    print ('The Tiny Turtle Pokémon')
                    print (pokemon['Squirtle'])
                    time.sleep (3)
                    print('''
                                       _,........__            
                                    ,-'            \"`-.            
                                  ,'                   `-.            
                                ,'                        \\            
                              ,'                           .            
                              .'\\               ,\"\".       `            
                             ._.'|             / |  `       \\            
                             |   |            `-.'  ||       `.            
                             |   |            '-._,'||       | \\            
                             .`.,'             `..,'.'       , |`-.            
                             l                       .'`.  _/  |   `.            
                             `-.._'-   ,          _ _'   -\" \\  .     `            
                        `.\"\"\"\"\"'-.`-...,---------','         `. `....__.            
                        .'        `\"-..___      __,'\\          \\  \\     \\            
                        \\_ .          |   `\"\"\"\"'    `.           . \\     \\            
                          `.          |              `.          |  .     L            
                            `.        |`--...________.'.        j   |     |            
                              `._    .'      |          `.     .|   ,     |            
                                 `--,\\       .            `7\"\"' |  ,      |            
                                    ` `      `            /     |  |      |    _,-'\"\"\"`-.            
                                     \\ `.     .          /      |  '      |  ,'          `.            
                                      \\  v.__  .        '       .   \\    /| /              \\            
                                       \\/    `\"\"\\\"\"\"\"\"\"\"`.       \\   \\  /.''                |            
                                        `        .        `._ ___,j.  `/ .-       ,---.     |            
                                        ,`-.      \\         .\"     `.  |/        j     `    |            
                                       /    `.     \\       /         \\ /         |     /    j            
                                      |       `-.   7-.._ .          |\"          '         /            
                                      |          `./_    `|          |            .     _,'            
                                      `.           / `----|          |-............`---'            
                                        \\          \\      |          |            
                                       ,'           )     `.         |            
                                        7____,,..--'      /          |            
                                                          `---.__,--.'              ''')
                    time.sleep (3)
                    z = True
                    while z == True:
                        q = input('Would you like to choose Squirtle? (y/n)\n')
                        if q in yes:
                            #Copies Squirtle from pokemon to team
                            team.update({key: pokemon[key] for key in pokemon.keys() & {'Squirtle'}})
                            pstart = team['Squirtle']
                            adjust()
                            x = False
                            y = False
                            z = False
                            break
                        elif q in no:
                            y = False
                            z = False
                            break
                        else:
                            print ('Please Give a proper answer!')
                #Hidden Cheat 1 - Dratini
                elif int(starter) == 99:
                    print ('Please wait till a question is asked to give input!')
                    time.sleep (1.5)
                    print ('\nDratini')
                    print ('The Dragon Pokémon')
                    print (pokemon['Dratini'])
                    time.sleep (3)
                    print ('''
                                                          H                      
                                           +             H +                     
                              +HHHH+      + H           +; H                     
                             H+++;;;+H    H +           H; H                     
                            +HH+++;;;;H   H  +   +HHHHH+;; H                     
                            +   H++;;;;H  H; H H+;;;;;;;H  H                     
                                 ++;;;;;+H+;; ++;;;;;;+H;H +                     
                                 H++;;;;H;;H; H;;;;;;H  H;+ +                    
                                  ++;;;;+;;;H H;;+H;;+; +;H H                    
                                  H+;;;;;+;;  H;+  +;;+H;+ +H                    
                                  H+;;;;;H;;  H;HH H;;;;;H H+                    
                                  H;;;;;;H;   H;HHHH;;;;;HHH                     
                                  H;;;;;;H   H+;+HH+;;+HH+H+                     
                                  +;;;;;;+  ++;;;++;+H    H                      
                                 +;;;;;;;;+H H+;;;+H       +                     
                                 H;;;;;;;;H  H+;;++;;      H                     
                                 +;;;;;;;;+   H;;+H;;;;    +                     
                                +;;;;;;;;;;+  H+;++;;;;;; +                      
                                H;;;;;;;;;;H  H+;;+H+;;;;+                       
                                H;;;;;;;;;+H  H+;;H;;+HH+                        
                                H;;;;;;;;;+H  H+;+  ;;;H                         
                                H;;;;;;;;;++H H+;H      +                        
                                H;;;;;;;;;++HH+;;+      H                        
                                H;;;;;;;;;+++H;;+       +                        
                                H;;;;;;;;;;+H;;;H        +                       
                                H+;;;;;;;;;H;;;;+        H                       
                                +++;;;;;;;;;;;;H         H                       
                                 H++;;;;;;;;;;;+         H                       
                                 ++++;;;;;;;;;+          +                       
                                  H+++++;;;;;;H         +                        
                                  H++++++++++H;;;       H                        
                                   H++++++++H;;;;;;    +                         
                                    H++++++H;;;;;;;;  H                          
                                     H+++H+;;;;;;;;; H                           
                                      +HH;;;;;;;;;;H+                            
                                         +H;;;;;;H+                              
                                           +HHHH+                    ''')
                    time.sleep (3)
                    z = True
                    while z == True:
                        q = input('Would you like to choose Dratini? (y/n)\n')
                        if q in yes:
                            #Copies Dratini from pokemon to team
                            team.update({key: pokemon[key] for key in pokemon.keys() & {'Dratini'}})
                            pstart = team['Dratini']
                            adjust()
                            x = False
                            y = False
                            z = False
                            break
                        elif q in no:
                            y = False
                            z = False
                            break
                        else:
                            print ('Please Give a proper answer!')
                #Hidden Cheat 2 - MewTwo
                elif int(starter) == 100:
                    print ('Please wait till a question is asked to give input!')
                    time.sleep (1.5)
                    print ('\nMewtwo')
                    print ('The Genetic Pokémon')
                    print (pokemon['Mewtwo'])
                    time.sleep (3)
                    print ('''
                                                                                               `/:+`                      ```                                            
                                                                          :- .+`     `....``        -+-:/:                                          
                                                                          ./. `/--:::-....--:::::-./:   +.                                          
                                                                           `/.  .`              `.:`  `/.                                           
                                                                            `/                       `+`                                            
                                                                            `o                       /.                                             
                                                                            :-                       /.                                             
                                                                           `+                        ./                                             
                                                                           .:                        `+                                             
                                                                           `+    `.`           `     .+                                             
                                                                            :-`-:``.-`      `..` `-.`/.                                             
                                                                            `+``o/o.` `- `- ```:+-/ ./                                              
                                                                             :- //Nh/. .:-/ .:hNh--.+`                                              
                                                    `-:::::-`                `+```:+ss::.`:/yoo/.``+`                                               
                                                   `+-`   `.+.              `:+-     ``     `     -:                                                
                                                   /-       .o              +.`./-.            `-:-`                                                
                                                   :/       :+:`           ::  --.-::.` ``. `.::.                                                   
                                                    :/-...-/:`./:--..`     o   o    s.::-..::-`                                                     
                                                     `..-+-`    -+:..-:-.` + `.+:---o````.+-                                                        
                                              `...`      :+      `:/-..-//:+:/:-.` `.--:``-:-.-.                                                    
                                            -/:-.-:/-``.:/. -      .s:...-/-````.-:`  `..-:-  `:-                                                   
                                           .o`     `o/--.  `o      o`     `o`     `/.      -``  -:                                                  
                                    ```    -/       /-      +`     s       o`       +`     ` .:` :-                                                 
                                `-//:::://:-s:`   `:o.``    `.   ``++.`  `:/-`      -/     .- -/  +`                                                
                              `//-`       `-:os+:::----:::.````-/:-.-:::::. ./`     `+      /  +` :/                                                
                             .o.   ``...:.    `:+.       `-::::-`            `+.    `+      `  :` :s                                                
                            `o.  `::----:+/`    `+:                           `/:`   /.      `..``/o                                                
                            :+  `+.       -+`     //                            ./-` `::-..-::-` :./`                                               
                            o.  :/         -o`     /+                             -/.    `    `  /..:                                               
                            y   +.          :+      //                             `::        /. :-`/                                               
                            y   +.           //      o-                              +.       `o``+`/`                                              
                            s`  /:            +/     .o                              -/        .+ .+./`                                             
                            +-  .o             /+`    s.                             -:         -- .+.+`                                            
                            -+   +-             -o:   s`                        ./::-:` .`       `  `/:o`                                           
                             o`  `o.              -///-                      `:/-        ``       ````-/o:                                          
                             .o   `o`                                      `//`              .:-::::::/++s+                                         
                              :/   `+-                                    -+`                 -:        :+:+-                                       
                               //    :+`                                 :/`                   +         `o-:+`                                     
                                :+`   `//`                              :/                     o          `s`-o`                                    
                                 -+`    .//-                           -+                     .o           o. -+                                    
                                  `+-     `-/:-.                     `-s                      +-           o.  /:                                   
                                   `//`      `.-:::---.....-------::::s.                     .o           `s   `s                                   
                                     .+:`         ````......``````   :/                     `o.           //    s`                                  
                                       -/:`                         `o`                     +-           .o`    s`                                  
                                         ./:`                       -/                    `+-           `o.     s`                                  
                                           .:/-`                    +.                   `+-           `o-      s                                   
                                             `-/:.`                 o`                  .+-           -+.      `o                                   
                                                `-/:-.`             o`                `//`          ./:`       :-                                   
                                                   `.-:::-.``       :`              `:/.          .//.        ./                                    
                                                        `.--::::-.-:+`            .:/.         `-/:.        .::`                                    
                                                              `.://:`          `.//.        `-:/-`       .-/-`                                      
                                                              -/-`          `-/+:.````...-:/s:.      `.-/-.                                         
                                                             `o         .::::-:---------..` o       `+-`                                            
                                                              o`      `-:-`                 ::      .+                                              
                                                              o`     ./.                     +`     +.                                              
                                                             `o     .o`                      +.     +                                               
                                                             ::     o.                      `o`     /`                                              
                                                            `o`    :+                      `+-      `+-                                             
                                                            :/     y`                    ./o/-`      `:/.                                           
                                                           `o`     h/-                  -+. `-s`       `//.`                                        
                                                          `o.      y`o`                 o`    o.         `:/:`                                      
                                                          /:       s.o.                 -o.``:s.`           .:/:.`       ````                       
                                                         :/        :o-                   `///-`-:/:.         ...:///::::/::://`                     
                                                        :/         `o.`..``                       .:+.        .-:/::/++-`    .+:                    
                                                       -+  `://`    `/:..::/-                       `+:`               -+-    `s                    
                                                      -o      -+            //                        -//:.```         `/o-:--:.                    
                                                      /:     `/o-:::::::`   `s                           `-:::::::::--:-`                           
                                                       :/::://-        `:////-                      ''')
                    time.sleep (3)
                    z = True
                    while z == True:
                        q = input('Would you like to choose Mewtwo? (y/n)\n')
                        if q in yes:
                            #Copies Mewtwo from pokemon to team
                            team.update({key: pokemon[key] for key in pokemon.keys() & {'Mewtwo'}})
                            #sets level to 100
                            team['Mewtwo']['exp'] = 1000000
                            team['Mewtwo']['level'] = bisect.bisect(levels, int(team['Mewtwo']['exp']))
                            #updates stats to level 100
                            team['Mewtwo']['hp'] = math.floor((((team['Mewtwo']['hp'] *2) *team['Mewtwo']['level']) /100) +team['Mewtwo']['level'] +10)
                            team['Mewtwo']['attack'] = math.floor((((team['Mewtwo']['attack'] *2) *team['Mewtwo']['level']) /100) +5)
                            team['Mewtwo']['defense'] = math.floor((((team['Mewtwo']['defense'] *2) *team['Mewtwo']['level']) /100) +5)
                            team['Mewtwo']['special'] = math.floor((((team['Mewtwo']['special'] *2) *team['Mewtwo']['level']) /100) +5)
                            team['Mewtwo']['speed'] = math.floor((((team['Mewtwo']['speed'] *2) *team['Mewtwo']['level']) /100) +5)
                            y = False
                            z = False
                            break
                        elif q in no:
                            y = False
                            z = False
                            break
                        else:
                            print ('Please Give a proper answer!')
                else:
                    print ('Please give a proper answer!')
            except ValueError:
                print ('Please give an proper answer!')
                y = False

#Adjusts starter level to 5
def adjust():
    #sets exp to level 5 value
    pstart['exp'] = 125
    #sets level to 5 based on exp value
    pstart['level'] = bisect.bisect(levels, int(pstart['exp']))
    #updates stats of start acording to level
    pstart['hp'] = math.floor((((pstart['hp'] *2) *pstart['level']) /100) +pstart['level'] +10)
    pstart['attack'] = math.floor((((pstart['attack'] *2) *pstart['level']) /100) +5)
    pstart['defense'] = math.floor((((pstart['defense'] *2) *pstart['level']) /100) +5)
    pstart['special'] = math.floor((((pstart['special'] *2) *pstart['level']) /100) +5)
    pstart['speed'] = math.floor((((pstart['speed'] *2) *pstart['level']) /100) +5)

#Save Function - Saves to save.dat
def save():
    save = True
    while save == True:
        try:
            with open('save.dat', 'wb') as i:
                pickle.dump([list(team), name, list(pc), location, badges], i)
            save = False
        except FileNotFoundError:
            open ('save.dat', 'x')
        except NameError:
            with open('save.dat', 'wb') as i:
                pickle.dump([team, pc, location, badges], i)
            save = False
        #Loading Dots
        for _ in range (1):
            for _ in range (3):
                #Prints "..."
                sys.stdout.write(".")
                sys.stdout.flush()
                time.sleep(.75)
            #Deletes "..."
            sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
            sys.stdout.flush()
        print ('Game Saved!')
        time.sleep(1)

#Pokemon around town
pallet_town = ['Pidgey', 'Rattata', 'Pikachu']
viridian_city = ['Pidgey', 'Rattata', 'Pikachu', 'Caterpie', 'Weedle', 'Nidoran (M)', 'Nidoran (F)', 
    'Diglett', 'Dugtrio', 'Metapod', 'Kakuna', 'Pidgeotto', 'Spearow', 'Mankey', 'Magikarp', 'Poliwag', 'Goldeen', 'Poliwhirl']
pewter_city = ['Pidgey', 'Rattata', 'Caterpie', 'Weedle', 'Nidoran (M)', 'Nidoran (F)', 'Diglett', 'Dugtrio', 'Metapod',
    'Kakuna', 'Pikachu', 'Pidgeotto', 'Spearow', 'Sandshrew', 'Jigglypuff', 'Mankey', 'Clefairy', 'Zubat', 'Paras', 'Geodude']
cerulean_city = ['Magikar', 'Poliwag', 'Goldeen', 'Psyduck', 'Krabby', 'Seaking', 'Bulbasaur', 'Rattata', 'Spearow', 'Ekans',
    'Sandshrew', 'Mankey', 'Caterpie', 'Metapod', 'Weedle', 'Kakuna', 'Pidgey', 'Pidgeotto', 'Oddish', 'Venonat', 'Abra',
    'Bellsprout', 'Charmander', 'Kingler', 'Raticate', 'Fearow', 'Nidoran (M)', 'Nidoran (F)', 'Nidorina', 'Nidorino', 'Zubat',
    'Geodude', 'Machop', 'Onix', 'Jigglypuff', 'Meowth']
vermillion_city = ['Squirtle', 'Magikarp', 'Poliwag', 'Goldeen', 'Tentacool', 'Shellder', 'Krabby', 'Horsea', 'Staryu',
    'Pidgey', 'Pidgeotto', 'Rattata', 'Jigglypuff', 'Oddish', 'Meowth', 'Mankey', 'Abra', 'Bellsprout', 'Psyduck', 'Golduck',
    'Raticate', 'Spearow', 'Ekans', 'Sandshrew', 'Drowzee']
lavender_town = ['Gastly', 'Haunter', 'Cubone', 'Rattata', 'Raticate', 'Spearow', 'Ekans', 'Sandshrew', 'Nidoran (M)',
    'Nidoran (F)', 'Machop', 'Magnemite', 'Voltorb', 'Magikarp', 'Poliwag', 'Goldeen', 'Poliwhirl', 'Slowpoke', 'Krabby',
    'Kingler', 'Horsea', 'Zubat', 'Geodude', 'Onix', 'Pikachu', 'Raichu','Magneton', 'Grimer', 'Muk', 'Electabuzz',
    'Electrode', 'Zapdos', 'Pidgey', 'Pidgeotto', 'Vulpix', 'Jigglypuff', 'Meowth', 'Mankey', 'Growlithe', 'Abra', 'Kadabra',
    'Snorlax']
celadon_city = ['Magikarp', 'Poliwag', 'Goldeen', 'Poliwhirl', 'Slowpoke', 'Pidgey', 'Pidgeotto', 'Rattata',
    'Vulpix', 'Jigglypuff', 'Oddish', 'Meowth', 'Mankey', 'Growlithe', 'Abra', 'Bellsprout', 'Raticate', 'Spearow', 'Fearow',
    'Doduo', 'Snorlax', 'Ponyta', 'Dodrio', 'Tentacool', 'Shellder', 'Krabby']
saffron_city = ['Pidgey', 'Pidgeotto', 'Rattata', 'Vulpix', 'Jigglypuff', 'Oddish', 'Meowth', 'Mankey', 'Growlithe', 'Abra',
    'Bellsprout', 'Ekans', 'Sandshrew', 'Kadabra', 'Hitmonchan', 'Hitmonlee']
fuchsia_city = ['Magikarp', 'Poliwag', 'Goldeen', 'Krabby', 'Seaking', 'Gyarados', 'Pidgey', 'Pidgeotto', 'Oddish',
    'Gloom', 'Venonat', 'Venomoth', 'Bellsprout', 'Weepinbell', "Farfetch'd", 'Ditto', 'Slowpoke', 'Slowbro', 'Tentacool', 
    'Tentacruel', 'Horsea', 'Seadra', 'Rattata', 'Raticate', 'Spearow', 'Fearow', 'Doduo', 'Staryu', 'Nidoran (M)',
    'Nidoran (F)', 'Nidorina', 'Nidorino', 'Paras', 'Parasect', 'Exeggcute', 'Rhyhorn', 'Chansey', 'Tangela', 'Scyther',
    'Pinsir', 'Psyduck', 'Dratini', 'Dragonair', 'Cubone', 'Marowak', 'Kangaskhan', 'Touros']
cinnabar_island = ['Magikarp', 'Poliwag', 'Goldeen', 'Tentacool', 'Shellder', 'Horsea', 'Staryu', 'Pidgey', 'Pidgeotto',
    'Rattata', 'Raticate', 'Tangela', 'Tentacruel', 'Zubat', 'Golbat', 'Psyduck', 'Golduck', 'Slowpoke',
    'Slwobro', 'Seel', 'Krabby', 'Dewgong', 'Kingler', 'Seadra', 'Articuno']
indigo_plateau = ['Spearow', 'Fearow', 'Ekans', 'Arbok', 'Sandshrew', 'Sandslash', 'Nidorina', 'Nidorino', 'Mankey',
    'Primeape', 'Ditto', 'Magikarp', 'Poliwag', 'Goldeen', 'Poliwhirl', 'Slowbro', 'Kingler', 'Seadra', 'Seaking', 'Zubat',
    'Golbat', 'Machop', 'Machoke', 'Geodude', 'Graveler', 'Onix', 'Marowak', 'Moltres', 'Venomoth']

#Gym Leader Teams
#Pewter City
brock = ['Geodude', 'Onix']
#Cerulean City
misty = ['Staryu', 'Starmie']
#Vermilion City
lt_surge = ['Raichu']
#Celadon City
erika = ['Tangela', 'Weepinbell', 'Gloom']
#Fuchsia City
koga = ['Venonat', 'Venonat', 'Venonat', 'Venomoth']
#Saffron City
sabrina = ['Abra', 'Kadabra', 'Alakazam']
#Cinnabar Island
blaine = ['Ninetales', 'Rapidash', 'Arcanine']
#Viridian City
giovanni = ['Dugtrio', 'Persian', 'Nidoqueen', 'Nidoking', 'Rhydon']
#Elite 4
#1
Lorelei = ['Dewgong', 'Cloyster', 'Slowbrow', 'Jynx', 'Lapras']
#2
bruno = ['Onix', 'Hitmonchan', 'Hitmonlee', 'Onix', 'Machamp']
#3
agatha = ['Gengar', 'Golbat', 'Haunter', 'Arbok', 'Gengar']
#4
lance = ['Gyarados', 'Dragonair', 'Dragonair', 'Aerodactyl', 'Dragonite']
#Champ
blue = ['Sandslash', 'Alakazam', 'Exeggutor', 'Ninetales', 'Magneton', 'Vaporeon']
#Moves
b_sandslash = ['Earthquake', 'Slash', 'Poison Sting', 'Fury Swipes']


#Determinaning location for battles
def battlelocation():
    while True:
        #Checks what town your in
        if 'Pewter City' in location:
            #Seeing if you have the badge or not
            if len(badges) == 0:
                b = input('''Would you like to look for wild Pokémon (1), battle the gym leader (2), or 
                    return to the navigation (3)?\n''')
                if b == '1':
                    print(random.choice(pewter_city))
                elif b == '2':
                    print ('Gym battle')
                elif b == '3':
                    break
                else:
                    print ('Please give a real response!')
            else:
                b = input('Would you like to look for wild Pokémon? (y/n)\n')
                if b in yes:
                    print(random.choice(pewter_city))
                elif b in no:
                    nav()
                else:
                    print('Please give a proper answer!')

        elif 'Cerulean City' in location:
            #Seeing if you have the badge or not
            if len(badges) == 1:
                b = input('''Would you like to look for wild Pokémon (1), battle the gym leader (2), or 
                    return to the navigation (3)?\n''')
                if b == '1':
                    print(random.choice(cerulean_city))
                elif b == '2':
                    print ('Gym battle')
                elif b == '3':
                    break
                else:
                    print ('Please give a real response!')
            else:
                b = input('Would you like to look for wild Pokémon? (y/n)\n')
                if b in yes:
                    print(random.choice(cerulean_city))
                elif b in no:
                    nav()
                else:
                    print('Please give a proper answer!')

        elif 'Vermilion City' in location:
            #See if you have the Badge or not
            if len(badges) == 2:
                b = input('''Would you like to look for wild Pokémon (1), battle the gym leader (2), or 
                    return to the navigation (3)?\n''')
                if b == '1':
                    print(random.choice(vermillion_city))
                elif b == '2':
                    print ('Gym battle')
                elif b == '3':
                    break
                else:
                    print ('Please give a real response!')
            else:
                b = input('Would you like to look for wild Pokémon? (y/n)\n')
                if b in yes:
                    print(random.choice(vermillion_city))
                elif b in no:
                    nav()
                else:
                    print('Please give a proper answer!')

        elif 'Celadon City' in location:
            #See if you have the Badge or not
            if len(badges) == 3:
                b = input('''Would you like to look for wild Pokémon (1), battle the gym leader (2), or 
                    return to the navigation (3)?\n''')
                if b == '1':
                    print(random.choice(celadon_city))
                elif b == '2':
                    print ('Gym battle')
                elif b == '3':
                    break
                else:
                    print ('Please give a real response!')
            else:
                b = input('Would you like to look for wild Pokémon? (y/n)\n')
                if b in yes:
                    print(random.choice(celadon_city))
                elif b in no:
                    nav()
                else:
                    print('Please give a proper answer!')

        elif 'Fuchsia City' in location:
            #See if you have the badge or not
            if len(badges) == 4:
                b = input('''Would you like to look for wild Pokémon (1), battle the gym leader (2), or 
                    return to the navigation (3)?\n''')
                if b == '1':
                    print(random.choice(fuchsia_city))
                elif b == '2':
                    print ('Gym battle')
                elif b == '3':
                    break
                else:
                    print ('Please give a real response!')
            else:
                b = input('Would you like to look for wild Pokémon? (y/n)\n')
                if b in yes:
                    print(random.choice(fuchsia_city))
                elif b in no:
                    nav()
                else:
                    print('Please give a proper answer!')

        elif  'Saffron City' in location:
            #See if you have the badge or not
            if len(badges) == 5:
                b = input('''Would you like to look for wild Pokémon (1), battle the gym leader (2), or 
                    return to the navigation (3)?\n''')
                if b == '1':
                    print(random.choice(saffron_city))
                elif b == '2':
                    print ('Gym battle')
                elif b == '3':
                    break
                else:
                    print ('Please give a real response!')
            else:
                b = input('Would you like to look for wild Pokémon? (y/n)\n')
                if b in yes:
                    print(random.choice(saffron_city))
                elif b in no:
                    nav()
                else:
                    print('Please give a proper answer!')

        elif 'Cinnabar Island' in location:
            #See if you have the badge
            if len(badges) == 6:
                b = input('''Would you like to look for wild Pokémon (1), battle the gym leader (2), or 
                    return to the navigation (3)?\n''')
                if b == '1':
                    print(random.choice(cinnabar_island))
                elif b == '2':
                    print ('Gym battle')
                elif b == '3':
                    break
                else:
                    print ('Please give a real response!')
            else:
                b = input('Would you like to look for wild Pokémon? (y/n)\n')
                if b in yes:
                    print(random.choice(cinnabar_island))
                elif b in no:
                    nav()
                else:
                    print('Please give a proper answer!')

        elif 'Pallet Town' in location:
            b = input('Would you like to look for wild Pokémon? (y/n)\n')
            if b in yes:
                print(random.choice(pallet_town))
            elif b in no:
                nav()
            else:
                print('Please give a proper answer!')

        elif 'Lavender Town' in location:
            b = input('Would you like to look for wild Pokémon? (y/n)\n')
            if b in yes:
                print(random.choice(lavender_town))
            elif b in no:
                nav()
            else:
                print('Please give a proper answer!')

        elif 'Viridian City' in location:
            if len(badges) == 7:
                b = input('''Would you like to look for wild Pokémon (1), battle the gym leader (2), or 
                return to the navigation (3)?\n''')
                if b == '1':
                    print (random.choice(viridian_city))
                elif b == '2':
                    print ('Gym battle')
                elif b == '3':
                    break
                else:
                    print ('Please give a real response!')
            else:
                b = input('Would you like to look for wild Pokémon? (y/n)\n')
                if b in yes:
                    print (random.choice(viridian_city))
                elif b in no:
                    nav()
                else:
                    print('Please give a proper answer!')

        elif 'Indigo Plateau' in location:
            b = input('''Would you like to look for wild Pokémon (1), challenge the Elite Four (2), or 
                return to navigarion (3)?\n''')
            if b == '1':
                print(random.choice(indigo_plateau))
            elif b == '2':
                print ('Challenges Elite Four')
            elif b == '3':
                break
            else:
                print ('Please give a real answer!')
            
        else:
            while True:
                print ('ERROR! Location not specified!')
                time.sleep(1)
                b = input('Would you like to delete entire save to repair corrupted location? (y/n)\n' +
                    'Warning: You will loose all progress currently made!')
                if b in yes:
                    #deletes save.dat
                    os.remove('save.dat')
                    print ('Save.dat deleted!')
                    b = input ('Would you like to restart game?')
                    while True:
                        if b in yes:
                            print ('Restarting!')
                            #Loading Dots
                            for _ in range (1):
                                for _ in range (3):
                                    #Prints "..."
                                    sys.stdout.write(".")
                                    sys.stdout.flush()
                                    time.sleep(.75)
                                #Deletes "..."
                                sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                                sys.stdout.flush()
                            os.execl(sys.executable, sys.executable, * sys.argv)
                        elif b in no:
                            sys.exit()
                        else:
                            print ('Please give a proper answer!')
                elif b in no:
                    sys.exit()
                else:
                    print ('Please give a proper answer!')
    
#Battleing Wild pokemon
#def battlewild():

#Team Function
def teamf():
    print (list(team))
    time.sleep(1)
    nav()

#PC Function
def pcf():
    print ('Team:')
    print (list(team))
    time.sleep(1)
    print ('PC:')
    print (list(pc))
    time.sleep(1)
    nav()

#Traveling fuction - based on badges
def travel():
    print ('Current location: ' + str(location))
    while True:
        if len(badges) == 0:
            print ('Where would you like to travel to?\n' +
                '   1. Pallet Town\n' +
                '   2. Viridian City\n' +
                '   3. Pewter City\n')
            l = input()
            if l == '1':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()                
                location.append('Pallet Town')
                print ('You have traveled to Pallet Town!\n' +
                    'Shades of your journey await!')
                time.sleep(2)
                break
            elif l == '2':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Viridian City')
                print ('You have traveled to Viridian City!\n' +
                    'The Eternally Green Paradise')
                time.sleep(2)
                break
            elif l == '3':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Pewter City')
                print ('You have traveled to Pewter City!\n' +
                    'A Stone Gray City')
                time.sleep(2)
                break
            else:
                print ('Please give a proper answer!')
        elif len(badges) == 1:
            print ('Where would you like to travel to?\n' +
                '   1. Pallet Town\n' +
                '   2. Viridian City\n' +
                '   3. Pewter City\n' +
                '   4. Cerulean City\n')
            l = input()
            if l == '1':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()                
                location.clear()
                location.append('Pallet Town')
                print ('You have traveled to Pallet Town!\n' +
                    'Shades of your journey await!')
                time.sleep(2)
                break
            elif l == '2':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Viridian City')
                print ('You have traveled to Viridian City!\n' +
                    'The Eternally Green Paradise')
                time.sleep(2)
                break
            elif l == '3':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Pewter City')
                print ('You have traveled to Pewter City!\n' +
                    'A Stone Gray City')
                time.sleep(2)
                break
            elif l == '4':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Cerulean City')
                print ('You have traveled to Cerulean City!\n' +
                    'A Mysterious, Blue Aura Surrounds It')
                time.sleep(2)
                break
            else:
                print ('Please give a proper answer!')
        elif len(badges) == 2:
            print ('Where would you like to travel to?\n' +
                '   1. Pallet Town\n' +
                '   2. Viridian City\n' +
                '   3. Pewter City\n' +
                '   4. Cerulean City\n' +
                '   5. Vermillion City\n' +
                '   6. Lavender Town\n')
            l = input()
            if l == '1':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()                
                location.clear()
                location.append('Pallet Town')
                print ('You have traveled to Pallet Town!\n' +
                    'Shades of your journey await!')
                time.sleep(2)
                break
            elif l == '2':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Viridian City')
                print ('You have traveled to Viridian City!\n' +
                    'The Eternally Green Paradise')
                time.sleep(2)
                break
            elif l == '3':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Pewter City')
                print ('You have traveled to Pewter City!\n' +
                    'A Stone Gray City')
                time.sleep(2)
                break
            elif l == '4':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Cerulean City')
                print ('You have traveled to Cerulean City!\n' +
                    'A Mysterious, Blue Aura Surrounds It')
                time.sleep(2)
                break
            elif l == '5':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Vermillion City')
                print ('You have traveled to Vermillion City!\n' +
                    'The Port of Exquisite Sunsets')
                time.sleep(2)
                break
            elif l == '6':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Lavender Town')
                print ('You have traveled to Lavender Town!\n' +
                    'The Noble Purple Town')
                time.sleep(2)
                break
            else:
                print ('Please give a proper answer!')
        elif len(badges) == 3:
            print ('Where would you like to travel to?\n' +
                '   1. Pallet Town\n' +
                '   2. Viridian City\n' +
                '   3. Pewter City\n' +
                '   4. Cerulean City\n' +
                '   5. Vermillion City\n' +
                '   6. Lavender Town\n' +
                '   7. Celadon City\n')
            l = input()
            if l == '1':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()                
                location.clear()
                location.append('Pallet Town')
                print ('You have traveled to Pallet Town!\n' +
                    'Shades of your journey await!')
                time.sleep(2)
                break
            elif l == '2':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Viridian City')
                print ('You have traveled to Viridian City!\n' +
                    'The Eternally Green Paradise')
                time.sleep(2)
                break
            elif l == '3':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Pewter City')
                print ('You have traveled to Pewter City!\n' +
                    'A Stone Gray City')
                time.sleep(2)
                break
            elif l == '4':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Cerulean City')
                print ('You have traveled to Cerulean City!\n' +
                    'A Mysterious, Blue Aura Surrounds It')
                time.sleep(2)
                break
            elif l == '5':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Vermillion City')
                print ('You have traveled to Vermillion City!\n' +
                    'The Port of Exquisite Sunsets')
                time.sleep(2)
                break
            elif l == '6':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Lavender Town')
                print ('You have traveled to Lavender Town!\n' +
                    'The Noble Purple Town')
                time.sleep(2)
                break
            elif l == '7':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Celadon City')
                print ('You have traveled to Celadon City!\n' +
                    'The City of Rainbow Dreams')
                time.sleep(2)
                break
            else:
                print ('Please give a proper answer!')
        elif len(badges) == 4:
            print ('Where would you like to travel to?\n' +
                '   1. Pallet Town\n' +
                '   2. Viridian City\n' +
                '   3. Pewter City\n' +
                '   4. Cerulean City\n' +
                '   5. Vermillion City\n' +
                '   6. Lavender Town\n' +
                '   7. Celadon City\n' +
                '   8. Fuchsia City\n')
            l = input()
            if l == '1':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()                
                location.clear()
                location.append('Pallet Town')
                print ('You have traveled to Pallet Town!\n' +
                    'Shades of your journey await!')
                time.sleep(2)
                break
            elif l == '2':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Viridian City')
                print ('You have traveled to Viridian City!\n' +
                    'The Eternally Green Paradise')
                time.sleep(2)
                break
            elif l == '3':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Pewter City')
                print ('You have traveled to Pewter City!\n' +
                    'A Stone Gray City')
                time.sleep(2)
                break
            elif l == '4':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                
                location.clear()
                location.append('Cerulean City')
                print ('You have traveled to Cerulean City!\n' +
                    'A Mysterious, Blue Aura Surrounds It')
                time.sleep(2)
                break
            elif l == '5':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                
                location.clear()
                location.append('Vermillion City')
                print ('You have traveled to Vermillion City!\n' +
                    'The Port of Exquisite Sunsets')
                time.sleep(2)
                break
            elif l == '6':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                
                location.clear()
                location.append('Lavender Town')
                print ('You have traveled to Lavender Town!\n' +
                    'The Noble Purple Town')
                time.sleep(2)
                break
            elif l == '7':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Celadon City')
                print ('You have traveled to Celadon City!\n' +
                    'The City of Rainbow Dreams')
                time.sleep(2)
                break
            elif l == '8':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                
                location.clear()
                location.append('Fuchsia City')
                print ('You have traveled to Fuchsia City!\n' +
                    "Behold! It's Passion Pink!")
                time.sleep(2)
                break
            else:
                print ('Please give a proper answer!')
        elif len(badges) == 5:
            print ('Where would you like to travel to?\n' +
                '   1. Pallet Town\n' +
                '   2. Viridian City\n' +
                '   3. Pewter City\n' +
                '   4. Cerulean City\n' +
                '   5. Vermillion City\n' +
                '   6. Lavender Town\n' +
                '   7. Celadon City\n' +
                '   8. Fuchsia City\n' +
                '   9. Saffron City\n')
            l = input()
            if l == '1':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()                
                
                location.clear()
                location.append('Pallet Town')
                print ('You have traveled to Pallet Town!\n' +
                    'Shades of your journey await!')
                time.sleep(2)
                break
            elif l == '2':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                
                location.clear()
                location.append('Viridian City')
                print ('You have traveled to Viridian City!\n' +
                    'The Eternally Green Paradise')
                time.sleep(2)
                break
            elif l == '3':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Pewter City')
                print ('You have traveled to Pewter City!\n' +
                    'A Stone Gray City')
                time.sleep(2)
                break
            elif l == '4':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Cerulean City')
                print ('You have traveled to Cerulean City!\n' +
                    'A Mysterious, Blue Aura Surrounds It')
                time.sleep(2)
                break
            elif l == '5':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Vermillion City')
                print ('You have traveled to Vermillion City!\n' +
                    'The Port of Exquisite Sunsets')
                time.sleep(2)
                break
            elif l == '6':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                
                location.clear()
                location.append('Lavender Town')
                print ('You have traveled to Lavender Town!\n' +
                    'The Noble Purple Town')
                time.sleep(2)
                break
            elif l == '7':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                
                location.clear()
                location.append('Celadon City')
                print ('You have traveled to Celadon City!\n' +
                    'The City of Rainbow Dreams')
                time.sleep(2)
                break
            elif l == '8':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Fuchsia City')
                print ('You have traveled to Fuchsia City!\n' +
                    "Behold! It's Passion Pink!")
                time.sleep(2)
                break
            elif l == '9':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                
                location.clear()
                location.append('Saffron City')
                print ('You have traveled to Saffron City!\n' +
                    'Shining, Golden Land of Commerce')
                time.sleep(2)
                break
            else:
                print ('Please give a proper answer!')
        elif len(badges) == 6 or 7:
            print ('Where would you like to travel to?\n' +
                '   1. Pallet Town\n' +
                '   2. Viridian City\n' +
                '   3. Pewter City\n' +
                '   4. Cerulean City\n' +
                '   5. Vermillion City\n' +
                '   6. Lavender Town\n' +
                '   7. Celadon City\n' +
                '   8. Fuchsia City\n' +
                '   9. Saffron City\n' +
                '   10. Cinnabar Island\n')
            l = input()
            if l == '1':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()                
                
                location.clear()
                location.append('Pallet Town')
                print ('You have traveled to Pallet Town!\n' +
                    'Shades of your journey await!')
                time.sleep(2)
                break
            elif l == '2':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Viridian City')
                print ('You have traveled to Viridian City!\n' +
                    'The Eternally Green Paradise')
                time.sleep(2)
                break
            elif l == '3':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Pewter City')
                print ('You have traveled to Pewter City!\n' +
                    'A Stone Gray City')
                time.sleep(2)
                break
            elif l == '4':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Cerulean City')
                print ('You have traveled to Cerulean City!\n' +
                    'A Mysterious, Blue Aura Surrounds It')
                time.sleep(2)
                break
            elif l == '5':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Vermillion City')
                print ('You have traveled to Vermillion City!\n' +
                    'The Port of Exquisite Sunsets')
                time.sleep(2)
                break
            elif l == '6':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Lavender Town')
                print ('You have traveled to Lavender Town!\n' +
                    'The Noble Purple Town')
                time.sleep(2)
                break
            elif l == '7':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Celadon City')
                print ('You have traveled to Celadon City!\n' +
                    'The City of Rainbow Dreams')
                time.sleep(2)
                break
            elif l == '8':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Fuchsia City')
                print ('You have traveled to Fuchsia City!\n' +
                    "Behold! It's Passion Pink!")
                time.sleep(2)
                break
            elif l == '9':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Saffron City')
                print ('You have traveled to Saffron City!\n' +
                    'Shining, Golden Land of Commerce')
                time.sleep(2)
                break
            elif l == '10':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Cinnabar Island')
                print ('You have traveled to Cinnabar Island!\n' +
                    'The Fiery Town of Burning Desire')
                time.sleep(2)
                break
            else:
                print ('Please give a proper answer!')
        elif len(badges) == 8:
            print ('Where would you like to travel to?\n' +
                '   1. Pallet Town\n' +
                '   2. Viridian City\n' +
                '   3. Pewter City\n' +
                '   4. Cerulean City\n' +
                '   5. Vermillion City\n' +
                '   6. Lavender Town\n' +
                '   7. Celadon City\n' +
                '   8. Fuchsia City\n' +
                '   9. Saffron City\n' +
                '   10. Cinnabar Island\n' +
                '   11. Indigo Plateau')
            l = input()
            if l == '1':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()                
                location.clear()
                location.append('Pallet Town')
                print ('You have traveled to Pallet Town!\n' +
                    'Shades of your journey await!')
                time.sleep(2)
                break
            elif l == '2':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Viridian City')
                print ('You have traveled to Viridian City!\n' +
                    'The Eternally Green Paradise')
                time.sleep(2)
                break
            elif l == '3':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Pewter City')
                print ('You have traveled to Pewter City!\n' +
                    'A Stone Gray City')
                time.sleep(2)
                break
            elif l == '4':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Cerulean City')
                print ('You have traveled to Cerulean City!\n' +
                    'A Mysterious, Blue Aura Surrounds It')
                time.sleep(2)
                break
            elif l == '5':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Vermillion City')
                print ('You have traveled to Vermillion City!\n' +
                    'The Port of Exquisite Sunsets')
                time.sleep(2)
                break
            elif l == '6':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Lavender Town')
                print ('You have traveled to Lavender Town!\n' +
                    'The Noble Purple Town')
                time.sleep(2)
                break
            elif l == '7':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Celadon City')
                print ('You have traveled to Celadon City!\n' +
                    'The City of Rainbow Dreams')
                time.sleep(2)
                break
            elif l == '8':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Fuchsia City')
                print ('You have traveled to Fuchsia City!\n' +
                    "Behold! It's Passion Pink!")
                time.sleep(2)
                break
            elif l == '9':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Saffron City')
                print ('You have traveled to Saffron City!\n' +
                    'Shining, Golden Land of Commerce')
                time.sleep(2)
                break
            elif l == '10':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Cinnabar Island')
                print ('You have traveled to Cinnabar Island!\n' +
                    'The Fiery Town of Burning Desire')
                time.sleep(2)
                break
            elif l == '11':
                #Loading Dots
                for _ in range (2):
                    for _ in range (3):
                        #Prints "..."
                        sys.stdout.write(".")
                        sys.stdout.flush()
                        time.sleep(.75)
                    #Deletes "..."
                    sys.stdout.write('\b'*3 + ' '*3 + '\b'*3)
                    sys.stdout.flush()
                location.clear()
                location.append('Indigo Plateau')
                print ('You have traveled to Indigo Plateau!\n' +
                    'The ultimate goal of Trainers!')
                time.sleep(2)
                break
            else:
                print ('Please give a proper answer!')

#Navigation
def nav():
    while True:
        print ('\nWhat would you like to do?')
        q = input ( '   1 - Battle\n' +
                    '   2 - Team\n' +
                    '   3 - PC\n' +
                    '   4 - Travel\n' +
                    '   5 - Badges\n' +
                    '   6 - Save\n' +
                    '   7 - Quit\n')
        if q == '1':
            battlelocation()
        elif q == '2':
            teamf()
        elif q == '3':
            pcf()
        elif q == '4':
            travel()
        elif q == '5':
            print('\n' + name)
            print(badges)
        elif q == '6':
            save()
        elif q == '7':
            sys.exit()
        elif q == '42':
            badges.clear()
            a = input('Badge Amount:\n')
            for _ in range(0,int(a)):
                b = input('Badge Name:\n')
                badges.append(b)
        else:
            print ('Please give a proper answer!\n')


#Game Start
#Load save
try:
    #Check for save and load it
    with open('save.dat', 'rb') as i:
            team, name, pc, location, badges = pickle.load(i)
    #Starts Game
    nav()
#If no save, but has save.dat - starts tutorial
except EOFError:
    title()
    intro()
    nav()
    #For troubleshooting only!
#    starter()
#    nav()
#No save.dat - creates save.dat and starts tutorial
except FileNotFoundError:
    open ('save.dat', 'x')
    title()
    intro()
    nav()
    #For troubleshoooting only!
#    starter()
#An error I ran into once and couldn't replicate.
#In the off chance it happens again, the fix was to delete the save.dat and let the script recreate it.
except pickle.UnpicklingError:
    #deletes save.dat
    print ('Error! Resolving issue!')
    os.remove('save.dat')
    #restarts script
    print ('Issues Resolved! Restarting...')
    os.execl(sys.executable, sys.executable, * sys.argv)

"""
Left to add:
Finding wild pokemon
Capturing
Gyms
Battling
Dual-Typeing

Maybe PyGame
"""