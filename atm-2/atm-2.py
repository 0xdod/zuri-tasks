import random
from datetime import datetime

database = {1111111111: ['testing', 'tester', 'testpassword']}


def login():
    username = input("What is your username? \n")
    password = input("Your password? \n")
    if(username in allowedLogins and password == allowedLogins[username]):
        print("Welcome " + username)
        return True
    else:
        print("Password or Username Incorrect. Please try again")
        return False


database = {}  # dictionary


def init():

    print("Welcome to Gbiti bank")

    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):

        login()
    elif(haveAccount == 2):

        register()
    else:
        print("You have selected invalid option")
        init()


def login():

    print("********* Login ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for accountNumber, userDetails in database.items():
        if(accountNumber == accountNumberFromUser):
            if(userDetails[3] == password):
                print("Welcome %s %s " % (userDetails[0], userDetails[1]))
                current_time = datetime.now().strftime('%H:%M:%S')
                print('----------------------------------')
                print("\nLast login: %s\n" % current_time)
                bankOperation(userDetails)

    print('Invalid account or password')
    login()


def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()


def bankOperation(user):
    options = '1: Withdraw\n2: Deposit\n3: Complaint\n4: Exit'
    while True:
        print(options)
        action = int(input('What do you want to do\n'))
        if action == 1:
            withdrawalOperation()
        elif action == 2:
            depositOperation()
        elif action == 3:
            input('What issue would you like to report?\n')
            print('Thank you for contacting us.')
        elif action == 4:
            input('Goodbye')
            exit()
        else:
            print('Invalid option selected. Please try again.')
            bankOperation(user)


def withdrawalOperation():
    amt = int(input('How much would you like to withdraw?:\n'))
    print('Processing request to withdraw %d...' % amt)
    print('Take your cash')


def depositOperation():
    amt = int(input('How much would you like to deposit?:\n'))
    print('Processing request to deposit %d...' % amt)
    print('Success')


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


if __name__ == '__main__':
    init()
