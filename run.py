"""
This programmme interact with users through a python
terminal to coordinate dog walks in a neighbourhood.
"""
import gspread
from google.oauth2.service_account import Credentials
from email_validator import validate_email, EmailNotValidError
from time import sleep

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('dogs_in_the_hood')
WORKSHEET = SHEET.worksheet("dogs_in_the_hood")


class User:

    """
    A class used to represent a dogs in the hood user

    ...

    Attributes
    --------------------------------------
    first_name - str
        The user's first name

    last_name - str
        The user's last name

    email - str
        The user's email address

    password - str
        The user's account password

        Methods
    --------------------------------------

    user_full_name
        Returns the full name of the user

    get_availability
        Returns the user's availability

    set_availability(day)
       Setting the user's availability to walk dogs on certain day of the week

    request_walkers(day)
       Return a list of up to five walkers on a given day of the week,
       excluding the current user
    """

    def __init__(self, first_name, last_name, email, password):
        """
        Instance attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def user_full_name(self):
        """
        Returns the user's full name
        """
        return f'{self.first_name} {self.last_name}'

    def get_availability(self):
        """
        Returns the user's availability
        1. Go to the Dogs in the hood spreadsheet and pull out the user's
        values from Mon to Sun
        2. Print out this information nicely
        """
        worksheet = SHEET.worksheet('dogs_in_the_hood')
        user_email = self.email
        row = find_row(user_email, worksheet)

        user_info = worksheet.row_values(row)

        availability = {
            'Monday': user_info[4],
            'Tuesday': user_info[5],
            'Wednesday': user_info[6],
            'Thursday': user_info[7],
            'Friday': user_info[8],
            'Saturday': user_info[9],
            'Sunday': user_info[10],
        }

        # return availabilitys

        if availability['Monday'] == "":
            return False
        else:
            return availability

        return False


# Welcome function


def homepage():
    """
    Welcome and introduction text
    Description of the service of this website
    Guidance of how to use the service
    Invitation to feedback to website owner
    """
    print("Dogs in the Hood")
    print("Where dog owners meet dog walkers")

# log in and sign up functions


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
    Code used to allow the user to log in
    """
    print("Good to have you back!")
    print("I just need to check your email.")
    print("Can you write it for me?")

    while True:
        user_email = collect_email()
        registered_user = is_user(user_email)

        # If it is a registered email
        if registered_user:
            info = user_info(user_email)
            user = create_user(info)
            print(f'Welcome {user.user_full_name()} you are registered!')
            user_function(user)
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
    print("Let's make your account!")

    new_user = register_user()
    new_user_availabilty = collect_availability()
    update_availability(new_user.email, new_user_availabilty)
    print(f'Welcome {new_user.user_full_name()} you are logged-in!')
    user_function(new_user)


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


def collect_password():
    """
    Collect the user's password
    """
    while True:
        password = input("Enter your answer here: \n")

        end_section()

        if validate_password(password):
            break

    return password


def collect_availability():

    user_availability = []

    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        user_input = ""
        while user_input not in [1, 2, "1", "2"]:
            print(f"Are you available on {day}?")
            print("1 - Available")
            print("2 - Unavailable")
            user_input = input("Enter your answer here:\n").upper().strip()
            if user_input not in [1, 2, "1", "2"]:
                print("invalid entry, please try again")
                return False
            else:
                user_availability.append(user_input)

                return user_availability
    return False


def is_user(email):
    """
    Check if email is from a customer account
    """
    user_worksheet = SHEET.worksheet('dogs_in_the_hood')
    email_column = user_worksheet.col_values(3)

    if email in email_column:
        return True
    else:
        return False


def register_user():
    """
    Register the user.
    Return the user's info
    """
    print("I need some basic info.\n")
    user_info = new_user_info()
    update_worksheet(user_info)

    return create_user(user_info)


def new_user_info():
    """
    Collect the user's info (first name, last name, email and password),
    And check if its not already registered.
    Return a list with the new user's info
    """
    worksheet = SHEET.worksheet('dogs_in_the_hood')
    email_column = worksheet.col_values(3)

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


def user_info(email):
    """
    Collect the user info from the dogs_in_the_hood worksheet
    Return a list with the user info
    """
    user_worksheet = SHEET.worksheet('dogs_in_the_hood')
    user_email = email
    row = find_row(user_email, user_worksheet)
    user_info = user_worksheet.row_values(row)

    return [user_info[0], user_info[1], user_info[2], user_info[3]]


def create_user(data):
    """
    Create the customer
    """
    return User(data[0], data[1], data[2], data[3])

# Main application functions


def user_function(user):
    """
    Code used for registered users
    """

    email = user.email
    return_calendar(user)
    user_menu_selection = user_menu()

    if user_menu_selection == '1':
        day_to_book = collect_day()
        # see if user already has a booking
        owner_info = find_row(email, SHEET.worksheet("dogs_in_the_hood"))
        cell = SHEET.worksheet("dogs_in_the_hood").cell(
            owner_info, int(day_to_book)+4)
        if cell.value != "Available":
            booked_walker = cell.value.replace("booked for walk", "").strip()
            print(
                f"You already have a booking. You will have to email {booked_walker} to cancel")  # noqa
        else:
            chosen_walker = request_walker(day_to_book)
            book_walker(email, chosen_walker, day_to_book)
        user_function(user)
    elif user_menu_selection == '2':
        print("Thank you for using dogs-in-the-hood. Goodbye!")


def user_menu():
    """
    Display the user's menu options:
    1 - Request a walker for your dog
    2 - Quit
    """
    print("Would you like to")
    print("1 - Find a walker for your dog")
    print("2 - Quit")
    menu_option = input("Enter your answer here:\n").upper().strip()

    end_section()

    # Validate if the answer is 1 or 2
    while menu_option not in ("1", "2"):
        print("Please choose one of the options:")
        print("1 - Find a walker for your dog")
        print("2 - Register availability to walk other user's dogs")
        menu_option = input("Enter your answer here:\n").upper().strip()

        end_section()

    return menu_option


def return_calendar(user):
    print("Here is your calendar this week:")
    end_section()
    cal = User.get_availability(user)
    for item in cal:
        print("{}: {}".format(item, cal[item]))

    end_section()
    sleep(2)


def request_walker(day_to_book):
    """
    Shows users which walkers are available on the day they want so they can
    choose one to walk their dog
    """

    end_section()

    available_walkers = get_walkers(day_to_book)

    end_section()

    count = 0

    for walker in available_walkers:
        count += 1
        print(count, " - ",
              available_walkers[count-1][0], available_walkers[count-1][1])

    end_section()

    print("Which walker would you like to book?")

    chosen_walker = input("Enter your answer here:\n").upper().strip()

    # Validate an available walker was chosen
    number_of_options = []
    option_count = 0
    for walker in available_walkers:
        option_count += 1
        number_of_options.append(str(option_count))

    while chosen_walker not in number_of_options:
        print(number_of_options)
        print("Please choose one of the options:")
        count = 0
        for walker in available_walkers:
            count += 1
            print(count, " - ",
                  available_walkers[count-1][0], available_walkers[count-1][1])

        end_section()

        print("Which walker would you like to book?")

        chosen_walker = input("Enter your answer here:\n").upper().strip()

    chosen_walker = int(chosen_walker)

    chosen_walker_list = available_walkers[chosen_walker-1]

    return chosen_walker_list


def collect_day():
    """
    Get's the day the user wants to have a walker booked for
    """
    print("Which day would you like to book a walk for?")
    print("1 - Monday")
    print("2 - Tuesday")
    print("3 - Wednesday")
    print("4 - Thursday")
    print("5 - Friday")
    print("6 - Saturday")
    print("7 - Sunday")

    booking_day = input("Enter your answer here:\n").upper().strip()

    # Validate if the answer is 1,2,3,4,5,6,7
    while booking_day not in ("1", "2", "3", "4", "5", "6", "7"):
        print("Please choose one of the options:")
        print("1 - Monday")
        print("2 - Tuesday")
        print("3 - Wednesday")
        print("4 - Thursday")
        print("5 - Friday")
        print("6 - Saturday")
        print("7 - Sunday")

        booking_day = input("Enter your answer here:\n").upper().strip()

        end_section()

    return booking_day


def book_walker(owner_email, walker, day):
    """
    Update the walker and owner's calendars to show booking
    """
    worksheet = SHEET.worksheet('dogs_in_the_hood')

    owner_info = find_row(owner_email, worksheet)
    walker_info = find_row(walker[0], worksheet)

    worksheet.update_cell(owner_info, int(
        day)+4, f"{walker[0]} {walker[1]} booked for walk")
    worksheet.update_cell(walker_info, int(
        day)+4, f"Booked to walk dog {owner_email}")

    print("Great, that's all booked for you. Here is your updated calendar:")


def get_walkers(day):
    """
    Gets the available walkers for the day the user requests
    """
    worksheet = SHEET.worksheet('dogs_in_the_hood')
    if day == "1":
        day = "Mon"
    elif day == "2":
        day = "Tue"
    elif day == "3":
        day = "Wed"
    elif day == "4":
        day = "Thu"
    elif day == "5":
        day = "Fri"
    elif day == "6":
        day = "Sat"
    elif day == "7":
        day = "Sun"

    cell = worksheet.find(day)
    cell_col = cell.col
    col_values = worksheet.col_values(cell_col)
    available_walkers = []
    count = 0

    for entry in col_values:
        count += 1
        if entry == "Available":
            walker_info = worksheet.row_values(count)
            available_walkers.append([walker_info[0], walker_info[1]])
        else:
            continue

    print("Here are the walkers available on", day, ":")

    return available_walkers


# Worksheet functions

def update_worksheet(data):
    """
    Receives a list to be inserted into a worksheet
    Update the registered users worksheet with the data provided
    """
    # Same function as used on the love_sandwiches walk through project
    # by Code Institute
    worksheet_to_update = SHEET.worksheet('dogs_in_the_hood')
    worksheet_to_update.append_row(data)


def find_row(item, worksheet):
    """
    Find the item's row in the specified worksheet
    """
    cell = worksheet.find(item)

    return cell.row


def update_availability(email, availability):
    """
    Update the worksheet with the user's availability
    """
    worksheet_to_update = SHEET.worksheet('dogs_in_the_hood')
    user_entry = find_row(email, worksheet_to_update)
    column = 5
    for day in availability:
        if day == '1':
            worksheet_to_update.update_cell(user_entry, column, "Available")
            column += 1

        elif day == '2':
            worksheet_to_update.update_cell(user_entry, column, "Unavailable")
            column += 1

# Validation functions


def validate_name(name):
    """
    Validate customer name
    Check if the name is at least 1 char long
    """
    try:
        if len(name) < 1:
            raise ValueError(
                "Your name needs to be at least one character long.")

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


def validate_password(password):
    """
    Validate the user's password
    Check if the password is at least 8 characters long
    """
    try:
        if len(password) < 8:
            raise ValueError(
                "Your password needs to be at least eight characters long.")

    except ValueError as e:
        print(f"Incorrect input: {e} Please try again.")
        return False

    return True


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
