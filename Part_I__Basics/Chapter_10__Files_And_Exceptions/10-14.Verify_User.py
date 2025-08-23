from pathlib import Path
import json

def yes_or_not(prompt: str) -> str:
    """Prompt user for yes or not."""
    while True:
        choice = input(prompt).strip().lower()
        if choice == 'y':
            return choice
        elif choice == 'n':
            return choice
        else:
            print("\nMake sure to enter only 'y' or 'n'.")

def get_stored_username(path: Path) -> None:
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path: Path) -> None:
    """Prompt for a new username."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def main(z):
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Is {username} your username?")
        choice = yes_or_not("(y/n): ")
        if choice == 'y':
            print(f"\nWelcome back, {username}!")
        else:
            username = get_new_username(path)
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

if __name__ == '__main__':
    main()
