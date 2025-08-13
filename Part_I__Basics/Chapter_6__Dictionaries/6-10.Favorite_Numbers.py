favorite_numbers = {
    'Gabo': (69, 13, 10),
    'Isabela': (21, 16),
    'Monika': (7, 2019, 6),
    'Ana': (3, 21, 17),
    'Caleb': (7, 2019, 2),
}

for person, numbers in favorite_numbers.items():
    numbers_list = ", ".join(str(n) for n in numbers)
    print(f"{person}'s favorite numbers are: {numbers_list}")

