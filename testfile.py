'''
The purpose of this program is to store passwords in safe that could be easily accessed by the user.
Written by: Miguel Armado
Date: 03/04/2023

Version 1: Has done the functions for changing or manipulating the passwords
in each of the accounts in the safe but hasn't put in 
a login system for the main username and the main password.

Version 2: Successfully put in a separate function for checking a password and whether the password has met the specific criteria.
Also, improved my method of displaying the menu of my program.

Version 3: Added the log in feature to access the password safe.

Version 4: Added a function wherein it dictates the current list after the changes
that the user has done to their password safe.

Version 5: Fixed a big wherein if there are no accounts in the password safe,
the program will still let the user add or remove an account, and/or change the
password of an existing account.

'''
LOGON = {"miguel":"st22602"} # Store the username and the password that is needed to be inputted in order for the user to access the password safe
credentials = {"user1":"pass1", "user2":"pass2", "user3":"pass3"} # Store the accounts and password in a dictionary


menu = ("Find the password for an existing account", "Add a new account and new password for it",  # Store all the name of the features of the password safe.
        "Change password for an existing account", 
        "Remove an existing account", "Exit")

def logon(): # This function verifies the user whether the user has inputted the right username and password. Failure to do so will result in the program shutting down immediately.
    username = input("Enter username: ").lower()
    password = input("Enter password: ")    
    if username not in LOGON.keys() or password != LOGON[username]:
        return False
    return True
    

def introduction(): # This function says an introductory message which tells the user what the program is for
    print("This is a password manager, it stores the username and the corresponding password for it in a 'safe'")
            
def display_menu(): # This function displays the menu of features that the user can choose from. Will display an error message that corresponds to the error that the user has incurred. 
    while True:
        try:
            for count, item in enumerate(menu, 1):
                print(f"{count} {item}")
            print()
            choice = int(input("Enter the number of the feature: "))
            while choice not in range (1, 6):
                print("It seems that your number is not in te choices, please try again.")
                print()
                for count, item in enumerate(menu, 1):
                    print(f"{count} {item}")
                print()
                choice = int(input("Enter the number of the feature: "))
            return choice
        except ValueError:
            print("It seems that your input is not a number, please try again.")
            print()
                
                
   

def get_credentials(): # This function lets the user find the password for the account that theyy have inputted in the password safe
    account = input("What is the username of the password you are finding?: ").lower()
    while account not in credentials.keys():
        print("It seems that the username that you have inputted is not in our system, please try again.")
        account = input("What is the account of the password you are finding?: ").lower()
    print(f"The password is {credentials[account]}.")

def add_account(): # This function lets the user add an account and a password to the password safe
    new_account = input("What will be the new account's name?: ").lower()
    while new_account in credentials.keys():
        print("It seems that you already have this account in your safe, please try again.")
        new_account = input("What will be the new account's name?: ").lower()   
    new_password = input("What will be the new account's password (password must contain at least one letter and one digit): ")
    valid_pass = check_pass(new_password)
    credentials[new_account] = valid_pass
    print("Successfully added.")
    printlist()
    
        
            

def change_password(): # This function lets the user change the password of an existing account in the password safe
    account = input("What is the existing account's name?: ").lower()
    while account not in credentials.keys():
        print("It seems that the account that you have inputted is not in our system, please try again.")
        account = input("What is the existing account's name?: ").lower()
    newpass = input("What will be the new account's password (password must contain at least one letter and one digit): ")
    valid_pass = check_pass(newpass)
    credentials[account] = valid_pass
    printlist()

def remove_account(): # This function gives the user the ability to remove an account from the password safe
    account = input("What is the account that you want to remove from your safe?: ").lower()
    while account not in credentials.keys():
        print("It seems that the account that you have input is not in our system, please try again.")
        account = input("What is the account that you want to remove from your safe?: ").lower()
    credentials.pop(account)
    print(f"Account {account} is successfully removed.")
    printlist()

def check_pass(password): # This function serves as a validation system for passwords. This will check if the password that the user has inputted at times when a password is required to be inputted contains at least 1 letter, 1 digit, and has a minimum length of 8 characters. It will display the corresponding error message depending on what the error the user has incurred.
    while True:
        if len(password) < 8:
            print("It seems that your password is too short, please try again.")
        elif password.isdigit() == True:
            print("It seems that your password is only in numbers, please try again.")
        elif password.isalpha() == True:
            print("It seems that your password is only in letters, please try again.")
        elif password in credentials.values():
            print("It seems that this password is already in use.")
        else:
            print("Password accepted.")
            return password
        password = input("Type in the password: ")
        
def printlist(): # This function prints the account and the corresponding password for it everytime the user has changed something in the password safe. Specifically, I have put it in the functions remove_account(), change_password(), and add_account()
    for key, value in credentials.items():
        print(f"{key} | {value}")
        

access = logon() # Assigning the returned value of the function logon() to the variable access
if access == True: # If the user has inputted the right credentials, program will run
    introduction() # Outputs an introductory message
    exit = False # Set up a flag
    while exit == False: # While the flag's value is still the same, which in this case is False, the loop will run infinitely.
        print() # Make a space
        choice = display_menu() # Assign the returned value from the function display_menu in the variable "choice".
        if choice == 1 and len(credentials) != 0: # If the user has picked the 1st feature and has enough accounts in the user's password safe
            get_credentials() # Run the "Find the password for an acccount" function.
        elif choice == 2: # If the user picked the 2nd feature
            add_account() # Run the "Add an account to the password safe" function.
        elif choice == 3 and len(credentials) != 0: # If the user has picked the 3rd feature and has enough accounts in the user's password safe
            change_password() # Run the "Change password for an existing account" function
        elif choice == 4 and len(credentials) != 0: # If the user has picked the 4th feature and has enough accounts in the user's password safe
            remove_account() # Run the "Remove an account" function
        elif choice == 5: # If the user has picked number 5
            exit = True # Change the value of the flag
            print("Goodbye!") # Print a goodbye message, then exits the loop
        else: # If the user doesn't have accounts in the user's password safe, the program will not let the user access the features that requires accounts to be in the user's password safe, instead displays a message saying the user has an insufficient amount of accounts in the user's password safe to access the feature that the user has typed in or picked
            print(f"Not enough accounts, please add an account to use the feature \"{choice}\"")
else: # If the user has inputted the wrong username and  password for the password safe, it will shut down immediately
    print("Invalid username or password.") # Output an error message saying that the user has inputted the wrong username or password, and shut down the program immediately
