from pathlib import Path

def count_words(path):
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"The file {path} does not exist.")
    else:
        # Find out how many times a word or phrase appears in a string
        print(f"The number of times the word 'the' appears in {path} is: {contents.lower().count('the ')}")

filename = 'romeo_and_juliet.txt'

path = Path(filename)
count_words(path)
