#ifndef menu_item_h
#define menu_item_h

#include <stdio.h>
#include <string>

class MenuItem {
  
public:
    MenuItem();
    MenuItem(std::string initTitle, int initIndex);
    MenuItem(std::string initTitle, void(*initFuncPtr)(), int initIndex);
    
    std::string getTitle();
    
    int getIndex();
    
    void performCallback();
private:
    std::string title;
    
    int index = 0;
    
    void(*funcPtr)() = nullptr;
};

#endif 
