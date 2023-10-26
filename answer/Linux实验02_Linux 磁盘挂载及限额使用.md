# Linux 磁盘挂载

##### （1）向系统添加一块硬盘

##### （2）由系统识别硬盘名：

硬盘添加成功后，重新启动计算机，进行Linux系统，

使用`fdisk -l`命令识别添加的硬盘

```
[root@localhost ~]# fdisk -l

Disk /dev/sdb: 1073 MB, 1073741824 bytes, 2097152 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes

Disk /dev/sda: 21.5 GB, 21474836480 bytes, 41943040 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x000a59c7

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    41943039    19921920   8e  Linux LVM
```

可以看到：现在系统中两块硬盘`/dev/sda`和`/dev/sdb`，其中第一块硬盘`/dev/sda`容量21.5GB是目前正在使用的硬盘，划分了两个分区，分别是`/dev/sda1`和`/dev/sda2`，第二硬盘`/dev/sdb`容量1GB，目前还没有磁盘分区表

##### （3）对新硬盘进行分区

新的存储设备使用之前，需要进行磁盘存储设备的分区操作，可以使用磁盘分区工具fdisk完成。在Linux中，每一个硬件设备都映射到一个系统文件，对于硬盘、光驱等IDE或SCSI设备也不例外。

Linux给IDE设备分配由`hd`前缀组成的文件；而对于SCSI设备，则分配由`sd`前缀组成的文件。例如，第一个IDE设备，Linux系统定义为`hda`；第二个IDE设备定义为`hdb`，以此类推。而SCSI设备则依次定义为`sda`、`sdb`、`sde`等。主目前新添加的硬盘为`/dev/sdb`

分区：

```
[root@localhost ~]# fdisk /dev/sdb
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table
Building a new DOS disklabel with disk identifier 0x50561f8e.

Command (m for help):


```

列出所有命令

```
Command (m for help): m
Command action
   a   toggle a bootable flag 				//调整硬盘启动分区
	....
   d   delete a partition					//删除分区
	....
   l   list known partition types			//列出分区表
   m   print this menu						//列出所有命令
   n   add a new partition					//添加新分区
  	...
   p   print the partition table			//打印分区表
   q   quit without saving changes			//不保存退出
	...
   w   write table to disk and exit			//保存退出
   x   extra functionality (experts only)	//x额外选项

```

创建主分区：

第1：

```
Command (m for help): n
Partition type:
   p   primary (0 primary, 0 extended, 4 free)
   e   extended
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-2097151, default 2048): 2048
Last sector, +sectors or +size{K,M,G} (2048-2097151, default 2097151): +256M   
Partition 1 of type Linux and of size 256 MiB is set
```

第2：

```
Command (m for help): n
Partition type:
   p   primary (1 primary, 0 extended, 3 free)
   e   extended
Select (default p): p
Partition number (2-4, default 2): 2
First sector (526336-2097151, default 526336): 
Using default value 526336
Last sector, +sectors or +size{K,M,G} (526336-2097151, default 2097151): 
Using default value 2097151
Partition 2 of type Linux and of size 767 MiB is set
```

查看并保存分区

```
Command (m for help): p

Disk /dev/sdb: 1073 MB, 1073741824 bytes, 2097152 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x50561f8e

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1            2048      526335      262144   83  Linux
/dev/sdb2          526336     2097151      785408   83  Linux

Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.

```

（4）查看目前分区情况

```
[root@localhost ~]# fdisk -l

Disk /dev/sdb: 1073 MB, 1073741824 bytes, 2097152 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x50561f8e

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1            2048      526335      262144   83  Linux
/dev/sdb2          526336     2097151      785408   83  Linux

...
```

fdisk 

MBR 14个分区（4个主分区，扩展分区，逻辑分区）

gdisk 128主分区

GPT 128个主分区

**(4). 创建文件系统**

完成分区后，要在分区上创建文件系统，该分区才可以被使用。由于刚才创建了两个
区，所以要依次创建文件系统。

```
[root@localhost ~]# mkfs -t xfs /dev/sdb1
meta-data=/dev/sdb1              isize=512    agcount=4, agsize=16384 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0, sparse=0
data     =                       bsize=4096   blocks=65536, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal log           bsize=4096   blocks=855, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0

```

第二个分区同上

```
[root@localhost ~]# mkfs -t xfs /dev/sdb2
```

文件类型： ext2, ext3, swap, ms-dos ,ISO 9660



**（5）挂载使用**

创建挂载点：

```
# mkdir /mnt/sdb1
# mkdir /mnt/sdb2
```

挂载文件系统：

```
# mount /dev/sdb1 /mnt/sdb1
# mount /dev/sdb2 -t xfs -o ro /mnt/sdb2
```

查看挂载情况

```shell
# mount
/dev/sdb1 on /mnt/sdb1 type xfs (rw,relatime,seclabel,attr2,inode64,noquota)
/dev/sdb1 on /mnt/sdb2 type xfs (rw,relatime,seclabel,attr2,inode64,noquota)
```

查看磁盘空间占用情况

```
[root@localhost clouduser]# df
Filesystem              1K-blocks    Used Available Use% Mounted on
devtmpfs                   919504       0    919504   0% /dev
tmpfs                      931512       0    931512   0% /dev/shm
tmpfs                      931512    9764    921748   2% /run
tmpfs                      931512       0    931512   0% /sys/fs/cgroup
/dev/mapper/centos-root  17811456 1434904  16376552   9% /
/dev/sda1                 1038336  153672    884664  15% /boot
tmpfs                      186304       0    186304   0% /run/user/1000
/dev/sdb1                  258724   13328    245396   6% /mnt/sdb1
/dev/sdb2                  781988   32992    748996   5% /mnt/sdb2
```

(6) 可以使用两个硬盘了

```
# cd /mnt/sdb1
# python -c 'for i in range(10000):print("test {0}".format(i))' > 1.txt
```

可以在该目录下看到这个文件

需要注意： 通过mount命令手动挂截的文件系统，在系统关机时会自己卸载，下交启动后，该系统不能自动挂载

（7）**自动挂载**

如果需要文件系统被自动挂载，则在系统配置文件/etc/fstab中添加对该文件系统的挂载信息。

/etc/fstab是系统自动挂载的配置文件。该文件记录了在系统启动的过程中需要自动挂载的文件系统、挂载点、文件系统类型、挂载权限等

```
/dev/mapper/centos-root                    /    xfs     defaults        0 0
UUID=af089b9f-86ac-4022-a38a-570d450d0479 /boot xfs     defaults        0 0
/dev/mapper/centos-swap swap                    swap    defaults        0 0

```

文件中各列含义：

>  		1. 要挂载的设备，设备文件或uuid
>  		1. 挂载点
>  		1. 挂截文件类型
>  		1. 文件的类型参数
>  		1. 使用dump备份的频率，如果该值为0，表明系统无需备份；1表示每天备份；2不定期备份
>  		1. 系统开机文件检查的顺序

修改 `/etc/fstab`

```
...
/dev/mapper/centos-swap swap                    swap    defaults        0 0
/dev/sdb1 /mnt/sdb1	xfs defaults 0 0
/dev/sdb2 /mnt/sdb2	xfs defaults 0 0

```

## 磁盘限额配置

创建两个用户market1,market2,属于market ：

```
[root@localhost ~]# groupadd market
[root@localhost ~]# useradd -g market market01
[root@localhost ~]# useradd -g market market02
```

把新加载的硬盘调整到market组

```
[root@localhost ~]# chown :market /mnt/sdb1
```

启用磁盘限额

编辑 /etc/fstab文件，启用文件系统的磁盘限额。

```
# /etc/fstab
# Created by anaconda on Tue Mar 29 04:27:09 2022
#
# Accessible filesystems, by reference, are maintained under '/dev/disk'
# See man pages fstab(5), findfs(8), mount(8) and/or blkid(8) for more info
#
/dev/mapper/centos-root /                       xfs     defaults        0 0
UUID=af089b9f-86ac-4022-a38a-570d450d0479 /boot                   xfs     defaults        0 0
/dev/mapper/centos-swap swap                    swap    defaults        0 0
/dev/sdb1	/mnt/sdb1	xfs	defaults,uquota,gquota	0	0
```

重新挂载文件系统

```
[root@localhost ~]# umount /mnt/sdb1
[root@localhost ~]# mount /mnt/sdb1
```

设置每个用户的磁盘限额，设置容量软限制20M,硬限制30M

```
[root@localhost ~]# xfs_quota -x -c "limit -u bsoft=20M bhard=30M market01" /mnt/sdb1
[root@localhost ~]# xfs_quota -x -c "report -a"
User quota on /mnt/sdb1 (/dev/sdb1)
                               Blocks                     
User ID          Used       Soft       Hard    Warn/Grace     
---------- -------------------------------------------------- 
market01            0       20480      30720     00 [--------]

```

设置组的磁盘限额，设置容量软限制30M,容量硬容量40M，文件数软限制3000，文件硬限制4000

```
[root@localhost ~]# xfs_quota -x -c 'limit -g  bsoft=30M bhard=40M isoft=3000 ihard=4000 market' /mnt/sdb1

```

查看限额

```
[root@localhost ~]# xfs_quota -x -c "report -a"
User quota on /mnt/sdb1 (/dev/sdb1)
                               Blocks                     
User ID          Used       Soft       Hard    Warn/Grace     
---------- -------------------------------------------------- 
market01            0      20480      30720     00 [--------]
market02            0      20480      30720     00 [--------]

Group quota on /mnt/sdb1 (/dev/sdb1)
                               Blocks                     
Group ID         Used       Soft       Hard    Warn/Grace     
---------- -------------------------------------------------- 
market              0      30720      40960     00 [--------]

```

### 验证：

下方法检查限额是否成功。

1. 从root用户切换到market01用户

```
# su market01

```

2. 在你进行限额的目录中创建一个10M的文件

```
$[market01@localhost ~] dd if=/dev/zero of=/mnt/sdb1/1 bs=10M count=1
```

​	如果不能创建文件，请检查修改一下你的/mnt/sdb1的目录的拥有者和读写权限

3. 根据你的限额情况，复制这个文件，使用用户使用的存储空间要求超过限额。

```
$[market01@localhost ~] cp 1 2
$[market01@localhost ~] cp 1 3
```

​	4. 如果你的存储空间超过限额后，会出现相应的错误提示

<img src="D:\_teach\_course\2023-2024第1学期\Linux服务运维与管理\Linux课堂练习实验\answer\img\image-20211011161807350.png" alt="image-20211011161807350" style="zoom:50%;" />

5. 在root的用户权限下，可以看到marker01的用户已经超过限额

<img src="D:\_teach\_course\2023-2024第1学期\Linux服务运维与管理\Linux课堂练习实验\answer\img\image-20211011162118811.png" alt="image-20211011162118811" style="zoom:50%;" />