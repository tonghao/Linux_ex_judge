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


def judge_args(judge, *args):
    def _judge():
        return judge(*args)
    return _judge

# 判断路径中是否是挂载的分区
def judge_mount(mount_path):
    return os.system('mount | grep {}'.format(mount_path)) == 0 
            
        
# 判断路径中是否是开机自动挂载
def judge_auto_mount(mount_path):
    return os.system('grep "{}" /etc/fstab'.format(mount_path)) == 0
            
# 判断路径中是否是xfs文件系统
def judge_xfs(mount_path):
    return os.system('df -T | grep "{}" | grep "xfs"'.format(mount_path)) == 0 

judges = [(judge_args(judge_mount,'/mnt/sdb1'), 5),
          (judge_args(judge_mount,'/mnt/sdb2'), 5),
          (judge_args(judge_auto_mount,'/mnt/sdb1'), 5), 
          (judge_args(judge_auto_mount,'/mnt/sdb2'), 5),
          (judge_args(judge_xfs,'/mnt/sdb1'), 5), 
          (judge_args(judge_xfs,'/mnt/sdb2'), 5)]
comments = ['检查/mnt/sdb1中挂载的分区是否正确',
            '检查/mnt/sdb2中挂载的分区是否正确',
            '判断/mnt/sdb1,中是否开机自动挂载',
            '判断/mnt/sdb2中是否开机自动挂载',
            '判断/mnt/sdb1中是否是xfs文件系统',
            '判断//mnt/sdb2中是否是xfs文件系统']


# 限制用户的磁盘配额



# 判断是否对/mnt/sdb1目录开启了磁盘配额
def judge_05():
    return os.system('sudo quotaon -pa | grep "/mnt/sdb1" ') == 0

# 判断用户market01的磁盘配额是否设置了配额
def judge_06():
    return os.system('sudo repquota -u /mnt/sdb1 | grep "market01" ') == 0

# 判断组market的磁盘配额是否正确
def judge_07():
    
    return os.system('sudo xfs_quota -x -c "report -a"| grep "market "') == 0

# 判断用户market01的磁盘配额是否超过了限制
def judge_08():
    return os.system('sudo repquota -u /mnt/sdb1 | grep "market01" | grep "days" ') == 0

judges_2 = [(judge_05, 5), (judge_06, 5), (judge_07, 5)]
comments_2 = [
            '判断是否对/mnt/sdb1目录开启了磁盘配额',
            '判断用户market01的磁盘配额是否正确',
            '判断组market的磁盘配额是否正确',
            '判断用户market01的磁盘配额是否超过了限制']



if __name__ == '__main__':
    print("磁盘分区管理".center(50, '-'))
    judge_all(judges, comments)
    print("限制用户的磁盘配额".center(50, '-'))
    judge_all(judges_2, comments_2)
    

