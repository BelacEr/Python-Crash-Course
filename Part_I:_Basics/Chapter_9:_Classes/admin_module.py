from user_module import User

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
