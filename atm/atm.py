credentials = {'me': 'passMe', 'you': 'passYou', 'other': 'passOther'}


name = input('Enter your name\n')
password = input('Enter your password\n')

if password == credentials.get(name, ''):
    print('Welcome %s' % name)
    current_time = datetime.now().strftime('%H:%M:%S')
    print('--------------------------')
    print("\nLast login: %s\n" % current_time)
    options = '1: Withdraw\n2: Deposit\n3: Complaint\n'
    print(options)
    action = int(input('What do you want to do\n'))
    if action == 1:
        withdrawalOperation()
    elif action == 2:
        depositOperation()
    elif action == 3:
        input('What issue would you like to report?\n')
        print('Thank you for contacting us.')
    else:
        print('Invalid option selected. Please try again.')
        bankOperation(user)
else:
    print('Incorrect user details, please try again.')
