import random
import matplotlib.pyplot as plt
import time


lista=[]
elapsed_times=[]

def imprimir_lista(lista):
    for i in lista:
        print(i)
    print("\n")
    
def main():
    for i in range(1,101):
        lista.append(random.randint(0, 50))
        
        start_time = time.time()
        imprimir_lista(lista)
        time.sleep(.2)
        end_time = time.time()
        
        elapsed_time = end_time-start_time
        elapsed_times.append(elapsed_time)
        print("\n")
    
    plt.plot(range(1,101),elapsed_times)
    plt.xlabel("Iteracion")
    plt.ylabel("Tiempo (s)")
    plt.title('Tiempo transcurrido')
    plt.show()
    
   


    
if __name__=="__main__":
    main()
