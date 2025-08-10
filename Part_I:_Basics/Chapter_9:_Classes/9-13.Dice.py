from random import randint

class Dice:
    def __init__(self, sides=6):    
        self.sides = sides  # attribute

    def roll_die(self):  # method
        """Prints a random number between 1 and the number of sides the variable has."""
        a = 0
        while a < 10:   # Make a 6-sided die and roll it 10 times. 
            number_random = randint(1, self.sides)
            print(f"The number on the die face is: {number_random}")
            a += 1

dice = Dice()    # instance
dice.roll_die()
