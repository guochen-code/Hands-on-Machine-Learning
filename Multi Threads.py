'''
Q:
I have a Class File. I created two threads A and B. In A and B, each thread, I create an auto varible File myfile. 
And then A and B will operate it. Is that secure? Will it lead to the inconsistent of data?

A:
From the pure memory ressource perspective, it will depend on the scope of your File variables :
-If they are local function variables, you are good to go. Each thread of execution owns it own stack, totally separate from other threads, 
where it create local variables.
-If they are static, you are referring to the same global address.
From the file access perspective, it will depends if it is the same file, and if you are writing to it or not.
'''

import threading
from random import random


def shooter(name, shoot_times):
    count = 0
    for i in range(shoot_times):
        x_random = random()
        y_random = random()
        if (x_random ** 2 + y_random ** 2) <= 1:
            count += 1
    print(f'this is count from {name}:', count)

shoot_times = 100
p1 = threading.Thread(target=shooter, args=('opla-111', shoot_times,))
p2 = threading.Thread(target=shooter, args=('opla-222', shoot_times,))
p1.start()
p2.start()
p1.join()
p2.join()
print('end')

'''
this is count from opla-111: 76
this is count from opla-222: 80
end
'''
'''
this is count from opla-111: 70
this is count from opla-222: 78
end
'''
