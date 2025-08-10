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

class Admin(User):

    def __init__(self, first_name, last_name, city, age):
        """       
        Initialize attributes of the parent class.
        Then initialize attributes that shows administrator privileges.
        """
        super().__init__(first_name, last_name, city, age)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Method that shows administrator privileges."""
        print("\nAdministrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
