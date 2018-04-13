from socket import *
ip_port = ('127.0.0.1',8080)
buffersize = 1024
client = socket(AF_INET,SOCK_STREAM)
client.connect(ip_port)
print('已成功连接服务端')
while True:
    msg = input('>>> ').strip()
    client.send(msg.encode('utf-8'))
    data = client.recv(buffersize)
    print(data.decode(encoding='utf-8'))