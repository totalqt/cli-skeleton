#include "menu_item.h"

MenuItem::MenuItem() {
    title = "Undefined";
}

MenuItem::MenuItem(std::string initTitle, int initIndex) {
    title = initTitle;
    
    index = initIndex;
}

MenuItem::MenuItem(std::string initTitle, void(*initFuncPtr)(), int initIndex) {
    title = initTitle;
    
    funcPtr = initFuncPtr;
    
    index = initIndex;
}

int MenuItem::getIndex() {
    return index;
}

std::string MenuItem::getTitle() {
    return title;
}

void MenuItem::performCallback() {
    if (funcPtr != nullptr) funcPtr();
}
