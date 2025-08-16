from pathlib import Path
import json

def your_favorite_number():
    """Read the file and say what the user's favorite number is."""
    path = Path('favorite_number.json')
    contents = path.read_text()
    number = json.loads(contents)
    print(f"Your favorite number is {number}!")

if __name__ == '__main__':
    your_favorite_number()
