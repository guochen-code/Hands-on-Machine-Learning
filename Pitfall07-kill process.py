'''
The reason is that the child process that is spawned by the os.system call spawns a child process itself. 
As explained in the multiprocessing docs descendant processes of the process will not be terminated – they will simply become orphaned. 
So. p.terminate() kills the process you created, but the OS process (/bin/bash ./test.sh) simply gets assigned to the system's scheduler process and continues executing.

You can kill a process via its pid with the os.kill() function.
The os.kill function takes two arguments, the process identifier (pid) to kill, and the signal to send to kill the process.
The signal is a constant from the signal module, such as signal.SIGINT or signal.SIGKILL.
'''

# kill a process via pid
os.kill(12345, signal.SIGKILL)

# get the pid
pid = process.pid

'''
The SIGINT or signal interrupt can be used to terminate the target process, which is equivalent to the user pressing CONTROL-C on the process. 
Alternately, the SIGKILL or signal kill process can be used to terminate the process forcefully.
The difference between SIGINT and SIGKILL is that it is possible for a process to detect and handle a SIGINT, whereas a SIGKILL cannot be handled.
'''

example:
# example of killing the current process via pid
from os import kill
from os import getpid
from signal import SIGKILL
# get the pid of the current process
pid = getpid()
# report a message
print(f'Running with pid: {pid}')
# attempt to kill the current process
kill(pid, SIGKILL)
# report a message
print('Skill running')

*********************************************************************** LINUX *********************************************************************************
'''
The most common kill signals are:
SIGHUP  1  Hangup
SIGINT  2 Interrupt from keyboard
SIGKILL 9 Kill signal
SIGTERM 15  Termination signal
SIGSTOP 17, 19, 23  Stop the process

kill SIGNAL PID # comman
'''

kill -9 10764

*********************************************************************** exception handling ************************************************************************
import multiprocessing, time, signal
p = multiprocessing.Process(target=time.sleep, args=(1000,))
print(p, p.is_alive())
<Process ... initial> False
p.start()
print(p, p.is_alive())
<Process ... started> True
p.terminate()
time.sleep(0.1)
print(p, p.is_alive())
<Process ... stopped exitcode=-SIGTERM> False
p.exitcode == -signal.SIGTERM                            ##### SIGKILL !!!!!!!!!!!!!!!!!!
True

****************************************************** prcess.terminate() not working in Elastic Beanstalk ********************************************************
****************************************************** prcess.kill() working but create zombie process, still present in the process table ************************
****************************************************** limited entries in the process table, if reach the maximum, cannot create more process *********************

import time
import multiprocessing
from listener import Listener
import os


# if __name__ == '__main__':                                       # problem-0: no need this in linux, otherwise error below. possible reason: root->raw process->parent process(application.py)->child processes. in this case, 
print('****************************************** start **********************************!!!!!')
all_active_process = {}

for opla_job in ['opla-123', 'opla-456', 'opla-789']:
    instance = Listener(opla_job)
    p = multiprocessing.Process(target=instance.get_stream, name=opla_job)
    print('new process created for: ', opla_job)
    p.start()
    all_active_process[opla_job] = p
    print('all active process:', all_active_process)

time.sleep(20)

for opla_job in ['opla-123']:
    all_active_process[opla_job].kill()                       # problem-1: terminate() will not terminate the process, not working. use kill()         
    print(f'{opla_job} terminated !!!! *************')

original_time=time.time()
print('original_time:',original_time)

while True:
    print('main script: running.............')
    time.sleep(2)
    current_time=time.time()
    print('current_time:',current_time)
    print('original_time - current_time',round(current_time-original_time))
    # if round(current_time-original_time) == 10:
    #     all_active_process['opla-456'].terminate()
    #     print('opla-456 terminated !!!! *************')
    # if round(current_time - original_time) == 20:
    #     all_active_process['opla-789'].terminate()
    #     print('opla-789 terminated !!!! *************')
    for process in list(all_active_process.keys()):
        if not all_active_process[process].is_alive():
            print('not live:',all_active_process[process])
            print('os.wait is calling..........')
            os.waitpid(-1,os.WNOHANG)                   # problem-2: can't just wait() and pause the parent process
            print('os.wait is called......')
            del all_active_process[process]
            print('delete:',process)
            print(all_active_process)
    print('all active process:', all_active_process)


    
####################################################################################################################################
Nov 20 19:35:26 ip-172-31-111-151 web: [2022-11-20 19:35:26 +0000] [18762] [INFO] Booting worker with pid: 18762
Nov 20 19:35:26 ip-172-31-111-151 web: Failed to find attribute 'application' in 'application'.
Nov 20 19:35:26 ip-172-31-111-151 web: [2022-11-20 19:35:26 +0000] [18762] [INFO] Worker exiting (pid: 18762)
Nov 20 19:35:26 ip-172-31-111-151 web: [2022-11-20 19:35:26 +0000] [18756] [INFO] Shutting down: Master
Nov 20 19:35:26 ip-172-31-111-151 web: [2022-11-20 19:35:26 +0000] [18756] [INFO] Reason: App failed to load.
Nov 20 19:35:27 ip-172-31-111-151 web: [2022-11-20 19:35:27 +0000] [18771] [INFO] Starting gunicorn 20.1.0
Nov 20 19:35:27 ip-172-31-111-151 web: [2022-11-20 19:35:27 +0000] [18771] [INFO] Listening at: http://127.0.0.1:8000 (18771)
Nov 20 19:35:27 ip-172-31-111-151 web: [2022-11-20 19:35:27 +0000] [18771] [INFO] Using worker: sync
Nov 20 19:35:27 ip-172-31-111-151 web: [2022-11-20 19:35:27 +0000] [18777] [INFO] Booting worker with pid: 18777
Nov 20 19:35:27 ip-172-31-111-151 web: Failed to find attribute 'application' in 'application'.
Nov 20 19:35:27 ip-172-31-111-151 web: [2022-11-20 19:35:27 +0000] [18777] [INFO] Worker exiting (pid: 18777)
####################################################################################################################################
    

Expanding a bit on the good answer you already got, it helps if you understand what Linux-y systems do. They spawn new processes using fork(), which has two good consequences:

All data structures existing in the main program are visible to the child processes. They actually work on copies of the data.
The child processes start executing at the instruction immediately following the fork() in the main program - so any module-level code already executed in the module will not be executed again.
fork() isn't possible in Windows, so on Windows each module is imported anew by each child process. So:

On Windows, no data structures existing in the main program are visible to the child processes; and,
All module-level code is executed in each child process.
So you need to think a bit about which code you want executed only in the main program. The most obvious example is that you want code that creates child processes to run only in the main program - so that should be protected by __name__ == '__main__'. For a subtler example, consider code that builds a gigantic list, which you intend to pass out to worker processes to crawl over. You probably want to protect that too, because there's no point in this case to make each worker process waste RAM and time building their own useless copies of the gigantic list.

Note that it's a Good Idea to use __name__ == "__main__" appropriately even on Linux-y systems, because it makes the intended division of work clearer. Parallel programs can be confusing - every little bit helps ;-)


