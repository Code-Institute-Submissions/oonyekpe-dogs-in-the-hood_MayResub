import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('dogs_in_the_hood')

class Dog_Walker:

    """
    A class used to represent a dog walker

    ...

    Attributes
    --------------------------------------
    first_name - str
        The walker's first name
    
    last_name - str
        The walker's last name

    email - str
        The walker's email address

    password - str
        The walker's account password

    availability_cal - list
        An array of the walker's availability, Monday to Sunday, mornings and afternoons for 3 weeks

    Methods
    --------------------------------------

    walker_full_name
        Returns the full name of the walker

    walker_availability_w1
        Returns the walkers availability this week

    walker_availability_w2
        Returns the walkers availability next week

    walker_availability_w3
        Returns the walkers availability in two week's time
    """

    def __init__(self, first_name, last_name, email, password):
        """
        Instance attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.availability_cal = []

    def walker_full_name(self):
        """
        Return the walker's full name
        """
        return f'{self.first_name} {self.last_name}'

class Dog_Owner:

    """
    A class used to represent a dog owner

    ...

    Attributes
    --------------------------------------
    first_name - str
        The owner's first name
    
    last_name - str
        The owner's last name

    email - str
        The owner's email address

    password - str
        The owner's account password

    booking_cal - list
        An array of the owner's bookings, Monday to Sunday, mornings and afternoons for 3 weeks

    Methods
    --------------------------------------

    owner_full_name
        Returns the full name of the owner

    owner_bookings_w1
        Returns the owner's bookings this week

    owner_bookings_w2
        Returns the owner's bookings next week

    owner_bookings_w3
        Returns the owner's bookings in two week's time
    """

    def __init__(self, first_name, last_name, email, password):
        """
        Instance attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.booking_cal = []

    def owner_full_name(self):
        """
        Return the owner's full name
        """
        return f'{self.first_name} {self.last_name}'



# User functions

def homepage():
    """
    Welcome and introduction text
    Description of the service of this website
    Guidance of how to use the service
    Invitation to feedback to website owner
    """
    print("Dogs in the Hood")
    print("Where dog owners meet dog walkers")
    print("To get started, register as either a dog owner or dog walker. You will then be able to book a walker, or register your availability.")

def login_or_register():
    """
    Check if the user wants to log in or register,
    And return the answer.
    """
    print("Do you have an account?")
    print("1 - Log In")
    print("2 - Create an account")
    answer = input("Enter your answer here:\n").strip()

    end_section()

    # Validate if the answer is 1 or 2
    while answer not in ("1", "2"):
        print("Please choose between one of the options.")
        answer = input("Enter your answer here:\n").strip()

        end_section()

    return answer

def log_in():
    """
    Code used to do a log in
    """
    print("Good to have you back!")
    print("I just need to check your email.")
    print("Can you write it for me?")

    while True:
        user_email = collect_email()
        walker = is_walker(user_email)
        owner = is_owner(user_email)
        # If it is a walker's email
        if walker:
            walker_function(user_email)
            break
        # If it is an owner's email
        elif owner:
            info = owner_info(user_email)
            owner = create_owner(info)
            owner_function(owner)
            break
        else:
            print("Sorry, I couldn't find your email")
            answer = email_not_found()
            # Try again
            if answer == "1":
                print("Can you write your email again?")
                pass
            # Register
            elif answer == "2":
                create_account()
                break

def collect_email():
    """
    Collect the user email
    """
    while True:
        email = input("Enter your answer here:\n").strip()

        end_section()

        if user_validate_email(email):
            break

    return email

def is_walker(email):
    """
    Check if email is from a customer account
    """
    walker_worksheet = select_worksheet('dog_walkers')
    email_column = customer_worksheet.col_values(3)

    if email in email_column:
        return True
    else:
        return False

def is_owner(email):
    """
    Check if email is from a admin account
    """
    owner_worksheet = select_worksheet('dog_owners')
    email_column = admin_worksheet.col_values(3)

    if email in email_column:
        return True
    else:
        return False

def email_not_found():
    """
    Used when the system can't find the email.
    Check if the user want to try another email or create a new account,
    And return the answer
    """
    print("Do you want:")
    print("1 - Try again")
    print("2 - Create an account")
    answer = input("Enter your answer here:\n").strip()

    end_section()

    # Validate if the answer is 1 or 2
    while answer not in ("1", "2"):
        print("Invalid option, please choose between 1 or 2.")
        answer = input("Enter your answer here:\n").strip()

        end_section()

    return answer


def create_account():
    """
    Code used to create an account
    """
    print("Are you a")
    print("1 - Dog owner")
    print("2 - Dog walker")
    account_type = input("Enter your answer here:/n").strip()

    if account_type == "1":
        owner = register_owner()
        owner_function(owner)

    elif account_type == "2":
        walker = register_walker()
        walker_function(walker)

    else:
        print("Sorry, your answer wasn't recognised")
        create_account()    




def register_owner():
    """
    Register the user as a new owner.
    Return an Owner.
    """
    print("Let's make a customer account for you!")
    print("I need some basic info.\n")
    owner_info = new_owner_info()
    update_worksheet(owner_info, "dog_owners")

    return create_owner(owner_info)

def owner_info(email):
    """
    Collect the owner info from the dogs in the hood worksheet
    Return a list with the owner info
    """
    owner_worksheet = select_worksheet('dog_owners')
    user_email = email
    row = find_row(user_email, customer_worksheet)
    owner_info = owner_worksheet.row_values(row)

    return [owner_info[0], owner_info[1], owner_info[2]]

def new_owner_info():
    """
    Collect the owner info (first name, last name, email and password),
    And check if its not already registered.
    Return a list with the new owner info
    """
    owner_worksheet = select_worksheet('dog_owners')
    email_column = owner_worksheet.col_values(3)

    print("What's your first name?")
    first_name = collect_name()
    print("What's your last name?")
    last_name = collect_name()
    print("What's your email?")

    while True:
        email = collect_email()

        # Check if email is already registered
        if email not in email_column:
            break
        else:
            print("Sorry, this email is already in use")
            print("Can we try again?\n")
    
    print("Please choose a secure password for your account")
    password = collect_password()

    return [first_name, last_name, email, password]


def create_owner(data):
    """
    Create the customer
    """
    return Dog_Owner(data[0], data[1], data[2])

def collect_name():
    """
    Collect the user's first and last name
    """
    while True:
        name = input("Enter your answer here:\n").capitalize().strip()

        end_section()

        if validate_name(name):
            break

    return name

def collect_password():
    """
    Collect the user's password
    """
    while True:
        password = input("Enter your answer here: /n")

        end_section()

    return password

def select_worksheet(option):
    """
    Based on the option, return the right worksheet
    """
    worksheet_dict = {
        "1": 'dog_owner',
        "2": 'dog_walker',
    }

    worksheet = ""

    for key, value in worksheet_dict.items():
        if option == key:
            worksheet = SHEET.worksheet(value)

    return worksheet


def update_worksheet(data, worksheet):
    """
    Receives a list to be inserted into a worksheet
    Update the relevant worksheet with the data provided
    """
    # Same function as used on the love_sandwiches walk through project
    # by Code Institute
    worksheet_to_update = select_worksheet(worksheet)
    worksheet_to_update.append_row(data)


def find_row(item, worksheet):
    """
    Find the item's row in the specified worksheet
    """
    cell = worksheet.find(item)

    return cell.row

# Validation functions

def validate_name(name):
    """
    Validate customer name
    Check if the name is at least 1 char long
    """
    try:
        if len(name) < 1:
            raise ValueError("Your name needs to be at least one char long.")

    except ValueError as e:
        print(f"Incorrect input: {e} Please try again.")
        return False

    return True

def user_validate_email(email):
    """
    Validate the email address.
    Check if follows the email pattern ____@xxx.xx
    """
    try:
        validate_email(email)

        return True

    except EmailNotValidError as e:
        print(str(e))
        print("Example: code@codersbistro.com")
        print('Lets try again')


# Formatting

def end_section():
    """
    Print a # line to end the sections
    """
    print(" ")
    print("# "*25)
    print(" ")

# Main function

def main():
    """
    Run the main code
    """
    # Welcome message
    homepage()
    sleep(2)

    end_section()

    # Login or register
    user_option = login_or_register()

    # Run the system based on the option
    # Log in option
    if user_option == "1":
        log_in()

    # Register option
    elif user_option == "2":
        create_account()


main()
