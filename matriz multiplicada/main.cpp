#include <iostream>

using namespace std;

int main()
{
    int matriz[3][3];
    int matrizTwo[3][3];
    matriz[0][0]=1;
    matriz[0][1]=2;
    matriz[0][2]=3;
    matriz[1][0]=4;
    matriz[1][1]=5;
    matriz[1][2]=6;
    matriz[2][0]=7;
    matriz[2][1]=8;
    matriz[2][2]=9;

    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            matrizTwo[i][j] = matriz[i][j]*matriz[i][j];
        }
    }

    for(int i=0;i<3;i++){

        cout << "\n";
        for(int j=0;j<3;j++){
            cout << matrizTwo[i][j] << "\t";
        }
    }
    return 0;
}
