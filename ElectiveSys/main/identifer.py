#_*_coding:utf-8_*_
__author__ = 'achuDk'

import pickle,os
from ElectiveSys.lib import commons

class Nid:
    def __init__(self,role,cls_path):
        role_list = [
            'admin','school','teacher','course','course_to_teacher','classes','students'
        ]
        if role not in role_list:
            raise Exception('角色定义不正确，应为：%s' %','.join(role_list))
        self.role = role
        self.cls_path = cls_path
        self.uuid = commons.create_uuid()

    def get_obj_via_uuid(self):
        file_path = os.path.join(self.cls_path,self.uuid)
        return pickle.load(open(file_path,'rb'))

class AdminNid(Nid):
    def __init__(self,path):
        super().__init__('admin',path)

class SchoolNid(Nid):
    def __init__(self,path):
        super().__init__('school',path)

class TeacherNid(Nid):
    def __init__(self,path):
        super().__init__('teacher',path)

class CourseNid(Nid):
    def __init__(self,path):
        super().__init__('course',path)

class Course_to_teacherNid(Nid):
    def __init__(self,path):
        super().__init__('course_to_teacher',path)

class classesNid(Nid):
    def __init__(self,path):
        super().__init__('classes',path)

class StudentsNid(Nid):
    def __init__(self,path):
        super().__init__('students',path)

if __name__ == '__main__':
    s1 = SchoolNid('123')