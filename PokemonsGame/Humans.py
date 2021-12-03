from Animals import Human


class Spectator(Human):
    pass


class Doctor(Human):
    def heal_pokemon(self, pokemon):
        print(f'{self.name} лечит {pokemon.name}')
        pokemon.health = 100


class Master(Human):
    def __init__(self, name, age, health, damage, sex, iq, score=0, pokemons=None):
        super().__init__(name, age, health, damage, sex, iq)
        self.score = score
        if pokemons == None:
            pokemons = []
        self.pokemons = pokemons

    def info(self):
        super().info()
        print(f'pokemons : {self.pokemons};')
        print(f'score : {self.score};')

    def catch_pokemon(self, pokemon):
        if pokemon.master == None:
            print(f'{self.name} ловит покемона {pokemon.name}')
            self.pokemons.append(pokemon.name)
            pokemon.master = self.name
        else:
            raise ValueError('покемон занят')

    def chose_pokemon(self, pokemon, team):
        if pokemon.name in self.pokemons:
            team.PokemonForFight = pokemon
            print(f'{self.name} выбирает для сражения покемона {pokemon.name}')
        else:
            raise ValueError('покемон не найден')
