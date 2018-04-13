from socket import *
import subprocess

ip_port = ('127.0.0.1',8080)
back_log = 5
buff_size = 1024

server = socket(AF_INET,SOCK_STREAM)
server.bind(ip_port)
server.listen(back_log)
#连接循环
while True:
    print('等待连接中...')
    conn,addr = server.accept()
    print('已经与客户端建立连接...')
    # print(conn,addr)
    print('客户端信息：',addr)
    # print(addr,type(addr))
    #通信循环
    while True:
        #定义异常处理逻辑
        try:
            cmd = conn.recv(buff_size)
            #当cmd值为空时，定义程序跳出陷入收取消息的死循环的逻辑
            if not cmd:break
            print('【%s】命令开始执行...' %(cmd.decode('utf-8')))
            res = subprocess.Popen(cmd.decode('utf-8'),shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   stdin=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()
            conn.send(cmd_res)
            print('【%s】命令执行完毕，执行结果已发送给客户端' %cmd.decode('utf-8'))
        except Exception as e:
            print(e)
            break
    conn.close()