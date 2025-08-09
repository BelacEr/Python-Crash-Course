class User:

    def __init__(self, first_name, last_name, city, age):
        self.first_name = first_name    # attribute
        self.last_name = last_name
        self.city = city
        self.age = age
        self.login_attempts = 0

    def describe_user(self):            # method
        """Method that prints all user information."""
        print(f"\nFirst name: {self.first_name.title()}.")
        print(f"Last name: {self.last_name.title()}.")
        print(f"City: {self.city.title()}.")
        print(f"Age: {self.age}") 

    def greet_user(self):
        """Methot that greets the user. """
        print(f"\nWelcome {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """Method that increments login_attempts by one."""
        self.login_attempts +=  1

    def reset_login_attempts(self):
        """Method that resets the value of login_attempt to 0."""
        self.login_attempts = 0


user = User("renata", "cruz", "monterrey", 19)  # Instance
user.describe_user()
user.greet_user()

user = User("isabela", "reyes", "mexico city" ,18)
user.describe_user()
user.greet_user()

user = User("camila", "navarro", "guadalajara", 20)
user.describe_user()
user.greet_user()

print("\n")
a = 0
while a < 5:    # call increment_login_attempts 5 times
    user.increment_login_attempts()
    a += 1

print(f"Call attempts: {user.login_attempts}")

user.reset_login_attempts()     # reset login_attempts to 0
print("\nlogin_attempts has been reset to 0\n")

print(f"Call attemtps: {user.login_attempts}")
