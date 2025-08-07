class User:
    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.age = age

    def describe_user(self):
        print(f"\nFirst name: {self.first_name.title()}.")
        print(f"Last name: {self.last_name.title()}.")
        print(f"City: {self.city.title()}.")
        print(f"Age: {self.age}") 

    def greet_user(self):
        print(f"\nWelcome {self.first_name.title()} {self.last_name.title()}!")

user = User("renata", "cruz", "monterrey", 19)
user.describe_user()
user.greet_user()

user = User("isabela", "reyes", "mexico city" ,18)
user.describe_user()
user.greet_user()

user = User("camila", "navarro", "guadalajara", 20)
user.describe_user()
user.greet_user()
