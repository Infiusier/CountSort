#COUNTSORT
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import sys
sys.setrecursionlimit(10**9)
lista=[]
tamanhos=[30000,40000,50000,60000,70000]
tempos=[]
def geraLista(tamanho):
  x=[]
  for i in range(tamanho): x.append(i)
  random.shuffle(x)
  return x

def geraListaPiorCaso(tamanho):
  x=[]
  for i in range(tamanho,0,-1):
    x.append(i)
  return x

def countingSort(lista):
    now=time.time()
    size = len(lista)
    output = [0] * size
    count = [0] * (size+1)

    for i in range(0, size):
        count[lista[i]] += 1

    for i in range(1, size):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[lista[i]] - 1] = lista[i]
        count[lista[i]] -= 1
        i -= 1

    for i in range(0, size):
        lista[i] = output[i]
    then=time.time()
    return(then-now)

for i in tamanhos:
  #print("comecei")
  #lista=geraLista(i)
  lista=geraListaPiorCaso(i)
  #print("terminei")
  #print("comecei dnv")
  
  tempo=countingSort(lista)
  #print(lista)
  #print("acabei dnv")
  tempos.append(tempo)
# Plot the data
plt.plot(tamanhos,tempos)
print(tempos)
# Show the plot
plt.show()
