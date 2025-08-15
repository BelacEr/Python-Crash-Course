from pathlib import Path        # Import the Path function

path = Path('learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():  # Skip the temporary variable
    print(line)
