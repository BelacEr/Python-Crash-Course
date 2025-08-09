class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name  # attribute
        self.cuisine_type = cuisine_type
        self.number_served = 13

    def describe_restaurant(self):              # method
        print(f"Restaurant name: {self.restaurant_name}.")
        print(f"Restaurant cuisine: {self.cuisine_type}.")

    def open_restaurant(self):
        """Method that announces that the restaurant is open."""
        print("\nThe restaurant is open!")

    def restaurant(self):
        """Method to print the number of customers the restaurant has served"""
        print(f"\nThe number of customers the restaurant has served: {self.number_served}")

    def set_number_served(self, number_served):
        """Method that allows you to modify the number of customers that the restaurant has served."""
        self.number_served = number_served

    def increment_number_served(self, increment_served):
        """Method that allows increasing the number of customers served by the restaurant."""
        if increment_served >= 0:
            self.number_served += increment_served
        else:
            print("\nYou can't increase with less than 0!")

class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an ice cream stand.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Butter pecan', 'Cherry', 'Chocolate', 'Vanilla', 'Pistachio', 'Banana']

    def describe_flavors(self):
        print(f"\nIce Cream flavors:")
        for flavor in self.flavors:
            print(f'- {flavor}')


restaurant = Restaurant("Hearth & Stone", "Italian")    # instance

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.restaurant()

restaurant.set_number_served(36)
restaurant.restaurant()

restaurant.increment_number_served(107)
restaurant.restaurant()


ice_cream_stand = IceCreamStand("Sweet Scoops", "Ice Cream")
ice_cream_stand.describe_flavors()
