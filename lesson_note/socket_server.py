import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',8080))
server.listen(5)
print('------->')
conn,addr = server.accept()
print('conn:',conn,'\n','addr:',addr)
msg = conn.recv(1024)
print('接收到msg:',msg)
conn.send(msg.upper())

conn.close()
server.close()
