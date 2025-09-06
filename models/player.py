class Person():
    def __init__(self, name, health = 10, base_attack = 2, ac = 14):
        self.name = name
        self.health = health
        self.base_attack = base_attack
        self.ac = ac
        self.inventory = []

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} add to your bags.")

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated")
        else:
            print(f"{self.name} has taken {amount} of damage, health is now {self.health}")

    def player_status(self):
        print(f"Player name: {self.name}")
        print(f"{self.name}'s health is: {self.health}")
        print(f"{self.name}'s inventory: {' '.join(self.inventory) if self.inventory else 'empty'}")