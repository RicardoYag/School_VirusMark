#需要修改的部分
0. 创建好usertable,录入好相关学生的信息
```sql
CREATE TABLE `usertable` (
  `stuId` char(20) NOT NULL,
  `stuName` char(20) DEFAULT NULL,
  `classId` char(20) DEFAULT NULL,
  `groupId` char(20) DEFAULT NULL,
  `qqId` char(20) DEFAULT NULL,
  PRIMARY KEY (`stuId`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```
2. isqd.py 中 要填写头部的school学校代码
3. isqd.py 中 要修改三条查询语句的tablename
4. 填写utils.sql中连接数据库参数
5. 最重要的地方,isqd.sendQQMessage()函数的url自己去找机器人提供平台,按照他们的接口拼接url发送消息,也可以了解一下Mirai,自己实现一个
6. isqd主要提供了查询哪些学生未打卡,并不解决qq机器人实现问题,个人使用了Mirai的http接口搭建了一个web-server
7. 之前我用的是Qmsg酱,当时觉得很不错,还给作者支付宝打赏了10块钱,后来我自己有去研究Mirai框架,发现实现一个Qmsg实在过于简单,经典做法**加一层**达到协议转换,想让消息隐私控制在自己手里,也就自己实现了一个,而且那个群里自从有云服务器的赞助商后,那个群简直了,,,于是屏蔽了那个群里很久没有发言,然后我被群主直接踢了233