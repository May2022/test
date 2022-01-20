import numpy as np
import matplotlib.pyplot as plt
def readFile(filename):
  x,y=np.loadtxt(filename,usecols=(0,1), unpack=True, dtype=float,comments='#',delimiter=',')
  return(x,y)

filename="./data/Wiggle1.txt"
x,y=readFile(filename)
plt.plot(x,y)
