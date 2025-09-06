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
    player = Person("Soja")
    print(f"Welcome to The Game!")
    # print("Menu")
    # print("New Game ('n' or 'N')")
    # print("Saved Game ('s' or 'S')")
    # new_or_saved_game(input("==> "))
    room_exits("start_room")

def new_or_saved_game(user_input):
    if user_input.lower() == 'n':
        print("New Game loaded")
        room_exits("start_room")
    elif user_input.lower() == 's':
        print("Saved Game loaded")
    else: print("Bad input")

def room_exits(current_room):        
    print(rooms[current_room]["description"])
    
    print(f"There are the exits: {" ".join(rooms[current_room]["exits"].keys())}")
    print("Where would you like to go?")
    user_input = input("==> ")
    valid_room(user_input, current_room)

def valid_room(user_input, current_room):
    if user_input in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][user_input]
        is_mob(current_room)
        room_exits(current_room)

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

def main():
    game_start()

if __name__ == "__main__":
    main()