import time
a=[]
def looping01():
    for i in range(1,10):
        a.append(i)
    print(a)

t=time.perf_counter()

# t=time.perf_counter()-t
print ("Calculation time "+str(t)+" seconds")
if __name__ == '__main__':
  '''
  Main block
  '''
  looping01()
  # call the looping function
  