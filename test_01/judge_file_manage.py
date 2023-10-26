#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# 导入上级目录的lib库中的judge_all函数
# 获取当前脚本的文件路径
current_file = os.path.abspath(__file__)

# 获取当前脚本的父目录路径
current_dir = os.path.dirname(current_file)

# 将父目录添加到系统路径
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from lib import judge_all


def judge(name, method, score):
    if method():
        return name, score
    return name, 0

def judge_01():
    # 检测目录/home/student/grading是否存在,并且是目录
    return os.path.exists('/home/student/grading') and \
                os.path.isdir('/home/student/grading')
                

def judge_02():
    # 检测/home/student/grading目录下`grade1`、`grade2` 和`grade3`文件是否存在
    return all([os.path.exists('/home/student/grading/grade1'),
            os.path.exists('/home/student/grading/grade2'),
            os.path.exists('/home/student/grading/grade3'),
            os.path.isfile('/home/student/grading/grade1'),
            os.path.isfile('/home/student/grading/grade2'),
            os.path.isfile('/home/student/grading/grade3')])

def judge_03():
    # 检测`/home/student/grading/manage-files.txt`中的前五行与'test.txt'中的前五行是否相同
    with open('/home/student/grading/manage-files.txt') as f1, \
            open('test.txt') as f2:
        for i in range(5): 
            if f1.readline() != f2.readline():
                return False
    return True

def judge_04():
    # 检测`/home/student/grading/manage-files.txt`中的后三行与'test.txt'中的后三行是否相同
    with open('/home/student/grading/manage-files.txt') as f1, \
        open('test.txt') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        return lines1[-3:] == lines2[-3:]
        
def judge_05():
    # 判断`/home/student/grading/manage-files-copy.txt`文件是否存在
    return os.path.exists('/home/student/grading/manage-files-copy.txt')        

def judge_06():
    # 判断`/home/student/grading/manage-files-copy.txt`有连续两行的文本"Test JJ"
    with open('/home/student/grading/manage-files-copy.txt') as f:
        lines = f.readlines()
        for i in range(len(lines)-1):
            if lines[i] == lines[i+1] and lines[i] == 'Test JJ\n':
                return True
    return False

def judge_07():
    # 判断`/home/student/grading/manage-files-copy.txt`文件中不存在 Test HH 行文本
    with open('/home/student/grading/manage-files-copy.txt') as f:
        for line in f:
            if line == 'Test HH\n':
                return False
    return True

def judge_08():
   # 判断`/home/student/grading/manage-files-copy.txt`文件中 在 Test BB 行和 Test CC 行之间存在 A 的 新行 
   with open('/home/student/grading/manage-files-copy.txt') as f:
       lines = f.readlines()
       for i in range(len(lines)):
           if lines[i] == 'Test BB\n':
               for j in range(i+1, len(lines)):
                   if lines[j] == 'Test CC\n':
                       return 'A\n' in lines[i:j]
                   
    
def judge_09():
    # 判断`/home/student/hardlink` 到文件 `/home/student/grading/grade1` 的硬链接是否存在
    return os.path.exists('/home/student/hardlink') and \
            os.path.isfile('/home/student/hardlink') and \
            os.path.samefile('/home/student/hardlink', '/home/student/grading/grade1')
            
def judge_10():
    # 判断 `/home/student/softlink` 到文件 `/home/student/grading/grade2` 的软链接是否存在
    return os.path.exists('/home/student/softlink') and \
        os.path.islink('/home/student/softlink') and \
        os.path.samefile('/home/student/softlink', '/home/student/grading/grade2')
        
def judge_11():
    # 判断文件/home/school/gradeing/longlisting.txt 中,保存的是'ls -l'的信息，包括文件权限、所有者和组所有者、每个文件的大小和修改日期
    with open('/home/student/grading/longlisting.txt') as f:
        lines = f.readlines()
        for line in lines[1:]:
            if len(line.split()) != 9:
                return False
        return True

# 评分标准
judges =[(judge_01, 5), (judge_02, 5), (judge_03, 5), (judge_04, 5), (judge_05, 5), (judge_06, 5), (judge_07, 5), (judge_08, 5), (judge_09, 5), (judge_10, 5), (judge_11, 5) ]     
   
if __name__ == '__main__':
    judge_all(judges)
                
               
            
            

    

    