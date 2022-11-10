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
