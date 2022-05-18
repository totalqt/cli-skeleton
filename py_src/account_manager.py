"""Account manager"""

import os
import sys
import bcrypt, getpass


def start_login():
    """Starts the login process."""
    # Ask user for username and password.
    # Verify with mongodb.
    # Start population of user's data.


def start_registration():
    """Starts the registration process.
    Email:
    First Name:
    Last Name:
    Password:
    """

    email = input("\nPlease enter an email: ")
    first_name = input("\nPlease enter a first name: ")
    last_name = input("\nPlease enter a last name: ")
    password = input("\nPlease enter a password: ")
    password_confirmed = input("\nPlease re-enter your new password: ")

    # Gen secure password using getpass. Gen salt. Gen hashed password.
    password = getpass.getpass()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)



def start_recovery():
    """Starts the recovery process."""
    # Ask user for username or email.
    # Send a recovery email to the user containing 6 random digits.
    # Ask user for digits sent to email.
    # If correct, allow user to set a new password.
