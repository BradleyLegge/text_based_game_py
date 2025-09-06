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
        
        if user_input.lower() == 'move':
            current_room = display_room(current_room)
        elif user_input.lower()== 'loot':
            pass
        elif user_input.lower() == 'fight':
            pass
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
    print("To view your player status type: 'status' ")

def display_room(current_room):
    print(rooms[current_room]["description"])
    print(f"There are the exits: {" ".join(rooms[current_room]["exits"].keys())}")
    print("Where would you like to move? ")
    user_direction = input("==> ")
    
    if user_direction in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][user_direction]
        print(f"You have moved to the {current_room}")  
    else: print("You cannot move there.")

    return current_room

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
        
def player_status(player):
    player.player_status()

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