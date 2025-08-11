from random import sample

lottery_list = [12, 38, 41, 40, 17, 37, 83, 19, 34, 97, 'c', 'h', 'j', 'm', 'z',]

lottery_number = sample(lottery_list, 4)

print("🏆 Lottery Results 🏆")
print("---------------------")
print(f"The winning ticket: {lottery_number}")

my_ticket = None
tries = 0
while my_ticket != lottery_number:
    """
    A loop that keep pulling numbers until your ticket wins.
    """
    my_ticket = sample(lottery_list, 4)
    tries += 1
print(f"\nThe number of attempts made until obtaining the winning ticket was {tries}")
