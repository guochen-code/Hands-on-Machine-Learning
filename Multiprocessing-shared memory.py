# pass changing values/arrays to child processes from parent process
******************************************************************************************************************************************************
from multiprocessing import Process, Value, Array
import time

class MyClass:
    def __init__(self,opla):
        self.opla=opla
        pass
    def f(self,n):
        print(self.opla) # print(n.value)
        result=n.value*1
        print(result)
active_list=['opla-123','opla-456']
if __name__ == '__main__':
    b=10
    while True:
        b+=1
        num = Value('i', b)
        for opla in active_list:
            c=MyClass(opla)
            p = Process(target=c.f, args=(num,), name=opla)
            p.start()
        time.sleep(6)
        print('---------------------------------------')
        
******************************************************************************************************************************************************
from multiprocessing import Process, Value, Array

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]

if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
    
# will print
'''
3.1415927
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
'''

# My Return
'''
0.0
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

reason: 
When working in interactive environment (i.e with the Notebook), you need to import the functions you want to call with Process or Pool.

In the same folder, create a file utils.py, insert your f function in it, and import it in your notebook with :

from utils import f
Your process should run fine after that.

Whole code :

util.py :

def f(n, a):
    n.value = 3.1415927
    for i in range(len(a)):
        a[i] = -a[i]
your notebook :

from multiprocessing import Process, Value, Array
from utils import f


if __name__ == '__main__':
    num = Value('d', 0.0)
    arr = Array('i', range(10))

    p = Process(target=f, args=(num, arr))
    p.start()
    p.join()

    print(num.value)
    print(arr[:])
