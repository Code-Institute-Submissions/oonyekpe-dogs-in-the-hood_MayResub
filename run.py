import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('dogs_in_the_hood')

def register_walker():
    """
    Make an account for a new dog walker
    """
    print("Please create a dog walker account to continue \n")
    user_first_name = input("Please enter your first name: ")
    user_last_name = input("Please enter your last name: ")
    user_email_address = input("Please enter your email address: ")
    user_password = input("Please create a password: ")
    print("\n You have now registered as a dog walker, {} {}".format(user_first_name, user_last_name))

register_walker()