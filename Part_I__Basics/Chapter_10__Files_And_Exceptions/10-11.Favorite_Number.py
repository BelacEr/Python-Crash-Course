from pathlib import Path
import json

def favorite_number():
    """Asks for the user's favorite name. Only accepts numbers."""
    while True:
        try:
            return float(input('\nWhat is your favorite number? '))
        except ValueError:
            print("Please, make sure to enter a valid number.")

def store_number():
    """
    Save the user's favorite number to a file. If the file already exists it will be replaced.
    """
    number = favorite_number()
    path = Path('favorite_number.json')
    contents = json.dumps(number)
    path.write_text(contents)

# Run the program.
if __name__ == '__main__':
    store_number()
