from pathlib import Path            # Import Path function

path = Path('learning_python.txt')  
contents = path.read_text()

for line in contents.splitlines():  # Skip the temporary variable and loop directly over the list that splitlines() returns
    print(line.replace("Python", "C"))  # Replace the word Python with C
