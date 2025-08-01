glossary = {
    'dictionary': 'A dictionary is a collection of key-value pairs. Each key is unique and maps to a value.',
    'list': 'A list is an ordered, changeable collection of items. Items can be of any type and duplicates are allowed.',
    'tuple': 'A tuple is like a list, but it is ordered and unchangeable (immutable).',
    'string': 'A string is a sequence of characters, usually used to represent text.',
    'integer': 'An integer is a whole number (no decimals).',
    'loop' : 'A loop is used to repeat a block of code multiple times. Common types: for and while loops.',
    'class': 'A class is a blueprint for creating objects in object-oriented programming.',
    'module': 'A module is a file containing Python code (functions, classes, variables) that can be imported and used in other files.',
    'exception': 'An exception is an error that occurs during program execution. You can handle them using try-except blocks.',
    'list comprehension': 'A list comprehension is a concise way to create lists using a single line of code.',
        }

for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")

