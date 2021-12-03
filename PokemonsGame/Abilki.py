class Ability:
    def __init__(self, name, element, damage):
        self.name = name
        self.element = element
        self.damage = damage

    def info_about_ability(self):
        print(f'{self.name} : {self.damage} урона. Только для {self.element} покемонов!')
