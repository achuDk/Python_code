from socket import *
import time

ip_port = ('127.0.0.1',8080)
buff_size = 1024
time_format = '%Y-%m-%d_%X'

client = socket(AF_INET,SOCK_STREAM)
client.connect(ip_port)
print('已成功连接服务端')
#通信循环
while True:
    cmd = input('请输入要执行的命令>>> ').strip()
    #避免当cmd值为空时，会报错
    if not cmd:continue
    #定义退出命令为quit
    if cmd == 'quit':break
    client.send(cmd.encode('utf-8'))
    print('命令执行的时间为：' ,time.strftime(time_format))
    cmd_res = client.recv(buff_size)
    print(cmd_res.decode('gbk'))
client.close()