# 第六章 应用层

## 应用层概述 

最上层，最顶层：对应用程序的通信提供服务。

应用层对**应用程序**的通信提供服务。

应用层协议定义

+ 应用进程交换的报文类型，请求还是响应

+ 各种报文类型的语法，如报文中的各个字段及其详细描述。

+ 字段的语义，即包含在字段中的信息的含义。

+ 进程何时and如何发送报文，以及对报文进行响应的规则。

应用层的**功能**

+ 文件传输，访问和管理

+ 电子邮件

+ 虚拟终端

+ 查询服务和远程作业登陆

应用层的重要协议：

+ FTP

+ SMTP/POP3

+ HTTP

+ DNS

## 网络应用模型

客户/服务器模型（client/server），p2p模型（peer to peer）

## C/S 模型

**服务器** 提供计算服务的设备。

1. 永久提供服务

2. 永久性的域名

**客户机** 请求计算服务的主机

1. 与服务器通信，使用服务器提供的服务

2. 间歇性接入网络

3. 可能使用动态ip地址

4. 不与其他客户机**直接**通信，先与服务器，再和客户机

应用： Web，文件传输FTP，远程登录，电子邮件

![CS模型](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/CS模型.png)

## p2p模型peer to peer

也叫对等模型，不存在永远在线的服务器。每个主机既可以提供服务，也可以请求服务

1. 任意端系统/节点之间可以直接通讯

2. 节点间歇性接入网络

3. 节点可能改变ip地址

4. 可扩展性好

5. 网络健壮性robustness好

![P2P模型](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/P2P模型.png)

## 域名解析系统DNS

Domain Name System域名解析系统，通过ip地址找到网站。用域名替代ip地址，如 www.baidu.com

![DNS工作过程](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/DNS工作过程.png)



### 域名

从左到右由低到高：www（三级域名）.baidu(二级域名).com（顶级域名）

顶级域名：国家顶级域名，通用顶级域名，基础结构域名/反向域名

二级域名：类别域名：ac、com、edu、gov；行政区域名：省市直辖市等

三级域名：mail;www;ftp;mail

四级域名：

### 域名服务器（dns服务器）

IP地址和域名的解析

+ 根域名服务器：最高层，有十三个不同的跟域名服务器，a.rootservers.net to m.rootservers.net

+ 顶级域名服务器:管理该顶级域名服务器注册的所有二级域名。

+ 权限域名服务器：负责一个区的域名服务器。

+ 本地域名服务器：当一个主机发出dns查询请求时，这个查询请求报文就发给**本地**域名服务器。


### 域名解析过程

递归查询，迭代查询：递归是用户只向本地DNS服务器发出请求，然后等待肯定或否定答案。而迭代是本地服务器向根DNS服务器发出请求，而根DNS服务器只是给出下一级DNS服务器的地址，然后本地DNS服务器再向下一级DNS发送查询请求直至得到最终答案。

[递归查询，迭代查询](https://blog.csdn.net/yanbao4070/article/details/79892032#:~:text=question%2F311381817.html-,DNS%E8%BF%AD%E4%BB%A3%E5%92%8C%E9%80%92%E5%BD%92%E7%9A%84%E5%8C%BA%E5%88%AB,%E8%AF%B7%E6%B1%82%E7%9B%B4%E8%87%B3%E5%BE%97%E5%88%B0%E6%9C%80%E7%BB%88%E7%AD%94%E6%A1%88%E3%80%82)

![域名解析过程](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/域名解析过程.png)

用高速缓存存储最近查询的域名，提高域名解析速度

## 文件传输协议FTP

文件传输协议 File Transfer Protocol

简单文件传输协议 Trivial File Transfer Protocol

### 介绍

提供**不同种类主机系统（硬软件体系都可以不同）之间**文件传输的能力。 

拷贝：上传和下载

### FTP服务器和用户端

FTP是基于客户/服务器（C/S）的协议

+ 用户通过一个客户及程序连接至在远程计算机上运行的服务器程序

+ 依照ftp协议提供服务，进行文件传送的计算机就是FTP服务器

+ 连接FTP服务器，遵循FTP协议与服务器传送文件的电脑就是FTP客户端。

### 工作原理

+ 登陆 ftp地址：用户名&密码 匿名

![FTP工作原理](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/FTP工作原理.png)

+ FTP使用TCP实现可靠传输。

服务器进程：1个主进程，n个从属进程

![FTP工作原理2](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/FTP工作原理2.png)

* 控制连接始终保持，只要建立连接。

* 数据连接保持一会儿

* 数据连接端口是否使用tcp20端口建立数据连接与传输模式有关

* 主动方式使用tcp20端口

* 被动方式由服务器和客户端自行协商决定（端口>1024）
（看看别的资料）

### FTP传输方式

+ 文本模式：ASCII模式，以文本序列传输数据

+ 二进制模式：Binary模式，以二进制序列传输数据

## 电子邮件

### 电子邮件的信息格式

信封 abc@163.com

内容 
+ 首部To，Subject
+ 主体

![电子邮件的信息格式](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/电子邮件信息格式.png)

### 组成结构

用户代理-邮件服务器-协议-邮件服务器-用户代理

![电子邮件系统组成结构](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/电子邮件系统组成结构.png)

![电子邮件系统组成结构2](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/电子邮件系统组成结构2.png)

+ **用户代理**功能：撰写，显示，处理，通信

+ **邮件服务器**功能：发送&接收邮件，向发件人报告邮件传送结果（c/s结构）

+ **协议** 发送SMTP，接收POP3，IMAP

### 简单邮件传送协议SMTP

SMTP规定了两个相互通信的SMTP进程之间应如何交换信息。

负责发送邮件的SMTP进程就是SMTP客户，负责接收的进程就是SMTP服务器

14条命令（几个字母），21种应答信息（三维数字代码+简单文字说明）

![SMTP](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/SMTP.png)

SMTP三个阶段：连接建立，邮件传送，连接释放

+ 连接建立
+ 邮件发送
   DATA命令

+ 连接释放

SMTP的缺点：
+ SMTP不能传送可执行文件或者其他二进制对象

+ 仅限于传送7位ASCII码，不能传输其他非英语国家的文字

+ SMTP服务器会拒绝超过一定长度的邮件

### 通用因特网扩送MIME

![MIME](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/MIME.png)

### 邮局协议POP3

图片（pop3是绿箭头那个

pop3的工作方式：

+ 下载并保留在服务器

+ 下载并删除

### 忘记报文存取协议IMAP

比POP3 复杂

![IMAP](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/IMAP.png)

### 基于万维网的电子邮件

方便，注意中间协议不同

![基于万维网的电子邮件](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/基于万维网的电子邮件.png)

## 万维网

概述：万维网（world wide web）是一个大规模的，联机式的信息储藏所/资料空间，是无数个网络站点和网页的集合。

统一资源定位符URL 是 资源（文字，视频，音频）的唯一标识

URL的一般形式：<协议>://<主机>:<端口>/<路径>，URL不区分大小写

协议：http，ftp

主机：域名，ip地址

用户点击超链接获取资源，这些资源通过超文本传输协议HTTP传送给使用者。

万维网也是以c/s方式工作，用户使用的浏览器就是万维网客户程序，万维网文档所驻留的主机 运行 服务器程序

万维网通过使用超文本标记语言**HTML**，使得万维网页面设计者可以很方便地从一个界面的链接转到另一个界面，
并能够在自己的屏幕上显示出来

### HTTP

HTTP协议定义了浏览器（万维网客户进程）怎样向万维网服务器请求万维网文档，以及服务器怎样把文档传送给浏览器。

#### HTTP工作流程

![HTTP工作流程](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/HTTP工作流程.png)

#### HTTP协议特点

无状态：每次访问是相同响应，无记忆的。

但是在实际工作中，一些万维网站点常常希望能够识别用户。

Cookie：是存储在用户主机中的文本文件，记录一段时间内某用户（识别码来识别）的访问记录。提供个性化服务

HTTP采用TCP作为运输层协议，但是HTTP本身是无连接的，通信双方在交换HTTP报文之前不需要先建立HTTP链接。

![HTTP协议特点](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/HTTP协议特点.png)

#### 连接方式

![HTTP连接方式](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/HTTP连接方式.png)

非持久连接耗时：两个rtt。

持久连接：保持连接，再想发信息就不用再建立连接

右图是非流水线式的，请求一个发一个，接受一个确认一个

流水线式可以同时多发

#### HTTP的报文结构

![HTTP报文结构](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/HTTP报文结构.png)

#### 状态码

3xx表示重定向，请求的网页转移到了新定位

![HTTP状态码](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/HTTP状态码.png)

### HTTPS

hyper text transfer protocol over securesocket layer

#### **HTTP问题：** 

HTTP数据传输过程中所有的数据都是明文传输，容易被窃听截取。
数据的完整性未校验，容易被篡改
没有验证对方身份，存在冒充危险

在http的基础上通过传输加密和身份认证保证了传输过程的安全性，原理：在http的基础上加入ssl（安全套接层）层或者TLS（安全传输层协议），混合加密。混合加密是指对称加密（解密加密都是同一个密钥，密钥管理负担问题，密钥也被截获的问题）和非对称加密（公钥私钥）。


![https和http关系](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/http1s和http关系.jpeg)

#### 过程


![https](https://github.com/nilshao/cpp-notebook/raw/master/internet/pictures/chapter06/http1s.jpeg)


1. 首先客户端通过URL访问服务器建立SSL连接。
2. 采用HTTPS的服务器要有一套CA证书，颁发证书的时候会产生私钥和公钥，私钥保存在服务端，不能泄露，公钥附带在证书信息中。
3. 服务端收到客户端请求后，会将网站支持的证书信息（证书中包含公钥）传送一份给客户端。
4. 客户端解析证书并对其验证，如果证书没问题，客户端就会从服务器证书中取出服务器的公钥A，然后客户端还会生成一个随机码KEY，并用公钥A加密
5. 客户端把加密后的随机码KEY发送给服务器，作为后面对称加密的密钥
6. 服务器在收到随机码KEY之后使用私钥对其解密，经过以上步骤建立了安全链接，并解决了密钥泄露
7. 服务器使用密钥key对数据进行对称加密，客户端使用key对称解密
8. 正常通信

#### 问题

申请证书成本，耗电，耗时间，其他的缺点说不明白不要说：中间人攻击，服务器劫持等






