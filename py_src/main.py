"""Brain File; Created and Managed by Michael Stolarz; mike@stoladev.com"""

import os


def display_main_menu():
    """Dislays the Main menu."""
    os.system("clear")
    print("TotalQT Automations: Main Menu")


choice = ""

while choice != "q":
    display_main_menu()
    print("1 - Scraper")
    print("2 - Generator")
    print("3 - Seeder")

    choice = input("Which automation would you like to run? ")

    if choice == "1":
        print("")
    if choice == "2":
        print("")
    if choice == "3":
        print("")


def display_scraper_menu():
    """Displays the Scraper menu."""
    print("")


def display_generator_menu():
    """Displays the Generator menu."""
    print("")


def display_seeder_menu():
    """Displays the Seeder menu."""
    print("")
