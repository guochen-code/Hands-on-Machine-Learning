'''
Total shoot times = 100,000,000		

	multithreading		multiprocessing		Normal
      1	7856535		7854614		
      2	7853773		7856018		
      3	7854919		7853573		
      4	7853540		7854644		
      5	7854876		7856011		
      6	7855493		7853409		
      7	7854673		7852215		
      8	7855551		7854355		
      9	7853120		7852075		
      10 7854303	7853755		
sum	      78546783		78540669		
pi	    3.14187132		3.14162676		3.1415028
time	  54.31396544		13.25850404		51.81063664
'''
'''
Total shoot times = 1,000,000,000	
78537656
78533465
78537633
78543401
78538508
78538447
78533752
78535067
78535282
78537763
sum 785370974
pi 3.141483896
time 133.0128756
# time increased 10 times. but max accuract not improved. maybe average accuracy improved.
'''

from random import random
import time
import multiprocessing
import threading

def shooter(shoot_times):
    count=0
    for i in range(shoot_times):
        x_random=random()
        y_random=random()
        if (x_random**2+y_random**2) <= 1:
            count+=1
    return count

shoot_times=100000000
start=time.perf_counter()
count=shooter(shoot_times)
pi=4*count/shoot_times
print(pi)
end=time.perf_counter()
print(end - start)
