
# -*- coding: utf-8 -*-
#!/usr/bin/env python3


import os

from judge_utils import judge, judge_all


def judge_01():
    # 检查Linux中的用户student是否存在, 并且是sodoer用户
    return os.system('id student') == 0 and os.system('sudo -l -U student') == 0

def judge_02():
    # 检查database的新用户组是否存在，其 GID 为 50000
    return os.system('grep database /etc/group | grep 50000') == 0

def judge_03():
    # 检查  dbuser1 的用户, database组为其辅助组
    return os.system('id dbuser1 | grep database') == 0
                

def judge_04():
    # 检查  dbuser1 的用户,其为超级用户 
    return os.system('id dbuser1') == 0 and os.system('sudo -l -U dbuser2') == 0

def judge_05():
    # 检查dbuser1 配置为默认 umask 为007
    return os.system('sudo grep umask /home/dbuser1/.bashrc | grep 007') == 0

def judge_06():
    # 检查/home/student/grading/review2目录和sgid权限和sticky权限是否正确
    return os.system('stat /home/student/grading/review2 | grep "Access: (2775/drwxrwsr-x)"') == 0

    
judges =[(judge_01, 5), (judge_02, 5), (judge_03, 5), (judge_04, 5), (judge_05, 5), (judge_06, 5)]

if __name__ == '__main__':
    judge_all(judges)