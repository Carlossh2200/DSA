import random
import matplotlib.pyplot as plt
import time

elapsed_times=[]

def multiplicarMatriz(N):
    listaPrincipal = []
    listaPrincipalMultiplicada = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        listaSecundaria = []  
        for j in range(N):
            listaSecundaria.append(random.randint(0, 50))
        listaPrincipal.append(listaSecundaria)

            
    for i in range(len(listaPrincipal)):
        for j in range(len(listaPrincipalMultiplicada)):
            listaPrincipalMultiplicada[i][j]=(listaPrincipal[i][0]*
                                              listaPrincipal[i][j])
    
    
    print("Matriz Original: ",listaPrincipal, "\n")
    print("Matriz multiplicada",listaPrincipalMultiplicada,"\n")

def main():
    N=1
    for i in range(11):
        start_time=time.time()
        multiplicarMatriz(N)
        time.sleep(.4)
        end_time=time.time()
        elapsed_time=end_time-start_time
        elapsed_times.append(elapsed_time)
        N+=1
    
    plt.plot(range(11),elapsed_times)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Tiempo Transcurrido")
    plt.show()
        

if __name__=="__main__":
    main()
