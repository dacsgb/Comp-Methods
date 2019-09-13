import random
import matplotlib.pyplot as plt

def Collatz(n):
    if n == 1:
        n = n
    elif n % 2 == 0:
        n = n/2
    elif n % 2 == 1:
        n = 3*n + 1
    return n

def iterate():
    n = random.randint(2**10,2**16)
    x = [n]
    while n != 1:
        n = Collatz(n)
        x.append(n)
    return x
    
def graph(x):
    fig, ax = plt.subplots()
    ax.plot(x,'o-')
    ax.set(xlabel='Iteration', ylabel='Value', title='Collatz Conjecture Graph')
    ax.grid()
    plt.show()  

if __name__ == "__main__":
    series = iterate()
    print("The value",series[0],"converged in",len(series),"steps")
    graph(series)