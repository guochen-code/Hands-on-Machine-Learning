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
