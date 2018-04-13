#_*_coding:utf-8_*_
__author__ = 'achuDk'

import os,pickle
import identifer
from ElectiveSys.conf import settings

data_dir = settings.DATA_DIR

class Base:
    def obj_detail(self):
        print('%s %s 的详细信息：%s' %(type(self),self.__dict__['name'],self.__dict__))
    #所有类生成的对象必须有 name 属性
    def __str__(self):
        return self.name
    def save(self,nid):
        # print(self)
        path = os.path.join(data_dir,str(type(self).__name__))
        file_name = os.path.join(data_dir,str(type(self).__name__),str(nid))
        # print(data_dir)
        # print(path,type(path))
        # print(file_name)
        os.makedirs(path,exist_ok='ok')
        pickle.dump(self,open(file_name,'wb'))
    @classmethod
    def get_all_obj_list(cls):
        ret = []
        dira = os.path.join(os.path.dirname(os.getcwd()), 'database', self.__name__)
        print(dira,type(dira))
        for i in os.listdir(dira):
            print(i)
            ret.append(i)

# class Admin(Base):
#     def __init__(self,name,password):
#         self.nid = identifer.AdminNid(os.path.join(data_dir,type(self).__name__)).uuid
#         self.name = name
#         self.password = password

class School(Base):
    def __init__(self,name,addr):
        self.nid = identifer.SchoolNid(os.path.join(data_dir,type(self).__name__)).uuid
        # print(self.nid)
        self.name = name
        self.addr = addr
        School.save(self,self.nid)

class Teacher(Base):
    def __init__(self,name,gender,school_obj):
        self.nid = identifer.TeacherNid(os.path.join(data_dir,type(self).__name__)).uuid
        self.name = name
        self.gender = gender
        self.school = school_obj.nid
        Teacher.save(self,self.nid)

# class Course(Base):
#     def __init__(self,name,price,period,school_obj):
#         self.nid = identifer.CourseNid(os.path.join(data_dir,type(self).__name__)).uuid
#         self.name = name
#         self.price = price
#         self.period = period
#         self.school = school_obj.nid
#         Course.save(self,self.nid)
#
# class Course_to_teacher(Base):
#     def __init__(self,name,addr):
#         self.nid = identifer.Course_to_teacherNid(os.path.join(data_dir,type(self).__name__)).uuid
#         self.name = name
#         pass
#         Course_to_teacher.save(self,self.nid)
#
# class Classes(Base):
#     def __init__(self,name,course_obj,teacher_obj,school_obj):
#         self.nid = identifer.ClassesNid(os.path.join(data_dir,type(self).__name__)).uuid
#         self.name = name
#         self.course = course_obj.nid
#         self.teacher = teacher_obj.nid
#         self.school = school_obj.nid
#         Classes.save(self,self.nid)
#
# class Students(Base):
#     def __init__(self,name,gender,classes_obj,school_obj):
#         self.nid = identifer.StudentsNid(os.path.join(data_dir,type(self).__name__)).uuid
#         self.name = name
#         self.gender = gender
#         self.classes = classes_obj.nid
#         self.school = school_obj.nid
#         Students.save(self,self.nid)

if __name__ == '__main__':
    s1 = School('ob','beijing')
    alex = Teacher('ales','male',s1)