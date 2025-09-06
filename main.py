import json
import random
from models.player import Person
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
    player_name = input("Enter your character name: ==> ")
    player = Person(player_name)
    current_room = "start_room"

    menu()

    while player.health > 0: #or boss.health > 0
        print(current_room)
        user_input = input("==> ")
        
        if user_input == 'move':
            display_room(current_room)
        elif user_input == 'loot':
            pass
        elif user_input == 'fight':
            pass
        elif user_input == 'run':
            pass
        elif user_input == 'menu':
            pass
        elif user_input == "status":
            pass
        elif user_input == "kill":
            kill_switch(player)
        else: print("You entered a wrong command!")

def menu():
    print("Welcome to The Game!")
    print("Search through the rooms, collecting loot and seeking the Boss.")
    print("Defeat the Boss and claim the title as Dungeon Master!")
    print("To move from room to room type: 'move'")
    print("To search the room for loot type: 'loot'")
    print("To fight a mob you encounter type: 'fight'")
    print("To retreat or avoid an encounter type: 'run'")
    print("What would you like to do?")


def display_room(current_room):
    print(rooms[current_room]["description"])
    print(f"There are the exits: {" ".join(rooms[current_room]["exits"].keys())}")
    print("Where would you like to move? ")
    user_input = input("==> ")
    is_valid_room(user_input, current_room)


# def room_exits(current_room):        
    
    
#     print("Where would you like to go?")
#     user_input = input("==> ")
#     valid_room(user_input, current_room)

def is_valid_room(user_input, current_room):
    if user_input in rooms[current_room]["exits"]:
        print("You can move there.")
        current_room = rooms[current_room]["exits"][user_input]
        print(current_room)
    else: print("You cannot move there.")

def is_mob(current_room):
    if "mobs" in rooms[current_room]:
        ran_mob = random.randint(0, 2)
        mob_type = rooms[current_room]["mobs"][ran_mob]
        
        print(f"When you enter the room you see a {mob_type}.")
        user_input = input("Would you like to fight ('f') it or run ('r')? ==> " )

        if user_input.lower() == 'f':
            enter_combat()
        elif user_input.lower() == 'r':
            pass

    else: pass

def enter_combat():
    print("You are about to enter combat!")
        
# def player_status(user_input, player):    
#     if user_input == 'm' or 'M':
#         player.player_status()

def make_attack(player):
    while player.health > 0:            #This needs to be done so the player(Soja) object is created
        attack_roll = random.randint(1, 20)
        
        print(f"{attack_roll} vs {player.ac}")
        
        if attack_roll >= player.ac:
            player.take_damage(2)
        else: print("Attack missed!")

def kill_switch(player):
    player.health = 0

def main():
    game_start()

if __name__ == "__main__":
    main()