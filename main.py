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

def main():
    data = read_file()

    print(data["start_room"])
    print("Directions: n for north, e for east, s for south, w for west")
    print("Where would you like to go?")
    move_room(data)
    

def move_room(data):
    move = input("==> ")
    
    if move == "n":
        print(data["hallway"])
    elif move == "s":
        print("Cannot move this way")
    elif move == "w":
        print("Cannot move this way")
    elif move == "e":
        print("Cannot move this way")
    



if __name__ == "__main__":
    main()