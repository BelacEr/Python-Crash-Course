from user_module import User
from admin_module import Admin, Privileges

admin = Admin('Renata', 'Cruz', 'monterrey', 19)   # instance
admin.privileges.show_privileges()
