be careful with the variable name used in for loop. 
Unintentional consequences will be caused: 
source: job-2 # start a new job, so
opla_job = 'job-2'
all_active_process ={'job-1': <process>}
current_active_list_600=['job-1','job-2']
len(long_list) == 600: check
for opla_job in list(all_active_process.keys()):                ###### opla_job is now tunred to be 'job-1'
    if opla_job not in current_active_list_600:                 ###### still streaming so code will not continue, but opla_job is changed
        all_active_process[opla_job].terminate()
        del all_active_process[opla_job]
when go through below:        
if opla_job not in list(all_active_process.keys()):               ###### this opla_job is 'job-1', so will never create a new process for job-2
    print('all_active_process:',all_active_process)
    print('current_active_list_600',current_active_list_600) 
*********************************************************************************************************************************************************
for message in Consumer:
    opla_job = message.value['oplaJobNumber']                          ###### this will be unintentionally replaced, see below
    if opla_job not in demon_jobs:
        # print('opla job number:', opla_job)                       
        long_list.append(opla_job)
        while len(long_list) > 600:
            long_list.pop(0)
        # check and terminate job that is no long streaming
        if len(long_list) == 600:
            current_active_list_600 = list(set(long_list))
            for oname in list(all_active_process.keys()):                ###### oname, can't be opla_job. otherwise will replace 
                if oname not in current_active_list_600:
                    all_active_process[oname].terminate()
                    del all_active_process[oname]
        # create new process for new job
        if opla_job not in list(all_active_process.keys()):               ###### this will be the right one you want to use, so never start a new job
            print('all_active_process:',all_active_process)
            print('current_active_list_600',current_active_list_600)
            instance = Listener(opla_job)
            p = multiprocessing.Process(target=instance.get_stream, name=opla_job)
            print('new process created for: ', opla_job)
            p.start()
            all_active_process[opla_job] = p
