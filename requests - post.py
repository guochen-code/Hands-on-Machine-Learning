# try two times
try:
  requests.adapters.DEFAULT_RETRIES = 2
  response = requests.post(url,data=body,headers=headers,timeout=5)
except Exception as ee:
  LOGGER.error(ee)
  
'''
前面配置的 “timeout=5” ，这个值是作为 connect 和 read 二者共用的 timeout ，

connect 连接超时
指的是客户端实现到远端服务器端口的连接时 request 所等待的时间。
连接超时一般设为比 3 的倍数略大的一个数值，因为 TCP 数据包重传窗口的默认大小是 3。

read 读取超时
指的客户端已经连接上服务器并且发送了 request 后，客户端等待服务器发送请求的时间。
一般指的是服务器发送第一个字节之前的时间。

元组配置方式，比如：

response = requests.post(url, data = body, headers = http_headers, timeout=(3, 1) )

元组 timeout=(3, 1) 内第一个值为连接超时时间，第二个值为读取超时时间
'''
