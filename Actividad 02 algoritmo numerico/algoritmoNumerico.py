import matplotlib.pyplot as plt
import random
import time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
   
def get_orientation(p, q, r):
    orientation = (q.y-p.y) * (r.x-q.x) - (q.x-p.x) * (r.y-q.y)
    if orientation > 0:
        return 1
    elif orientation <0:
        return -1
    return 0


def compare_orientation(a, b):
    if a != b:
        return 1
    else:
        return 0
   
def plot_points(p1, q1, p2, q2):
    plt.scatter([p1.x, q1.x, p2.x, q2.x], [p1.y, q1.y, p2.y, q2.y], c='red',
                marker='o', label='Points')
    plt.plot([p1.x, q1.x], [p1.y, q1.y], c='blue', label='Segment 1')
    plt.plot([p2.x, q2.x], [p2.y, q2.y], c='green', label='Segment 2')

def numericalAlgorithm():
    LIMITE_N=10
    for i in range(5,LIMITE_N,5):
        print("NUMERO EN i: " , i)
        for j in range(0,i):
            randP1X = random.randint(0,50)
            randP1Y = random.randint(0,50)
            randQ1X = random.randint(0,50)
            randQ1Y = random.randint(0,50)
            randP2X = random.randint(0,50)
            randP2Y = random.randint(0,50)
            randQ2X = random.randint(0,50)
            randQ2Y = random.randint(0,50)
            p1 = Point(randP1X, randP1Y)
            q1 = Point(randQ1X, randQ1Y)
            p2 = Point(randP2X, randP2Y)
            q2 = Point(randQ2X, randQ2Y)
        
            a = get_orientation(p1, q1, p2)
            b = get_orientation(p1, q1, q2)
            c = get_orientation(p2, q2, p1)
            d = get_orientation(p2, q2, q1)
            print("NUMERO EN J: " , j)
            if compare_orientation(a, b) and compare_orientation(c, d):
                print("Hay interseccion")
            else:
                print("Las rectas no coinciden")
        
            
            plot_points(p1, q1, p2, q2)
            plt.legend()
            plt.xlabel('X-axis')
            plt.ylabel('Y-axis')
            plt.grid()
            plt.show()

def main():
    start_time = time.process_time()
    numericalAlgorithm()
    end_time = time.process_time()
    cpu_time=end_time-start_time
    print(f"Tiempo: {cpu_time} segundos")

if __name__ == "__main__":
    main()
