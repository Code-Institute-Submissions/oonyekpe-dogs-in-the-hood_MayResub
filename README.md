# Dogs-in-the-hood

![image](https://user-images.githubusercontent.com/68662449/163656132-b9347d81-103d-4c75-a8a1-5749e4b7ee7d.png)
Dogs-in-the-hood website is an app to connect dog walkers and dog owners in the neighbourhood, so that people can coordinate dog walking.

Deployed url: https://dogs-in-the-hood.herokuapp.com/

## Author

Obiageli Onyekpe



## How to Use

The first thing you need to do when using this app is choosing if you want to log in or create a new account.



## Features

### Implemented Features


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
