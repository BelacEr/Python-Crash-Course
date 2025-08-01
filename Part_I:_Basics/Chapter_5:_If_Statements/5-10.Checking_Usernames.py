current_usernames = ['belac', 'gabo', 'admin', 'jack', 'monika']
new_users = ['gabo', 'jack', 'natsuki', 'sayori', 'yuri']


for user in new_users:
    if user in current_usernames:
        print('The username is already in use. Please enter a new username.')
    else:
        print('The username is available.')
