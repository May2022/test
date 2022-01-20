import time
import numpy as np
def bubbleSort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

t=time.perf_counter()
t=time.perf_counter()-t
data=np.random.random((10))
print(bubbleSort(data))
print ("Calculation time "+str(t)+" seconds")