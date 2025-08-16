from pathlib import Path
import json

def enter_number():
    """Asks for the user's favorite name. Only accepts numbers."""
    while True:
        try:
            return float(input('\nWhat is your favorite number? '))
        except ValueError:
            print("Please, make sure to enter a valid number.")

def get_stored_number(path):
    """Save the user's favorite number to a file."""
    number = enter_number()
    contents = json.dumps(number)
    path.write_text(contents)

def your_favorite_number():
    """Says the user's favorite number."""
    path = Path('favorite_number.json')
    if path.exists():       # If the file exists, we say what the user's favorite number is (the file).
        contents = path.read_text()
        number = json.loads(contents)
        print(f"\nI know your favorite number! It's {number}.")
    else:       # If the file does not exist, we create it. 
        get_stored_number(path)
        print(f"We'll remember your favorite number the next time you come back.")

# Run the program
if __name__ == '__main__':
    your_favorite_number()
