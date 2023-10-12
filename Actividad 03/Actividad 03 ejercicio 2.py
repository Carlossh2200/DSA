import random
import matplotlib.pyplot as plt
import time


lista=[]
elapsed_times=[]

def imprime_ultimo(lista):
    print(lista[len(lista)-1])

def main():
    for i in range(1,101):
        lista.append(random.randint(0, 50))
        start_time=time.time()
        imprime_ultimo(lista)
        time.sleep(.2)
        end_time=time.time()
        elapsed_time=end_time-start_time
        elapsed_times.append(elapsed_time)
        print("\n")
    
    plt.plot(range(1,101),elapsed_times)
    plt.xlabel("N")
    plt.ylabel("Tiempo")
    plt.title("Tiempo transcurrido.")
    plt.show()
    
    
if __name__=="__main__":
    main()

