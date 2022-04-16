# Project 3 Python Essentials: Dogs-in-the-hood

![image](https://user-images.githubusercontent.com/68662449/163656132-b9347d81-103d-4c75-a8a1-5749e4b7ee7d.png)

Dogs-in-the-hood is an online app to connect dog owners and dog walkers in the same neighbourhood. It is for people in the community to easily find and coordinate to meet dog walking demands. The app contains a function that allows users to either log-in or create a new account to use the app. The app is supported by a Google sheet behind the scence, that is populated with the information entered by users when they register and use the app.

Deployed url: https://dogs-in-the-hood.herokuapp.com/

## Author

Obiageli Onyekpe


## How to Use

To start, users are presented with a short introduction and can either log-in as already signed-up users or they can create a new account. For ease, users are requested to type in  1 (then the ENTER key) or 2 ( then the ENTER key) to make their selection.

To log-in, users are requested to type in their email address.
To create an account, users are requested to type in their first and last names, their email address, and a password. The screenshots demonstrating these steps on the app site are shown below:

![image](https://user-images.githubusercontent.com/68662449/163658072-34d5281f-cfd0-4b2f-b975-143ae7001ab4.png)




![image](https://user-images.githubusercontent.com/68662449/163658238-0d4f17c1-b070-487b-bebe-c05c4db54436.png)


![image](https://user-images.githubusercontent.com/68662449/163658442-9211f3d6-cb1a-4e70-94b6-bc7b3859f372.png)


Once a new account is successfully created, the user is presented with clear instructions to input their availability for the week, as evidenced in the screenshot below: 

![image](https://user-images.githubusercontent.com/68662449/163662410-db485e94-38ae-4d56-97c8-7bfdcfc40e3e.png)



Next step, the new user is presented with the option 1 - Select a dog walker or option 2 - Quit the app:

![image](https://user-images.githubusercontent.com/68662449/163658789-5115418d-ed04-401e-a27d-9ef36b3b08fc.png)

If the user selects option 1, they are then presented with the option to indicate what day of the week (Monday - Sunday) by corresponding numbers 1,2,3,4,5,6,7, as seen in the screenshot below:

![image](https://user-images.githubusercontent.com/68662449/163658983-04f5e6fc-4f39-4816-b6a8-8307f5315b9d.png)


On entering their selected day, users are presented with a list of available walkers for their selected day, as shown below:

![image](https://user-images.githubusercontent.com/68662449/163659111-ed26082a-f773-4d40-afbe-34eee0290116.png)


Once they enter which dog walker they would like on the day, they receive a confirmation wihtin seconds, together with an update of their calendar showing their confirmed bookings and outstanding availability. See screenshot demonstrating these below:

![image](https://user-images.githubusercontent.com/68662449/163659220-b9fb1996-3213-4f80-bbd8-7b068a558e21.png)


In the above screenshot, it shows that after the update, users are presented again with two new options. Option 1 is to find a dog walker again and option 2 is to quit the app.
If the users select to quit the app at this point, they receive a 'Thank you and goodbye' message, as shown in the screenshot below:


![image](https://user-images.githubusercontent.com/68662449/163659338-ace80f5b-8321-48d3-ad25-370c7fe4b4d7.png)





## Features

### Implemented Features

#### User
* Log in and create an account

![image](https://user-images.githubusercontent.com/68662449/163659948-c1cbf993-f049-485f-a0e5-81d90541658b.png)

- Display app name and short description
- Display questions asking if user wants to log-in or create a new account.

* Log in (collect and verify email)

![image](https://user-images.githubusercontent.com/68662449/163660233-f5945ec0-8118-46e6-bd6f-01570869be09.png)

- Good to have you back message
- Collect user's email address
- Validate user's email address

* Create an account

![image](https://user-images.githubusercontent.com/68662449/163660315-41e54a98-02e0-4247-b785-3954f4b9fecc.png)

- Request for user's first and last names
- Request for user's email address and validate the email address
- Check if email is not already in use
- Request user to enter password
- New data automated to input into linked Google sheet

* Collect user's avaliability and display in week's calendar

![image](https://user-images.githubusercontent.com/68662449/163660529-dab4b5ce-f558-4581-a722-2cf299dc605b.png)

- Users to indicate by selecting each day of the week they are available by was of numbers for each day of the week:

![image](https://user-images.githubusercontent.com/68662449/163660593-be786953-dd6b-4ff3-93a8-22bbf1e512e9.png)


- User receives personalised message showing their availability for the week:

![image](https://user-images.githubusercontent.com/68662449/163660664-7fa6e3ee-1770-4f8f-b71d-26938d7072ef.png)


* Offer user option to book a dog walk for their pet, or quit the app:

![image](https://user-images.githubusercontent.com/68662449/163660765-88441522-891e-4ad2-934e-bcfe870cdd58.png)

* User presented with a list of days to choose from in the week, and then a list of people available to walk their dog on the selected day:

![image](https://user-images.githubusercontent.com/68662449/163660907-03be46e4-4696-4b60-8b43-d3a25303290a.png)

* User receives confirmation of all their selected bookings and the remainder availability they still have for the week:

![image](https://user-images.githubusercontent.com/68662449/163661161-fe5163d8-4d70-4e9b-94e9-4155eaace256.png)

* QUIT app

![image](https://user-images.githubusercontent.com/68662449/163661205-8aa3207e-617c-4cd4-b042-c11942376a77.png)

- QUIT option 2 presented to user after confirmation of their bookings and calendar update.
- Selecting the Quit option returns the message 'Thank you for using dogs-in-the-hood. Goodbye!'.

* SPECIAL FEATURE
- With mentor Malia's guidance, found code with special feature to prevent the app accepting double bookings!

![image](https://user-images.githubusercontent.com/68662449/163661635-5e75619d-cd6d-43b9-9464-6641fd1c1f43.png)

- For example, in the above screenshot, user Emma was unable to book a dog walk for Monday as she was already booked. The message: " You will have to email Joe Jonas to cancel" was returned with an update of Emma's calendar for the week.


### Future Features
- **Manage Availability** was dropped from this project as I didn't have time to work out the logic.  If given more time, manage availability would have been a 2nd option on the main menu and quit would be 3rd. Users would be able to set the days they were available to walk dogs. So that the spreadsheet owner would not have to manage that functionality.

## Design Documents

I made an original project plan as seen in this flow chart, but it turned out to be really complicated and needed far more time than I had, so I scaled back and adjusted to scale as I coded.

![image](https://user-images.githubusercontent.com/68662449/163657194-a1d0eb32-8101-403b-8415-2ae40541a612.png)


## Data Model

## Google Sheet
![image](https://user-images.githubusercontent.com/68662449/163656457-6bc38e8d-fabd-457a-aab8-7677b4ea05fa.png)

When a user is registered their information is automatically enetred here etc


## Libraries Used

* cachetools

    - Extensible memoizing collections and decorators

* dnspython

    - It is a DNS toolkit for Python. It supports almost all record types. It can be used for queries, zone transfers, and dynamic updates. It supports TSIG authenticated messages and EDNS0.

* email-validator

    - This library validates that a string is of the form name@example.com.

* google-auth

     - This library simplifies using Google’s various server-to-server authentication mechanisms to access Google APIs.

* google-auth-oauthlib

    - This library provides oauthlib integration with google-auth.

* gspread

     - Interface for working with Google Sheets.

* oauthlib

    - A generic, spec-compliant, thorough implementation of the OAuth request-signing logic for Python 3.6+.

* pyasn1

    - Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)

* pyasn1-modules

    - A collection of ASN.1 modules expressed in form of pyasn1 classes. Includes protocols PDUs definition (SNMP, LDAP etc.) and various data structures (X.509, PKCS etc.).

* requests-oauthlib

    - Provides first-class OAuth library support for Requests.

* rsa

    - It supports encryption and decryption, signing and verifying signatures, and key generation according to PKCS#1 version 1.5.


## Testing

### Validation Testing

* PEP 8
        
    - I used `# noqa` to avoid flake8 errors around lines too long where I couldn't rearrange the code to make it work. 
    - I also had to remove some extra spaces and the unused datetime import.
    ![PEP8 all ok](https://user-images.githubusercontent.com/68662449/163655398-b5dee422-e198-4021-8c4d-e82b5dd8bdf3.PNG)


### Manual Testing



### Bugs

* issues with bookings - fixed; double bookings; highlight the bugs and struggles (3-5 examples)

### Unifxed Bugs

* No bugs remaining

## Deployment

This application will be deployed via [Heroku](https://heroku.com)

1. Log into Heroku.

2. Navigate to Dashboard. 

3. Click "New" and select "create new app" from the drop-down menu. This is found in the upper right portion of the window. Provide a name for your application, this needs to be unique, and select your region.

![Heroku step1](https://user-images.githubusercontent.com/68662449/163655564-83cb284c-310c-41c7-a13d-fe0f77bd14ad.PNG)

4. Click "Create App".

5.	Navigate to "Settings" and scroll down to "config vars".
6. Click "Reveal Config Var", in the field key I entered the CREDS word and in the value field I copied my creds.json content as past there.

![Heroku step2-config vars](https://user-images.githubusercontent.com/68662449/163655613-9aa8edaf-b1fe-43ed-a771-0a373ba4c3ad.PNG)

7. Then scroll down to "build packs", click "build packs" and then click both "python" and "node.js"(node.js is needed for the mock terminal.)
![Heroku step3 - buildpacks](https://user-images.githubusercontent.com/68662449/163655690-10a1a530-46ef-4d8d-a097-f27ba6cecfae.PNG)

8. Navigate to the "Deploy" section.

9. Scroll down to "Deployment Method" and select "GitHub".
![Heroku step4 - connect to github](https://user-images.githubusercontent.com/68662449/163655804-a9fb7b7c-ab21-4aaa-8b4d-e590f716b644.PNG)


10. Authorise the connection of Heroku to GitHub.

11. Search for your GitHub repository name, and select the correct repository.

12. For Deployment there are two options, Automatic Deployments or Manual, I chose Automatic Deployment so Heroku will re-build each time code is pushed to GitHub.

13. Ensure the correct branch is selected "master/Main", and select the deployment method that you desire.
![Heroku step5 - automatic deployment to github](https://user-images.githubusercontent.com/68662449/163655875-bf2e764b-15a5-41c1-a7a2-521184e5f8f6.PNG)


## Credits

### Acknowledgments

* Code Institute: Love Sandwiches Project
    
    - Deployment terminal

    - Function update_worksheet

    - Steps to declare and connect the API to my worksheet

* Coder's Bistro programme by Arthur Henrique El Mezaonik Martins

    - Used deployment section for the read.me
    - Used for libraries included section.

* Malia Havlicek: Reviewing and giving suggestions how to improve my project.
