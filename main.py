import json
import random
from models.player import Person
from models.mobs import Goblin, Kobald, Orc


def read_file(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

rooms = read_file("rooms.json")
loot = read_file("loot.json")

def game_start():
    print("Welcome to The Game!")
    print("Search through the rooms, collecting loot and seeking the Boss.")
    print("Defeat the Boss and claim the title as Dungeon Master!")
    player_name = input("Enter your character name: ==> ")
    player = Person(player_name)
    current_room = "start_room"
    game_running = True

    menu()

    while game_running and player.health > 0: #or boss.health > 0
        print("What would you like to do? ('m' for menu)")
        user_input = input("==> ").lower().strip()
        print(" ")
        
        if user_input == 'move':
            current_room = display_room(current_room)
        elif user_input== 'search':
            search(player)
        elif user_input == 'fight':
            make_attack(player)
        elif user_input in ('menu', 'm'):
            menu()
        elif user_input == 'status':
            player_status(player)
        elif user_input == 'exit':
            game_running = False
        else: print("You entered a wrong command!")

def menu():
    print("To move from room to room type: 'move'")
    print("To search the room type: 'search'")
    print("To fight a mob you encounter type: 'fight'")
    print("To try to loot type: 'loot'")
    print("To view the menu type: 'menu'")
    print("To view your player status type: 'status'")
    print("To exit the game type: 'exit")

def display_room(current_room):
    print(rooms[current_room]["description"])
    print(f"There are the exits: {" ".join(rooms[current_room]["exits"].keys())}")
    print("Where would you like to move? ")
    user_direction = input("==> ")
    print(" ")
    
    if user_direction in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][user_direction]
        print(f"You have moved to the {current_room}")
    else: print("You cannot move there.")

    return current_room

def search(player):
    # room_search = random.randint(1, 1)
    # if room_search == 1:
    for i in loot:
        if i["name"] == "key":
            loot_item = i["name"]
    player.add_item(loot_item)

def make_attack(player):
    mob_types = [Goblin, Kobald, Orc]
    mob = random.choice(mob_types)()
    mob_init = random.randint(1, 20)
    player_init = random.randint(1, 20)
    print(f"The {mob.name} rolled a {mob_init} initiative roll.")
    print(f"{player.name} rolled a {player_init} initiative roll.")
    print("")

    player_turn_first = player_init > mob_init

    while player.health > 0 and mob.health > 0:

        if player_turn_first:
            player_attack(player, mob)
            if player.health <= 0:
                break
            mob_attack(mob, player)
        else:
            mob_attack(mob, player)
            if mob.health <= 0:
                break
            player_attack(player, mob)

def mob_attack(mob, player):
    attack_roll = random.randint(1, 20)
    print(f"The {mob.name} rolled a {attack_roll} against your AC of {player.ac}")
    if attack_roll >= player.ac:
        player.take_damage(mob.base_attack)
    else: print("Attack missed!\n")

def player_attack(player, mob):
    attack = input("Type roll to make an attack: ==> ")
    if attack == "roll":
        attack_roll = random.randint(1, 20)
        print(f"You rolled a {attack_roll} against the AC of {mob.ac}")
        if attack_roll >= mob.ac:
            mob.take_damage(player.base_attack)
        else: print("Attack missed!\n")

def kill_switch(player):
    player.health = 0

def player_status(player):
    player.player_status()

def main():
    game_start()

if __name__ == "__main__":
    main()