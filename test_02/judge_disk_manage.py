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

# 磁盘分区管理

# 判断/mnt/sdb1,/mnt/sdb2中挂载的分区是否正确
def judge_01():
    return os.system('mount | grep "/mnt/sdb1"') == 0 and \
            os.system('mount | grep "/mnt/sdb2"') == 0
            
# 判断/mnt/sdb1,/mnt/sdb2中是否开机自动挂载
def judge_02():
    return os.system('grep "/mnt/sdb1" /etc/fstab') == 0 and \
            os.system('grep "/mnt/sdb2" /etc/fstab') == 0
            
# 判断/mnt/sdb1,/mnt/sdb2中是否是xfs文件系统
def judge_03():
    return os.system('df -T | grep "/mnt/sdb1" | grep "xfs"') == 0 and \
            os.system('df -T | grep "/mnt/sdb2" | grep "xfs"') == 0
            

judges = [(judge_01, 5), (judge_02, 5), (judge_03, 5)]
comments = ['检查/mnt/sdb1,/mnt/sdb2中挂载的分区是否正确',
            '判断/mnt/sdb1,/mnt/sdb2中是否开机自动挂载',
            '判断/mnt/sdb1,/mnt/sdb2中是否是xfs文件系统']


# 限制用户的磁盘配额

# 判断是否开启了磁盘配额
def judge_04():
    return os.system('sudo quotaon -pa') == 0

# 判断是否对/mnt/sdb1目录开启了磁盘配额
def judge_05():
    return os.system('sudo repquota -pa | grep "/mnt/sdb1"') == 0

# 判断用户market01的磁盘配额是否正确
def judge_06():
    return os.system('sudo repquota -pa | grep "market01" | grep "100000"') == 0

# 判断组market的磁盘配额是否正确
def judge_07():
    return os.system('sudo repquota -pa | grep "market" | grep "100000"') == 0

judges_2 = [(judge_04, 5), (judge_05, 5), (judge_06, 5), (judge_07, 5)]
comments_2 = ['判断是否开启了磁盘配额',
            '判断是否对/mnt/sdb1目录开启了磁盘配额',
            '判断用户market01的磁盘配额是否正确',
            '判断组market的磁盘配额是否正确']



if __name__ == '__main__':
    print("磁盘分区管理".center(50, '-'))
    judge_all(judges, comments)
    print("限制用户的磁盘配额".center(50, '-'))
    judge_all(judges_2, comments_2)
    

