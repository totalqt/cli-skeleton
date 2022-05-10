#include "menu.h"
#include <stdio.h>
#include <iostream>

Menu::Menu() {

}

Menu::Menu(std::string initHeader) {
    
    hasHeader = true;
    header = initHeader;
    
}

Menu::Menu(std::string initHeader, void (*initCallback)(int)) {
    
    hasHeader = true;
    header = initHeader;
    
    globalCallbackPtr = initCallback;
    
}

Menu::Menu(void (*initCallback)(int)) {
    
    globalCallbackPtr = initCallback;
    
}

void Menu::addItem(std::string title) {
    menuItems.push_back(new MenuItem(title, count));
    
    count++;
}

void Menu::addItem(std::string title,void(*funcPtr)()) {
    menuItems.push_back(new MenuItem(title, funcPtr, count));
    count++;
}


void Menu::printMenu() {
    
    int option = 0;
    
    if (hasHeader) std::cout << header << "\n" << std::endl;
    
    for (int i = 0; i < menuItems.size(); i++) std::cout << i << ".) " << menuItems[i]->getTitle() << std::endl;

    
    std::cout << "\nSelect option: ";
    std::cin >> option;
    
    if (option < 0 && option >= menuItems.size()) {
        std::cout << "Not a valid selection.  Please try again." << std::endl;
        printMenu();
    } else {
        menuItems[option]->performCallback();
        
        if (globalCallbackPtr != nullptr) globalCallbackPtr(option);
    }
    
}
