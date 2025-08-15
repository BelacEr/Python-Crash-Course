from pathlib import Path            # Import Path function

path = Path('learning_python.txt')  
contents = path.read_text()

lines = contents.splitlines()

for line in lines:
    print(line.replace("Python", "C"))  # Replace the word Python with C
