import json
import random
from models.player import Person
from models.goblin import Goblin
file_path = "rooms.json"

def read_file():
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

rooms = read_file()

def game_start():
    print("Welcome to The Game!")
    print("Search through the rooms, collecting loot and seeking the Boss.")
    print("Defeat the Boss and claim the title as Dungeon Master!")
    player_name = input("Enter your character name: ==> ")
    player = Person(player_name)
    current_room = "start_room"

    menu()

    while player.health > 0: #or boss.health > 0
        print("What would you like to do? ('m' for menu)")
        user_input = input("==> ")
        print(" ")
        
        if user_input.lower() == 'move':
            current_room = display_room(current_room)
        elif user_input.lower()== 'search':
            search()
        elif user_input.lower() == 'fight':
            make_attack(player)
        elif user_input.lower() == 'run':
            pass
        elif user_input.lower() == 'menu':
            menu()
        elif user_input.lower() == 'status':
            player_status(player)
        elif user_input.lower() == 'kill':
            kill_switch(player)
        else: print("You entered a wrong command!")

def menu():
    print("To move from room to room type: 'move'")
    print("To search the room for loot type: 'loot'")
    print("To fight a mob you encounter type: 'fight'")
    print("To retreat or avoid an encounter type: 'run'")
    print("To view your player status type: 'status'")

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

def search():
    room_search = random.randint(1, 3)
    if room_search == 1:
        print("There is something moving about in this room!")
    elif room_search == 2:
        print("You see something shiny laying on the desk!")
    elif room_search == 3:
        print("The room is completely empty")

# def is_mob(current_room):
#     if "mobs" in rooms[current_room]:
#         ran_mob = random.randint(0, 2)
#         mob_type = rooms[current_room]["mobs"][ran_mob]
        
#         print(f"When you enter the room you see a {mob_type}.")

def player_status(player):
    player.player_status()

def make_attack(player):
    mob_types = [Goblin]
    mob = random.choice(mob_types)()
    mob_init = random.randint(1, 20)
    player_init = random.randint(1, 20)
    print(f"The {mob.name} rolled a {mob_init} initiative roll.")
    print(f"{player.name} rolled a {player_init} initiative roll.")
    print("")

    while player.health > 0 and mob.health > 0:

        if mob_init > player_init:
            attack_roll = random.randint(1, 20)
            print(f"The {mob.name} rolled a {attack_roll} against your AC of {player.ac}")
            if attack_roll >= player.ac:
                player.take_damage(mob.base_attack)
            else: print("Attack missed!\n")

            if player.health <= 0:
                break

            attack = input("Type roll to make an attack: ==> ")
            if attack == "roll":
                attack_roll = random.randint(1, 20)
                print(f"You rolled a {attack_roll} against the AC of {mob.ac}")
                if attack_roll >= mob.ac:
                    mob.take_damage(player.base_attack)
                else: print("Attack missed!\n")
            elif attack == "special":
                pass
        elif player_init > mob_init:
            attack = input("Type roll to make an attack: ==> ")
            if attack == "roll":
                attack_roll = random.randint(1, 20)
                print(f"You rolled a {attack_roll} against the AC of {mob.ac}")
                if attack_roll >= mob.ac:
                    mob.take_damage(player.base_attack)
                else: print("Attack missed!\n")

                if mob.health <= 0:
                    break

            attack_roll = random.randint(1, 20)
            print(f"The {mob.name} rolled a {attack_roll} against your AC of {player.ac}")
            if attack_roll >= player.ac:
                player.take_damage(mob.base_attack)
            else: print("Attack missed!\n")


def kill_switch(player):
    player.health = 0

def main():
    game_start()

if __name__ == "__main__":
    main()