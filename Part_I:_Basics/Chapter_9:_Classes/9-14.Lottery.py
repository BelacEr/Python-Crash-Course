from random import sample

lottery_list = [12, 38, 41, 40, 17, 37, 83, 19, 34, 97, 'c', 'h', 'j', 'm', 'z',]

# Select 4 numbers or letter from the list
lottery_number = sample(lottery_list, 4)

print("🏆 Lottery Results 🏆")
print("---------------------")
print(f"The winning ticket: {lottery_number}")
