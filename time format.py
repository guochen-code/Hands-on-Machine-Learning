datetime.today().strftime("%Y-%m-%d %H:%M:%S %p %a")
# output 
# '2022-05-30 12:20:39 PM Mon'


datetime.today().strftime("%Y-%m-%d %H:%M:%f %p %a")
# output 
# '2022-05-30 12:20:397326 PM Mon'  ############################### wrong format

datetime.today().strftime("%Y-%m-%d %H:%M:%S %p %A")
# output 
# '2022-05-30 13:01:44 PM Monday'

datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")
# output 
# '2022-05-30 12:22:15.804398'

datetime.today().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
# output 
# '2022-05-30 12:23:04.524'
