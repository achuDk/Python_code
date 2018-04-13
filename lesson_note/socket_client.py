import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',8080))

data = input('请输入要发送的信息>>> ')
client.send(data.encode('utf-8'))
msg = client.recv(1024)
print('收到的信息内容：',msg)

client.close()