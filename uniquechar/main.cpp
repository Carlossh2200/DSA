#include <iostream>
#include <set>
#include <string>

using namespace std;


bool areAllAsciiCharactersUnique(std::string str) {
    set<char> val;
    for(int i=0;i<str.length();i++){
        if (val.find(str[i]) != val.end()){
            return false;
        }
        else{
          val.insert(str[i]);
        }
    }
    return true;
}

int main(){
    if (areAllAsciiCharactersUnique("Hola")){
        std::cout << "true";
        }
    else{
        std::cout << "false";
    }
}
