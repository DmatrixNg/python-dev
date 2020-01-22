#!C:/Users/user/AppData/Local/Programs/Python/Python38/python.exe

# database
database = [
    {'name': 'Elijah Okokon', 'email': 'test1@example.com', 'password': 'test1', 'account_bal': 2000},
    {'name': 'Bassey Okokon', 'email': 'test2@example.com', 'password': 'test2', 'account_bal': 200}
]


def next_opp(user):
    next = input('Do you want to perform another operation (yes/no)\n')
    while True:
        if next == 'yes' or next == 'no':
                break
        else:
            print('Wrong input, please enter Yes or No\n')
        next = input('Do you want to perform another operation (yes/no)\n')

    if next == 'yes':
        user_interface(user)
    else:
        exit('Exiting Thanks for banking with us')

#check user in database
def check_data(key, value):
    for user in database:
        if user[key] == value:
            return user
    return False


# function to deposit cash
def deposit_cash(user):
    # amount to be deposited
    deposit = input('please enter the deposit amount\n')
    while(True):
        try:
            user_amount = float(deposit)
            if user_amount > 0.0:
                break
            else:
                print('invalid amount\n')
                deposit = input('please enter the deposit amount\n')
        except ValueError:
            print('invalid amount\n')
            deposit = input('please enter the deposit amount\n')
    new_balance = float(user['account_bal']) + user_amount
    print('Congratulations you just deposited {deposit} into your account, your current balance is {balance}'.format(
        deposit=user_amount, balance=new_balance))
    next_opp(user)



def check_balance(user):
    print('Your account balance is {}\n'.format(user['account_bal']))
    next_opp(user)

# function to withdraw money given the user


def withdraw(user):
    amount = input('please enter the amount you want to withdraw\n')
    while(True):
        try:
            user_amount = float(amount)
            if user_amount > 0.0:
                break
            else:
                print('invalid amount\n')
                amount = input(
                    'please enter the amount you want to withdraw\n')
        except ValueError:
            print('invalid amount\n')
            amount = input('please enter the amount you want to withdraw\n')
    if user['account_bal'] == 0.0:
        print('insufficent balance')
        deposit_cash(user)
    elif user['account_bal'] < user_amount:
        print('insufficient balance\n')
    else:
        new_balance = float(user['account_bal']) - user_amount
        print('your have successfully withdrawn {withdrawn_amount}, your balance is {balance}'.format(
            withdrawn_amount=user_amount, balance=new_balance))
    next_opp(user)

# function to transfer money given user


def tranfer(user):
    amount = input('please enter the amount you want to transfer\n')
    while(True):
        try:
            user_amount = float(amount)
            if user_amount > 0.0:
                break
            else:
                print('invalid amount\n')
                amount = input(
                    'please enter the amount you want to transfer\n')
        except ValueError:
            print('invalid amount\n')
            amount = input('please enter the amount you want to transfer\n')
    if float(user['account_bal']) < user_amount:
        print('insufficent balance')
    else:
        receiver = input('please enter beneficiary\'s email address \n')
        while(True):
            beneficiary = check_data('email', receiver.lower())

            if beneficiary:
                break
            print('No user found\n')
            receiver = input('please enter beneficiaries email address\n')

        beneficiary_balance = float(beneficiary['account_bal']) + user_amount
        sender_balance = user['account_bal'] - user_amount
        beneficiary['account_bal'] = beneficiary_balance
        user['account_bal'] = sender_balance
        print('you have successfully transfered {sent_amount} to {reciever}, your new balance is {new_balance}'.format(
            sent_amount=user_amount, reciever=beneficiary['email'], new_balance=user['account_bal']))
    next_opp(user)


def user_interface(user):
    user_option = input(
        'press 1: check balance\npress 2: deposit\npress 3: withdraw\npress 4: transfer\npress 0: go back\n\n')
            # makes sure user chooses from available options
    while True:
        if user_option == '0' or user_option == '1' or user_option == '2' or user_option == '3' or user_option == '4':
                break
        else:
                print('please choose one the following options\n')
                user_option = input(
                        'press 1: check balance\npress 2: deposit\npress 3: withdraw\npress 4: transfer\npress 0: go back\n')
    
    if user_option == '0':
        main()
    elif user_option == '1':
        check_balance(user)
    elif user_option == '2':
        deposit_cash(user)
    elif user_option == '3':
        withdraw(user)
    else: 
        tranfer(user)

# function creates a new user
def create():
    email = input('please enter your email\n')
    # loop checks if user with the given email or identity already exist
    while(True):
        if not check_data('email', email.lower()):
            break
        else:
            print('An account with the email already exist.\n')
            email = input('please enter your email\n')

    name = input('please enter your name:\n')
    password = input('please choose a password:\n')
    
    # add new user to users
    new_user = {'name': name, 'email': email.lower(
    ), 'password': password, 'account_bal': 0.0}
    database.append(new_user)
    print('Account created successfully!')
    user_interface(new_user)


def main():
    # This variable holds an authenticated user
    
    option = input('press 1: create account \npress 2: transaction\n')

    
    
    if option == '1': 
        create()
    elif option == '2':
        transaction()
    else:
        print('incorrect input, press either 1 or 2\n')
        main()
        
def transaction():
        #ask user for  password
        password = input('please enter your password\n')
        # check if password is correct
        user = check_data('password', password)

        if not user:
            print('password incorrect, you are not authorized!')
            main()

        else:
            # authicate user
            print('Welcome! {}\n'.format(user['name']))
            user_interface(user)

if __name__ == "__main__":
    main()
