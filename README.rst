*****
PASSMAN
*****

What is Passman?
########

Passman aims to be a simple and secure password manager for the generation, assignment, organization, hashing, and refreshing of passwords for the user. Passman makes use of cryptographic services like salting and hashing when creating credentials for the use.  

How do Passwords Work in Passman?
########

Passman's generations must be:
**********************
* Must be greater than 12 characters
* Nse upper and lower letters, numbers, and symbols
* Update automatically after an interval of time (while also notifying the user)
* Never stored as plaintext

Does Passman use Pass Phrase?
########

Yes, Passman use pass phrases (a series of 6 - 12  words) in order for the associated user to view their environment credentials; while a user password is required to view the generated passwords for the user's accounts.  

What the Passman Process?
########

Passman's process:
**********************

Setup:
**********************
* Prompt user to create credentials for the app.
* Store credentials as environment variables, then hash part of the credentials. 

Use:
**********************
* Prompt for purpose of to-be-generated-password (gmail, home computer, school email, gaming account, etc.)
* Generated password for account is cryptographically treated and then stored as an object.
* From the list of generated passwords, users can then update their accounts accordingly (based on the settings of the external account). 
* After an interval of time, passwords are updated. The user can choose the update intervals. 