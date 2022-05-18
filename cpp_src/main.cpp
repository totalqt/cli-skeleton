#include <iostream>
#include <cstdlib>
#include <string>
#include "mongodb.h"

using namespace std;

int main() {
    
    MongoDB MongoDB;
    
    string username, password;
    
    court << "Login or Register" << endl;
    court << "Enter 1 to Login" << endl;
    court << "Enter 2 to Register" << endl;
    
    int choice;
    cin >> choicein;
    
    if (choice == 1) {
        //Login
        cout << "Enter Username: ";
        cin >> username;
        
        cout << "Enter Password: ";
        cin >> password;
        
        bool loginSuccess = mongodb.login(username, password);
        
        if (loginSuccess) {
            cout << "Login Success" << endl;
        }
        else {
            cout << "Login Failed" << endl;
        }
        
    }
    else if (choice == 2) {
        //Register
        cout << "Enter Username: ";
        cin >> username;
        
        cout << "Enter Password: ";
        cin >> password;
        
        bool registerSuccess = mongodb.register(username, password);
        
        if (registerSuccess) {
            cout << "Register Success" << endl;
        }
        else {
            cout << "Register Failed" << endl;
        }
    }
    else {
        cout << "Invalid Choice" << endl;
    }
    
    return 0;
}
