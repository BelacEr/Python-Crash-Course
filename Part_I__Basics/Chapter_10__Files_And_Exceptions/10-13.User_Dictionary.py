from pathlib import Path
import json

def enter_number(prompt: str) -> int:
    """Prompt user for an integer input with validation.
    
    Args:
        prompt (str): Custom input prompt to display.
        
    Returns:
        int: Validated integer input from user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Error: Please enter a valid integer.")

def enter_name(prompt: str) -> str:
    """Prompt user for an alphabetical name (allows spaces).
    
    Args:
        prompt (str): Custom input prompt to display.
        
    Returns:
        str: Validated name containing only letters/spaces.
    """
    while True:
        name = input(prompt).strip()
        if name.replace(" ", "").isalpha():     # Allows spaces for multi-word names
            return name
        print("Error: Names can only contain letters and spaces.")

def get_new_user(path: Path) -> None:
    """Collect new user details and save to JSON file.
    
    Args:
        path (Path): Path object for the JSON file.
    """
    user_data = {
        "First name": enter_name("First name: "),
        "Last name": enter_name("Last name: "),
        "Username": input("Username: ").strip(),
        "Age": enter_number("Age: ")
    }
    
    path.write_text(json.dumps(user_data, indent=4))  # Pretty-print JSON

def user_information() -> None:
    """Display or collect user information from JSON file."""
    path = Path("user_information.json")
    
    if path.exists():
        print("\n--- User Information ---")
        data = json.loads(path.read_text())
        for key, value in data.items():
            print(f"{key}: {value}")
    else:
        get_new_user(path)
        print("\nWe'll remember you next time! ♡")

if __name__ == "__main__":
    user_information()
