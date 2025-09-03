import json
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
lst = []

def main():
    current_room = "start_room"
    
    game_start()
    room_exits(current_room)

def game_start():
    print("Welcome to The Game! Travel from room to room collecting loot and find the key to unlock "
    "the boss room. If you are brave enough fight the boss and collect the ultimate prize!")

def room_exits(current_room):        
    print(rooms[current_room]["description"])
    
    print(f"There are the exits: {" ".join(rooms[current_room]["exits"].keys())}")
    print("Where would you like to go?")
    user_input = input("==> ")
    valid_room(user_input, current_room)

def valid_room(user_input, current_room):
    if user_input in rooms[current_room]["exits"]:
        current_room = rooms[current_room]["exits"][user_input]
        room_exits(current_room)
        

if __name__ == "__main__":
    main()