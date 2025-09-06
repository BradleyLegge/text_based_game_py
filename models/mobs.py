from models.player import Person

class Goblin(Person):
    def __init__(self, name="Goblin", health = 10, base_attack = 2, ac = 10):
        super().__init__(name, health, base_attack, ac)

class Kobald(Person):
    def __init__(self, name="Kobald", health = 15, base_attack = 3, ac = 14):
        super().__init__(name, health, base_attack, ac)

class Orc(Person):
    def __init__(self, name="Orc", health = 20, base_attack = 4, ac = 18):
        super().__init__(name, health, base_attack, ac)