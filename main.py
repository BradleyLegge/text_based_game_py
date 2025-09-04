import json
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

def main():
    game_start()

def game_start():
    print(f"Welcome to The Game!")
    print("Menu")
    print("New Game ('n' or 'N')")
    print("Saved Game ('s' or 'S')")
    new_or_saved_game(input("==> "))

def new_or_saved_game(user_input):
    if user_input.lower() == 'n':
        print("New Game loaded")
        # current_room = "start_room"
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
        # print(current_room)
        room_exits(current_room)
    # elif user_input == 'm' or 'M':
    #     player.player_status()
        
def player_status(user_input, player):
    if user_input == 'm' or 'M':
        player.player_status()

if __name__ == "__main__":
    main()