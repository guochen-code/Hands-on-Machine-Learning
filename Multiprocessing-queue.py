************************************************************************************************************************************************************

                                            multiple consumers/child processes and one producer/parent process

************************************************************************************************************************************************************

from multiprocessing import Process, Queue
import time
import sys
import random


def reader_proc(queue,name):
    ## Read from the queue; this will be spawned as a separate Process
    while True:
        msg = queue.get()         # Read from the queue and do nothing
        print(f'name {name}:',msg)
        if (msg == 'DONE'):
            break

# def writer(queue):
#     ## Write to the queue
#     i=0
#     while True:
#         time.sleep(1)
#         i+=1
#         queue.put(i)             # Write 'count' numbers into the queue
#         queue.put(i)
#         queue.put(i)


if __name__=='__main__':
    pqueue1 = Queue() # writer() writes to pqueue from _this_ process
    pqueue2 = Queue() # writer() writes to pqueue from _this_ process
    pqueue3 = Queue() # writer() writes to pqueue from _this_ process

    q_lst={'111':pqueue1,'222':pqueue2,'333':pqueue3}

    ### reader_proc() reads from pqueue as a separate process
    reader_p1 = Process(target=reader_proc, args=((pqueue1),'opla-111')).start()
    reader_p2 = Process(target=reader_proc, args=((pqueue2),'opla-222')).start()
    reader_p3 = Process(target=reader_proc, args=((pqueue3),'opla-333')).start()

    name_lst=['111','222','333']
    while True:
        time.sleep(1)
        message = {'id': random.choice(name_lst), 'value': random.random()}
        print('generated message:',message)
        for i in q_lst.keys():
            if message['id'] == i:
                q_lst[i].put(message)


**************************************************** auto scale ****************************************************
from multiprocessing import Process, Queue
import time
import sys
import random


def reader_proc(queue,name):
    ## Read from the queue; this will be spawned as a separate Process
    while True:
        msg = queue.get()         # Read from the queue and do nothing
        print(f'name {name}:',msg)
        if (msg == 'DONE'):
            break

if __name__=='__main__':
    name_lst=['111','222','333','444','555','666']
    all_active_process={}
    all_active_queue={}
    while True:
        time.sleep(1)
        message = {'id': random.choice(name_lst), 'value': random.random()}
        print('generated message:',message)

        if message['id'] not in all_active_process.keys():
            all_active_queue[message['id']]=Queue()
            all_active_process[message['id']] = Process(target=reader_proc, args=((all_active_queue[message['id']]), message['id']))
            all_active_process[message['id']].start()

        for i in all_active_queue.keys():
            if message['id'] == i:
                all_active_queue[i].put(message)
'''
generated message: {'id': '222', 'value': 0.8496754167881175}
name 222: {'id': '222', 'value': 0.8496754167881175}
generated message: {'id': '555', 'value': 0.6130036145157562}
name 555: {'id': '555', 'value': 0.6130036145157562}
generated message: {'id': '444', 'value': 0.7538112166666542}
name 444: {'id': '444', 'value': 0.7538112166666542}
generated message: {'id': '444', 'value': 0.719968479151165}
name 444: {'id': '444', 'value': 0.719968479151165}
generated message: {'id': '222', 'value': 0.9858231576376857}
name 222: {'id': '222', 'value': 0.9858231576376857}
generated message: {'id': '111', 'value': 0.05165566336301364}
name 111: {'id': '111', 'value': 0.05165566336301364}
'''
