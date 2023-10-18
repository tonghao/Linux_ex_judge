# Linux课程测验

### 文件管理

请以student的身份登录，如果没有student，请先创建student用户，切换到student用户（参见：用户管理练习01）

练习01 - 创建一个名为 `/home/student/grading` 的新目录。

练习02 - 在 `/home/student/grading` 目录中创建三个空文件，分别命名为`grade1`、`grade2` 和`grade3`。

练习03 - 获取`test.txt`文件的前五行，并存放到`/home/student/grading/manage-files.txt` 文件中 

练习04 - 获取`test.txt`文件的最后三行，并追加到文件 `/home/student/grading/manage-files.txt`中， 注意不要覆盖manage-files.txt文件 中已有的信息

练习05 - 拷贝文件test.txt到/home/student/grading/manage-files-copy.txt

练习06 - 编辑文件 /home/student/grading/manage-files-copy.txt，以便应该有连续两行的文本Test JJ。

练习07 - 编辑文件 /home/student/grading/manage-files-copy.txt，以便文件中不存在 TestHH 行文本。

练习08 - 编辑文件 /home/student/grading/manage-files-copy.txt，以便在 Test BB 行和 Test CC 行之间存在 A的 新行。

练习09 - 创建一个名为 `/home/student/hardlink` 到文件 `/home/student/grading/grade1` 的硬链接。

练习10 -  创建一个名为 `/home/student/softlink` 到文件 `/home/student/grading/grade2` 的软链接

练习11 - 列出/boot 目录内容，并将输输出保存到文件/home/school/grade/longlisting.txt 中。输出应该是一个“长列表”，其中包括文件权限、所有者和组所有者、每个文件的大小和修改日期。



### 用户管理
练习01- 创建一个名为“student"的新用户

练习02 - 创建一个名为“database”的新用户组，其 GID 为 50000。

练习03 - 创建一个名为 dbuser1 的新用户，该用户使用database组作为其辅助组之一。dbuser1的初始密码应设置为centos。(扩展：配置用户 dbuser1 以在首次登录时强制更改密码。用户 dbuser1 应能够在密码更改之日起 10 天后更改其密码。dbuser1 的密码应在自密码更改最后一天起 30 天内过期。)

练习04 - 配置用户 dbuser1 以使用 sudo 以超级用户身份运行任何命令。

练习05 - 将用户 dbuser1 配置为默认 umask 007。

练习06 - 创建一个名为 `/home/student/grading/review2` 的新目录，其中`student`和`database`分别作为其所属用户和组。配置该目录的权限，以便其中的任何新文件都继承`database`作为其所属组，而不管创建用户是谁。 `/home/student/grading/review2` 的权限应允许`database`的组成员和用户student 访问该目录并在其中创建内容。所有其他用户应该具有该目录的读取和执行权限。(扩展：另外，请确保用户只能从 /home/student/grading/review2 中删除他们自己的文件，而不能删除其他人的文件。）
