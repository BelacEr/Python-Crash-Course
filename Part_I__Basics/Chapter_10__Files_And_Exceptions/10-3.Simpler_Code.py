from pathlib import Path            # Import the Path function

path = Path('pi_digits.txt')
contents = path.read_text()

for line in contents.splitlines():  # I skip the temporary variable and loop directly over the list that splitlines() returns
    print(line)
