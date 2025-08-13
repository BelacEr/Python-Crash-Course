numbers = [cube ** 3 for cube in range(1,11)]   # the cube of each integer from 1 through 10

for number in numbers:
    print(number)



print('\nThe first three items in the list are:', numbers[:3])
print('Three items from the middle of the list are:', numbers[4:7])
print('The last three items in the list are:', numbers[-3:])
