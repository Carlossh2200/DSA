//Avila Sanchez Carlos Humberto
//Ruiz Hernandez Oscar Alejandro
//Sandoval Huerta Carlos Arturo
//D01 Analisis de algoritmos

#include <iostream>
#include <time.h>
#include <math.h>
#include <chrono>

using namespace std;

void llenarArreglo(int tamanioArreglo,int arreglo[]){
    srand((unsigned)time(0));
    int aleatorio;
    for(int i=0;i<tamanioArreglo;i++){
        aleatorio=rand();
        arreglo[i]=aleatorio;
    }
}

void selectionSort(int tamanioArreglo,int arreglo[]){
    int i,j,menor;
    for(i=0;i<tamanioArreglo-1;++i){
    menor=i;
        for(j=i+1;j<tamanioArreglo;++j){
            if (arreglo[j]<arreglo[menor]){
                menor=j;
            }
        }
        int aux=arreglo[i];
        arreglo[i]=arreglo[menor];
        arreglo[menor]=aux;
    }
}



int main()
{
    int tamanioArreglo;
    for(int i=5;i<=1000;i+=50){
        tamanioArreglo=i;
        int arreglo[tamanioArreglo];
        llenarArreglo(tamanioArreglo,arreglo);
        auto startTime = std::chrono::high_resolution_clock::now();
        selectionSort(tamanioArreglo,arreglo);
        for(int i=0;i<tamanioArreglo;i++){
        cout << endl << endl << arreglo[i] << " ";
        }
        auto endTime = std::chrono::high_resolution_clock::now();
        auto duracion = std::chrono::duration_cast<std::chrono::microseconds>
        (endTime - startTime).count();
        std::cout << "Duracion: " << duracion << "\n";
        cout << "Presiona enter" << endl;
        cin.get();
    }
    return 0;
}
