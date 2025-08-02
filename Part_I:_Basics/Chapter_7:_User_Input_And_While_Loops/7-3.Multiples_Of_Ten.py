while True:
    try:
        number = int(input('Enter a number: '))
        break
    except ValueError:
        print('Enter a valid number.')

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of 10.")
else:
    print(f"\nThe number {number} is not a multiple of 10.")
