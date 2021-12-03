from Pokemons import *
from Humans import *
from Teams import *
from Arenas import *

voda = WaterPokemon('voda', 10, 100, 6, 'Ж', 1)
fire = FirePokemon('ogonek', 9, 100, 5, 'М', 1)
falt = FaltPokemon('faltec', 23, 100, 11, 'М', 1)
s1 = Spectator('vadim', 11, 11, 11, 'M', 11)
s2 = Spectator('max', 22, 22, 22, 'M', 11)
d1 = Doctor('Kolya', 34, 40, 2, 'M', 80)
d2 = Doctor('olga', 22, 222, 2, 'Ж', 33)
m2 = Master('niko', 33, 43, 2, 'M', 99)
m1 = Master('volodya', 14, 26, 4, 'M', 85)
m3 = Master('fdfd', 33, 22, 3, 'M', 33)
m1.catch_pokemon(voda)
m2.catch_pokemon(fire)

t1 = Team('noobs', m1, d1, s1)
t2 = Team('boobs', [m2, m3], d2, s2)
a = FireArena([t1, t2])
t1.chose_master(m1, voda)
t1.chose_doctor(d1)
t2.chose_master(m2, fire)
t2.chose_doctor(d2)
a.start_battle(t1, t2)
