from Animals import Pokemon
from Abilki import Ability

WaterBlast = Ability('WaterBlast', 'Water', 20)
FireBall = Ability('FireBall', 'Fire', 22)
KnowledgeFlow = Ability('KnowledgeFlow', 'Falt', 35)


class WaterPokemon(Pokemon):
    def __init__(self, name, age, health, damage, sex, level, master=None, ability=WaterBlast, element='Water'):
        super().__init__(name, age, health, damage, sex, level, master, ability, element)

    def info(self):
        super().info()
        self.ability = WaterBlast
        self.ability.info_about_ability()


class FirePokemon(Pokemon):
    def __init__(self, name, age, health, damage, sex, level, master=None, ability=FireBall, element='Fire'):
        super().__init__(name, age, health, damage, sex, level, master, ability, element)

    def info(self):
        super().info()
        self.ability = FireBall
        self.ability.info_about_ability()


class FaltPokemon(Pokemon):
    def __init__(self, name, age, health, damage, sex, level, master=None, ability=KnowledgeFlow, element='Falt'):
        super().__init__(name, age, health, damage, sex, level, master, ability, element)

    def info(self):
        super().info()
        self.ability = KnowledgeFlow
        self.ability.info_about_ability()
