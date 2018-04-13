#_*_coding:utf-8_*_
__author__ = 'achuDk'

import os

#项目dir
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#子dir
BIN_DIR = os.path.join(BASE_DIR,'bin')
DATA_DIR = os.path.join(BASE_DIR,'database')
LIB_DIR = os.path.join(BASE_DIR,'lib')
LOG_DIR = os.path.join(BASE_DIR,'log')
MAIN_DIR = os.path.join(BASE_DIR,'main')





if __name__ == '__main__':
    print(BASE_DIR)
    # for i in os.listdir(BASE_DIR):
    #     print(i)
    print(BIN_DIR)
    print(DATA_DIR)
    print(LIB_DIR)
    print(LOG_DIR)
    print(MAIN_DIR)