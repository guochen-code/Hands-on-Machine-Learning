mport multiprocessing
import threading
import time
import sys


def send():
    while True:
        time.sleep(3)
        print('send to operation chat')


def not_send():
    while True:
        time.sleep(3)
        print('not send to operation chat')


if __name__ == '__main__':
    # now threading1 runs regardless of user input
    threading1 = multiprocessing.Process(target=send)
    threading1.start()

    while True:
        if input() == 'disarm':
            threading1.terminate()
            threading1 = multiprocessing.Process(target=not_send)
            threading1.start()

        if input() == 'arm':
            threading1.terminate()
            threading1 = multiprocessing.Process(target=send)
            threading1.start()
            
**************************************************************************************************************

