"""Menu manager"""

import os
import sys

import account_manager as account

def display_login_menu():
    """Dislays the Login menu."""
    os.system("clear")
    print("\nLogin Menu\n")

    login_menu_choice = ""

    while login_menu_choice != "q":
        print("1 - Login")
        print("2 - Register")
        print("3 - Recover")

        login_menu_choice = input("\nWhich choice? ")

        if login_menu_choice == "1":
            account.start_login()
        elif login_menu_choice == "2":
            account.start_registration()
        elif login_menu_choice == "3":
            account.start_recovery()
        elif login_menu_choice == "q":
            sys.exit()
        else:
            print("\nInvalid choice. Please try again.")


def display_main_menu():
    """Dislays the Main menu."""
    os.system("clear")
    print("\nTotalQT Automations: Main Menu\n")


def display_scraper_menu():
    """Displays the Scraper menu."""
    print("\n")


def display_generator_menu():
    """Displays the Generator menu."""
    print("\n")


def display_seeder_menu():
    """Displays the Seeder menu."""
    print("\n")
