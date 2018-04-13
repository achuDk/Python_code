import socketserver

buffer_size = 1024

#TCP
class Myserver(socketserver.BaseRequestHandler):
    def handle(self):
        print('连接套接字对象：',self.request)
        print('客户端地址：',self.client_address)
        while True:
            recive = self.request.recv(buffer_size).decode(encoding='utf-8')
            if not recive:break
            print('收到客户端【%s】的消息：%s' %(self.client_address,recive))
            self.request.sendall(recive.upper().encode('utf-8'))

if __name__ == '__main__':
    s = socketserver.ThreadingTCPServer(('127.0.0.1',8080),Myserver)
    s.serve_forever()