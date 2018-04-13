#_*_coding:utf-8_*_
__auther__ = 'achuDk'

import uuid,hashlib,time

def create_uuid():
    # print(uuid.uuid1(),type(uuid.uuid1()))
    # print(str(uuid.uuid1()),type(str(uuid.uuid1())))
    return str(uuid.uuid1())
def md5():
    m = hashlib.md5()
    # print(m)
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()

if __name__ == '__main__':
    print('test',create_uuid())
    print('test',md5())