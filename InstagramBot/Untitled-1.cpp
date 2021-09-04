#include <iostream>
using namespace std;
int ustAl(int taban, int kuvvet){
    if (kuvvet > 1) 
        taban *= ustAl(taban, kuvvet - 1);
    return taban;
}
int main(){
    cout << ustAl(2, 5);
    system("pause");
}