import user_module

admin = user_module.Admin("Renata", "Cruz", "monterrey", 19)    #instance
admin.privileges.show_privileges()


"""

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

admin = Admin("Renata", "Cruz", "monterrey", 19)    # instance
admin.show_privileges()

"""
