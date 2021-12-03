import random


class Arena:
    def __init__(self, teams=None, element=None, ):
        if teams == None:
            teams = []
        self.teams = teams
        self.element = element

    def start_battle(self, team1, team2):
        if team1.PokemonForFight != None and team2.PokemonForFight != None and team1.DoctorForFight != None and team2.DoctorForFight != None:
            print(f'начинается битва между командой {team1.name} и командой {team2.name} на {self.element} арене')
        else:
            raise ValueError('мастера команд и их покемоны не выбраны')
        self.give_bonus(team1)
        self.give_bonus(team2)
        print('-' * 10)
        print('')
        self.draw(team1, team2)

    bonus = {'damage': 0, 'health': 0}

    def give_bonus(self, team):
        if self.element == team.PokemonForFight.element:
            for i in self.bonus:
                if self.bonus[i] != 0:
                    print(f'{team.PokemonForFight.name} получает + {self.bonus[i]} к {i}')
                if i == 'damage':
                    team.PokemonForFight.damage += self.bonus[i]
                elif i == 'health':
                    team.PokemonForFight.health += self.bonus[i]
        else:
            print(f' для команды {team.name} бонуса не положено')

    def add_team(self, team):
        self.teams.append(team)
        print(f'на арену влетает команда {team.name}')

    def draw(self, team1, team2):
        x = random.randint(0, 1)
        if x == 0:
            print(f' команда {team1.name} начинает')
            self.fight(team1, team2)
        else:
            print(f' команда {team2.name} начинает')
            self.fight(team2, team1)

    def attack(self, tm1, tm2):
        action = int(input(f'команда {tm1.name} ,0 - обычная атака, 1 - абилка'))
        if action == 0:
            tm1.PokemonForFight.hit(tm2.PokemonForFight)
        elif action == 1:
            tm1.PokemonForFight.using_ability(tm2.PokemonForFight, tm1.PokemonForFight.ability)
        else:
            print('\033[2;31;40m ---WARNING!!!--- \033[0;0m')
            print(
                'пользователь - рукожоп, попросил же 0 или 1! Так и быть не кину исключение, продолжай сражаться, только ход ты просрал')
        print('-' * 10)
        print(
            f'{tm1.PokemonForFight.health} hp осталось у {tm1.PokemonForFight.name} покемона <-> {tm2.PokemonForFight.health} hp осталось у {tm2.PokemonForFight.name} покемона')
        print('-' * 10)

    def fight(self, tm1, tm2):
        while tm1.PokemonForFight.health > 0 and tm2.PokemonForFight.health > 0:
            self.attack(tm1, tm2)
            if tm2.PokemonForFight.health <= 0:
                break
            self.attack(tm2, tm1)
        self.reabilitation(tm1, tm2)
        if tm1.PokemonForFight.health > 0:
            print(f'команда {tm1.name} победила')
            tm1.PokemonForFight.evo()
        else:
            print(f'команда {tm2.name} победила')

    def reabilitation(self, tm1, tm2):
        print('происходит lechevo after mesivo')
        tm1.doctors.heal_pokemon(tm1.PokemonForFight)
        tm2.doctors.heal_pokemon(tm2.PokemonForFight)
        print('-' * 10)


class WaterArena(Arena):
    def __init__(self, teams=None, element='Water'):
        super().__init__(teams, element)

    bonus = {'damage': 0, 'health': 19}



class FireArena(Arena):
    def __init__(self, teams=None, element='Fire'):
        super().__init__(teams, element)

    bonus = {'damage': 15, 'health': 1}


class FaltArena(Arena):
    def __init__(self, teams=None, element='Falt'):
        super().__init__(teams, element)

    bonus = {'damage': 17, 'health': 0}