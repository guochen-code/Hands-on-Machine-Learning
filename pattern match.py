import re
r1=r'OPLA-1234*'
r2=r'OPLA-587*'
regex = re.compile("(%s|%s)"%(r1,r2))

matches = re.findall(regex, 'OPLA-504004')

if len(matches) == 0:
    print('create')
    
*******************************************************************************************************************************    
import fnmatch

patterns=['OPLA-587*','OPLA-1234*']

lst=['OPLA-123456','OPLA-123459','OPLA-587321','OPLA-401018','OPLA-104002','OPLA-587111','OPLA-123400']

for opla_job in lst:
    print('....',opla_job)
    demo_job=False
    for pattern in patterns:                                                #### not preferred, because of loop through patterns !!!
        print(pattern,len(fnmatch.filter([opla_job], pattern)))
        if len(fnmatch.filter([opla_job], pattern)) !=0:
            print(fnmatch.filter([opla_job], pattern))
            demo_job = True
    print('demo_job:',demo_job)
    if demo_job is False:
        print(f'!!!{opla_job} - create ....')
    else:
        print(f'!!!{opla_job} - not create......')
