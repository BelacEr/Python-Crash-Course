glossary = {
    'dictionary': 'A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.',
    'list': 'A list is an ordered, changeable collection of items. Items can be of any type and duplicates are allowed.',
    'tuple': 'A tuple is like a list, but it is ordered and unchangeable (immutable).',
    'string': 'A string is a sequence of characters, usually used to represent text.',
    'integer': 'An integer is a whole number (no decimals).',
        }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")
