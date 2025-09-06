from models.player import Person

class Goblin(Person):
    def __init__(self, name="Goblin", health = 10, base_attack = 2, ac = 12):
        super().__init__(name, health, base_attack, ac)