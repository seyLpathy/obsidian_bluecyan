#include"default.h"
int main(){
    std::string newDog("Persephone");
    std::string oldDog("Satch");
    NamedObject<int> p(newDog,2); 
    NamedObject<int> s(oldDog,36);
    p = s;// compiler can not alter the refrence to other objects
    return 0;
}