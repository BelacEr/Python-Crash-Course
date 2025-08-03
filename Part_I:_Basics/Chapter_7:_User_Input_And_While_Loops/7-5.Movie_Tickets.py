prompt = "Enter your age "
prompt += "(enter 'quit' when you finished): "

while True:
    age = int(input(prompt))

    if age < 3:
        print("\nThe ticket is free.")
        break
    elif age < 12:
        print('\nThe ticket is $10.')
        break
    else:
        print('\nThe ticket is $15.')
        break
