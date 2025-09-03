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
    lst = []
    current_room = "start_room"

    print(data["start_room"]["description"])
    for i in data["start_room"]["exits"]:
        lst.append(i)
    print(f"These are the exits: {" ".join(lst)}")
    print("What would you like to do?")
    user_input = input("==> ")

    if user_input in data[current_room]["exits"]:
        current_room = data[current_room]["exits"][user_input]
        print(f"You are in {current_room}")
    else: print("Outside")


if __name__ == "__main__":
    main()