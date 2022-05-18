"""DB Connection File; created and maintained by Michael Stolarz; mike@stoladev.com"""

import os
import bcrypt


def get_database():
    from pymongo import MongoClient
    import pymongo

    # Atlas URL
    CONNECTION_STRING = "mongodb+srv://TotalQT:<password>@cluster0.wk919.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

    # Connection creation
    client = MongoClient(CONNECTION_STRING)

    return client["tqt_automation_data"]


if __name__ == "__main__":
    dbname = get_database()


collection_name = dbname["accounts"]


def create_account(email, first_name, last_name, password):
    """
    Email:
    First Name:
    Last Name:
    Hashed Password:
    Salt:
    """



#
# print("Connecting...")
#
# print("Connected.")
#
# print("Connection failed.")
#
# print("Connection lost.")
