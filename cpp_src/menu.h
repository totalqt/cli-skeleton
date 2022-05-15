#ifndef menu_h
#define menu_h

#include <stdio.h>
#include <vector>
#include "menu_item.h"

class Menu {
    
public:
    Menu();
    Menu(std::string);
    Menu(void(*)(int));
    Menu(std::string, void(*)(int));
    
    void addItem(std::string);
    void addItem(std::string,void(*)());

    
    void printMenu();
    
private:
    
    std::vector<MenuItem*> menuItems;
    
    int count = 0;
    
    std::string header;
    bool hasHeader = false;
    
    void(*globalCallbackPtr)(int) = nullptr;
};

#endif 
