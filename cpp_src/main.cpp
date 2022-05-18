//
// Created by mike on 5/6/2022.
//

#include <iostream>
#include "menu.h"

void globalCallback(int option) {
    std::cout << "Global Callback | Selection: " << option << std::endl;
}

void option0() {
    std::cout << "Item Callback | Selected option 0" << std::endl;
}

void option1() {
    std::cout << "Item Callback | Selected option 1" << std::endl;
}

void option2() {
    std::cout << "Item Callback | Selected option 2" << std::endl;
}

// include catch string
// const = constant
// 
int main(int argc, const char * argv[]) {
    
    Menu defaultMenu;
    defaultMenu.addItem("Option 0", &option0);
    defaultMenu.addItem("Option 1", &option1);
    defaultMenu.addItem("Option 2", &option2);
    
    defaultMenu.printMenu();
    
    Menu headerMenu("Select an option");
    headerMenu.addItem("Option 0", &option0);
    headerMenu.addItem("Option 1", &option1);
    headerMenu.addItem("Option 2", &option2);
    
    headerMenu.printMenu();
    
    Menu globalMenu(&globalCallback);
    globalMenu.addItem("Option 0");
    globalMenu.addItem("Option 1", &option1);
    globalMenu.addItem("Option 2");
    
    globalMenu.printMenu();
    
    Menu globalAndHeader("Selection an option:", &globalCallback);
    
    globalAndHeader.addItem("Option 0");
    globalAndHeader.addItem("Option 1", &option1);
    globalAndHeader.addItem("Option 2");
    
    globalAndHeader.printMenu();
    
    return 0;
}