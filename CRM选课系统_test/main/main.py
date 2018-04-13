#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "achuDk"
# Date: 2017/12/15

import pickle,os

class Base:
    def obj_detail(self):
        print('%s %s 的详细信息：%s' %(type(self),self.__dict__['name'],self.__dict__))
    def __str__(self):
        return self.name
    def save(self,file_name):
        upstair_dir = os.path.join(os.path.dirname(os.getcwd()),'database',str(type(self).__name__))
        dirs = os.path.join(os.path.dirname(os.getcwd()),'database',str(type(self).__name__),file_name)
        # print(upstair_dir)
        # print(dirs)
        os.makedirs(upstair_dir,exist_ok='ok')
        pickle.dump(self,open(dirs,'wb'))
    @classmethod
    def get_all_obj(self):
        ret = []
        dira = os.path.join(os.path.dirname(os.getcwd()), 'database', self.__name__)
        print(dira,type(dira))
        for i in os.listdir(dira):
            print(i)
            ret.append(i)

class School(Base):
    i = 0
    def __init__(self,name,addr,type):
        # print(type(self))
        self.name = name
        self.addr = addr
        self.type = type
        School.save(self,self.name+'.log')
        School.i += 1
    def detail(self):
        super().obj_detail()

School.get_all_obj()


class Course(Base):
    i = 0
    def __init__(self,name,price,period,school_obj):
        self.name = name
        self.price = price
        self.period = period
        self.school = school_obj
        School.save(self,self.name+'.log')
        type(self).i += 1
    def detail(self):
        super().obj_detail()

class Teacher(Base):
    i = 0
    def __init__(self,name,gender,school_obj):
        self.name =name
        self.gender = gender
        self.school = school_obj
        School.save(self,self.name+'.log')
        type(self).i += 1
    def detail(self):
        super().obj_detail()

class Classes(Base):
    i = 0
    def __init__(self,name,course_obj,teacher_obj,school_obj):
        self.name = name
        self.course = course_obj
        self.teacher = teacher_obj
        self.school = school_obj
        School.save(self,self.name+'.log')
        type(self).i += 1
    def detail(self):
        super().obj_detail()

class Students(Base):
    i = 0
    def __init__(self,name,gender,classes_obj,school_obj):
        self.name = name
        self.gender = gender
        self.classes = classes_obj
        self.school = school_obj
        School.save(self,self.name+'.log')
        type(self).i += 1
    def detail(self):
        super().obj_detail()


if __name__ == '__main__':
    school_bj = School('ob1','beijing','non-public')
    school_sh = School('ob2','shanghai','non-public')
    # school_bj.detail()
    # print(School.i)

    # print(Course.i)
    course_python = Course('python',100,3,school_bj)
    # print(Course.i)
    course_linux = Course('linux',200,5,school_bj)
    # print(Course.i)
    course_go = Course('go',300,7,school_sh)
    # print(Course.i)
    # course_python.detail()

    alex = Teacher('alex','male',school_bj)
    egon = Teacher('egon','mle',school_bj)
    huihui = Teacher('tom','female',school_sh)
    # print(Teacher.i)
    # alex.detail()

    class_5 = Classes('class_5',course_python,egon,school_bj)
    # print(Classes.i)
    # class_5.detail()

    tom = Students('tom','male',class_5,school_bj)
    # print(Students.i)
    # tom.obj_detail()