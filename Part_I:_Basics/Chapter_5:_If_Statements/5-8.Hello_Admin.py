usernames = ['belac', 'gabo', 'admin', 'jack', 'monika']

for username in usernames:
    if 'admin' == username:
        print(f'Hello {username},  would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again.')
