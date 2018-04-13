import pymysql

host = "loaclhost"
port = 3306
user = root
passwd = ""

# 创建连接对象
conn = pymysql.connect(host,port,user,passwd)

# 创建游标对象
cursor = pymysql.cursors

# 编辑要执行的 SQL 语句
sql = "create table user(id int PRIMARY KEY ,user VARCHAR(30) NOT NULL ,passwd )"