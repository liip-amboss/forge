# Apps

## Accounts
The account app is used to mange the users inside of django.
To login you can use the simplejwt api. 

### User
The default user model is overwritten to disable the username and enable the
user to login with email only.

### EmailUserManager
We also overwrite the default user manager, so we can easily create users with
email instead of username.
