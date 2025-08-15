from pathlib import Path

def read_file(path):
    """Read files and print the contents of the file to the screen."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        pass
    else:
        # Print the contents of the file to the screen.
        print(f"\nThe content of {path} is:")
        for line in contents.splitlines():
            print(line)

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    path = Path(filename)
    read_file(path)
