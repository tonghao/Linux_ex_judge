# Linux 课程测验答案

### 文件管理

请以 student 的身份登录，如果没有 student，请先创建 student 用户，切换到 student 用户（参见：用户管理练习 01）

练习 01 - 创建一个名为 `/home/student/grading` 的新目录。

```bash
mkdir  /home/student/grading
```

练习 02 - 在 `/home/student/grading` 目录中创建三个空文件，分别命名为`grade1`、`grade2` 和`grade3`。

```
touch /home/student/grading/grade{1,2,3}
```

练习 03 - 获取`test.txt`文件的前五行，并存放到`/home/student/grading/manage-files.txt` 文件中(使用 head 命令)

```
head -5 text.txt > /home/student/grading/manage-files.txt
```

练习 04 - 获取`test.txt`文件的最后三行，并追加到文件 `/home/student/grading/manage-files.txt`中， 注意不要覆盖 manage-files.txt 文件 中已有的信息(使用 tail 命令)

```
tail -3 test.txt >> /home/student/grading/manage-files.txt
```

练习 05 - 拷贝文件 test.txt 到/home/student/grading/manage-files-copy.txt

```
cp test.txt/home/student/grading/manage-files-copy.txt
```

练习 06 - 编辑文件 /home/student/grading/manage-files-copy.txt，以便应该有连续两行的文本 Test JJ。

```
vim /home/student/grading/manage-files-copy.txt
yyp
```

练习 07 - 编辑文件 /home/student/grading/manage-files-copy.txt，以便文件中不存在 Test HH 行文本。



练习 08 - 编辑文件 /home/student/grading/manage-files-copy.txt，以便在 Test BB 行和 Test CC 行之间存在 A 的 新行。

```
vim /home/student/grading/manage-files-copy.txt
esc + o
A
:wq
```

练习 09 - 创建一个名为 `/home/student/hardlink` 到文件 `/home/student/grading/grade1` 的硬链接。

```
ln /home/student/grading/grade1 /home/student/hardlink 
```

练习 10 - 创建一个名为 `/home/student/softlink` 到文件 `/home/student/grading/grade2` 的软链接

```
ln -s /home/student/grading/grade2 /home/student/softlink
```

练习 11 - 列出/boot 目录内容，并将输输出保存到文件/home/school/grading/longlisting.txt 中。输出应该是一个“长列表”，其中包括文件权限、所有者和组所有者、每个文件的大小和修改日期。

```
ls -l /boot >  /home/student/grading/longlisting
```



### 用户管理

练习 01- 创建一个名为“student"的新用户

```
useradd student
```

练习 02 - 创建一个名为“database”的新用户组，其 GID 为 50000。

```
groupadd -g 50000 database
```

练习 03 - 创建一个名为 dbuser1 的新用户，该用户使用 database 组作为其辅助组之一。dbuser1 的初始密码应设置为 centos。(扩展：配置用户 dbuser1 以在首次登录时强制更改密码。用户 dbuser1 应能够在密码更改之日起 10 天后更改其密码。dbuser1 的密码应在自密码更改最后一天起 30 天内过期。)

```
useradd -G database dbuser1

chage -d 0 dbuser1
chage -m 10 dbuser1
chage -M 30 dbuser1

```

练习 04 - 配置用户 dbuser1 以使用 sudo 以超级用户身份运行任何命令。

```
echo "dbuser1 ALL=(ALL) ALL" >> /etc/sudoers.d/dbuser1
```

练习 05 - 将用户 dbuser1 配置为默认 umask 007。

```
echo "umask 007" >> /home/dbuser1/.bash_profile
echo "umask 007" >> /home/dbuser1/.bashrc
```

练习 06 - 创建一个名为 `/home/student/grading/review2` 的新目录，其中`student`和`database`分别作为其所属用户和组。配置该目录的权限，以便其中的任何新文件都继承`database`作为其所属组，而不管创建用户是谁。 `/home/student/grading/review2` 的权限应允许`database`的组成员和用户 student 访问该目录并在其中创建内容。所有其他用户应该具有该目录的读取和执行权限。另外，请确保用户只能从 /home/student/grading/review2 中删除他们自己的文件，而不能删除其他人的文件。

```
mkdir /home/student/grading/review2
chown student:database /home/student/grading/review2

chmod g+s /home/student/grading/review2
chmod 775 /home/student/grading/review2
chmod o+t /home/student/grading/review2
```

