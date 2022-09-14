# splitting task

length=100
number_of_process=4

for i in range(number_of_process):
    lower=i*length/4
    upper=(i+1)*length/4
    print(lower,upper)

'''
0.0 25.0
25.0 50.0
50.0 75.0
75.0 100.0
'''
