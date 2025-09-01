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
    

    print(data[0]["start_room"])
    print("Directions: n for north, e for east, s for south, w for west")
    user_input = input("Where would you like to go? ==> ")
    
    if user_input in data["exits"]:
        print(data["hallway"])
    else: print("you cannot move that way!")

if __name__ == "__main__":
    main()