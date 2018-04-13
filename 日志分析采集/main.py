# -*- coding: UTF-8 -*-
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from config import *
from pymongo import MongoClient
from message import em
import re


def save1(time,rdd):
    if rdd.isEmpty() is False:
        rddstr =  ' '.join(rdd.collect())
        # strip_control_characters = lambda s: "".join(i for i in s if 31 < ord(i) < 127)
        # text = strip_control_characters(rddstr)
        conn = MongoClient(mgconf['host'], mgconf['port'])
        db = conn[mgconf['dbname']]
        my_set = db.abc
        my_set.insert({'msg':rddstr,'time':str(time)})
        em(mail["mail_host"], mail["mail_user"], mail["mail_pass"]).send('1628359000@qq.com',rddstr)

def finds(word,keyword):
    #查找字符串
    word = word.lower()
    for i in keyword:
        n = word.count(i)
        if n>0:
            return True
            break

if __name__=='__main__':
    sc = SparkContext("local[2]")
    # 处理时间间隔为5s
    ssc = StreamingContext(sc, 5)
    # 打开一个TCP socket 地址 和 端口号
    lines = KafkaUtils.createStream(ssc, kfk['host'], kfk['group'], kfk['top'])
    lines1 = lines.map(lambda x: x[1]).map(lambda s: "".join(i for i in s if 31 < ord(i) < 127)).filter(lambda word: finds(word, keyword))  # 注意 取tuple下的第二个即为接收到的kafka流

    # #对数据进行存储
    lines1.foreachRDD(save1)

    ssc.start()
    ssc.awaitTerminationOrTimeout(90)
    ssc.stop()


