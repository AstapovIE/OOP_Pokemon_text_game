class Animal:
    def __init__(self, name, age, health, damage, sex):
        self.name = name
        self.age = age
        self.health = health
        self.damage = damage
        self.sex = sex

    def _help_(self):
        return [method for method in dir(self) if method.startswith('__') is False and callable(getattr(self, method))]

    def info(self):
        print('главная информация : ')
        print(f'name : {self.name};')
        print(f'age : {self.age};')
        print(f'health : {self.health};')
        print(f'damage : {self.damage};')
        print(f'sex : {self.sex};')

    def growing_up(self):
        self.age += 1
        print(f'у {self.name} день рождение теперь ему {self.age}')

    def hit(self, target):
        if type(self) == type(target) or (isinstance(self, Pokemon) and isinstance(target, Pokemon)):
            print(f'{self.name} дает тычку по {target.name}')
            target.health -= self.damage
        else:
            raise ValueError('тычковать можно только свой класс')


class Pokemon(Animal):
    def __init__(self, name, age, health, damage, sex, level, master, ability, element):
        super().__init__(name, age, health, damage, sex)
        self.level = level
        self.master = master
        self.ability = ability
        self.element = element

    def info(self):
        super().info()
        print(f'level : {self.level};')
        print(f'master : {self.master};')
        print(f'element : {self.element};')

    def using_ability(self, target, ability):
        if isinstance(target, Pokemon):
            print(f'{self.name} использует {ability.name} в {target.name}')
            target.health -= ability.damage
        else:
            raise ValueError(f'нельзя применить абилку на {target.name} (шмалять только по покемонам!)')

    def evo(self):
        self.level += 1
        self.health += 2
        self.damage += 1
        print(f'{self.name} получает {self.level} уровень: health - {self.health}; damage - {self.damage}')


class Human(Animal):
    def __init__(self, name, age, health, damage, sex, iq):
        super().__init__(name, age, health, damage, sex)
        self.iq = iq

    def info(self):
        super().info()
        print(f'iq : {self.iq};')

    def support(self, target):
        print(f'{self.name} поддерживает {target.name}')


