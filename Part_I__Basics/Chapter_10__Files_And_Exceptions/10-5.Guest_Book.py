from pathlib import Path

path = Path("guest_book.txt")

a = 0           
users = ""                                      # Creates an empty string to store user names.
active = True
while active:                                   # A loop that repeats until someone types 'q'.
    print("\nType 'q' to finish")
    user_input = input("What is your name? ")   # Ask for the user's name.
    if user_input == 'q':
        active = False                          # Break the loop.
    else:
        users += user_input
        users += "\n"                           # Each entry appears on a new line.
path.write_text(users)
