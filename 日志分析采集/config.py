# -*- coding: UTF-8 -*-
#日志类型
# logType={'mysql':{
#                 'event':'mysqlEvent',
#                 'topic':'mysql'
#                 },
#          'tomcat':{
#                 'event':'tomcatEvent',
#                 'topic':'tomcat'
#                 },
#          'nginx':{
#                 'event':'nginxEvent',
#                 'topic':'nginx'
#                 }
#          };
mail={
    'mail_host':'smtp.qq.com',
    'mail_user':'335935098@qq.com',
    'mail_pass':'ektltsyuheilbgdd'
}
mgconf={'host':'192.168.1.223','port':27017,'dbname':'logs'}

kfk={'host':'192.168.1.223:2181','group':'test-consumer-group','top':{"tomcat": 1,"mysql": 2,"nginx": 3}}

keyword=['error','warn']
