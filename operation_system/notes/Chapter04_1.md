# 第四章 第一节 

## 文件管理简介

作为系统资源的系统管理者，文件管理是操作系统提供的功能之一。
文件内部，文件之间如何组织？怎么能方便用户、应用程序使用文件？文件数据怎么存放在外存上？

### 文件的属性：

* 文件名：同一目录下不能有重名文件

* 标识符：一个系统内各个文件标识符唯一，对用户来说无可读性，只是操作系统使用的

* 类型

* 位置：文件存放路径，在外存中的地址

* 大小，创建时间，上次修改时间

* 保护信息：对文件进行保护的访问控制

### 文件内部数据怎样组织起来？

无结构文件，又称流式文件

有结构文件

![文件组织结构](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/文件组织结构.png)

### 文件之间的组织

“目录”

### 操作系统应该向上提供哪些共呢蝈 

创建文件，读文件，写文件，打开文件，关闭文件，删除文件

几个基本操作可以组成更复杂的操作，比如复制文件

### 文件如何存在外存？

和内存被分为内存块类似，外存也会被分为块/磁盘块/物理块，每个磁盘块大小相等，每块一般包含2的整数幂个地址。文件逻辑地址也可以被分为逻辑块号，块内地址。操作系统将逻辑地址转换为外存内的物理地址 

### 其他功能

文件共享，文件保护

## 文件的逻辑结构

逻辑结构：在用户看起来，文件内部数据结构如何组织起来

### 无结构文件

又称流式文件

### 有结构文件

又称记录式文件，由一组相似的记录组成，每一条记录又由若干个数据项组成。一般来说每条记录又一个数据项可以作为关键字，根据各条记录长度又可以分为定长记录和可变长记录。

 ![有结构文件逻辑结构](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/有结构文件逻辑结构.png)




### 顺序文件

文件中的记录一个接一个地顺序排列，分顺序存储和链式存储。顺序文件一般指物理上顺序存储的顺序文件，增加/删除一个记录比较困难

顺序文件：串结构，记录之间的顺序与关键字无关，通常按存入时间决定顺序；顺序结构：记录之间的顺序按照关键字排列。

能否随机存取，快速查找：

![顺序文件随机存取快速查找](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/顺序文件随机存取快速查找.png)


### 索引文件

对于可变长记录文件需要快速查找，如何解决？建立索引表加快文件检索速度，文件中的这些记录在物理上可以离散的存放。索引表本身是鼎昌的顺序文件 

### 索引顺序文件

索引文件的缺点：每个记录都对应一个索引表项，因此索引表可能太大。改进：**一组记录**对应一个索引表项，“分组的思想”。减少存储消耗，也减少了查找次数，直接在不重复的索引项里找就可以了，索引文件的索引表很多重复。

也可以继续建立多级索引表，成为**多级索引顺序文件**。

## 文件目录

![文件目录](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/文件目录.png)

### 文件控制块FCB

目录文件中的一条记录就是一个FCB，FCB中的有序集合称为文件目录，FCB包含了文件的基本信息（**文件名，物理地址**，逻辑结构，物理结构等），存取控制信息（可读？可写？禁止访问？），使用信息

需要对目录进行哪些操作？搜索，创建文件，删除文件，显示目录，修改目录

### 目录结构————单级目录结构

整个系统只有一张目录表，不允许文件重名

### 目录结构————两级目录结构

主文件目录MFD，用户文件目录UFD，允许不同用户的文件重名。

### 目录结构————多级目录结构（树形目录结构）

文件路径是个字符串，各级目录之间用“/”隔开，从根目录出发的路径称为绝对路径。系统根据绝对路径一层一层地找到下一级目录。

每次都从根目录找很低效，可以设置一个当前目录，从当前目录出发的“相对路径”，linux中用“.“表示当前目录


### 目录结构————无环图目录结构

树形结构层次结构清晰，但不方便文件共享，于是提出无环图目录结构

在树形结构的基础上增加一些指向同一节点的有向边，成为一个有向无环图。可以更方便地实现多个用户之间的文件共享。

这样可以用不同的文件名指向同一个文件，甚至指向同一目录。为了方便操作，设置共享计数器，删除文件时，只是删除该用的fcb，并使共享计数器减一

### 索引结点（FCB的改进）

 ![索引结点](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/索引结点.png)

除了文件名之外的所有信息都放在索引结点中，每个文件对应一个索引结点，目录项中只包含文件名，索引结点指针，因此每个目录项的长度大幅减小

## 文件的物理结构（文件的分配方式）

文件数据如何存放在外存中？对非空闲磁盘块的管理（存放了文件数据的磁盘块），对空闲磁盘块的管理

 ![文件的分配方式](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/文件的分配方式.png)

文件的逻辑地址被分为了一个一个的块，因此文件的逻辑地址也可以表示为 逻辑块号，块内地址。

### 连续分配方式

连续分配方式要求每个文件在磁盘上占有一组连续的块。 

逻辑地址到物理地址的映射：物理块号=起始块号+逻辑块号

读取某个磁盘块时，需要移动磁头，访问的两个磁盘块相隔越远，移动磁头所需要的时间越长。

结论：连续分配的文件在顺序读写时速度最快。不方便拓展，会产生磁盘碎片

### 链接分配

分显示链接和隐式链接

**隐式**：每个磁盘块都会保存指向下一个盘块的指针

只支持顺序访问，不支持随机访问，查找效率低，指针也消耗一定存储空间。

**显式**：把用于链接文件各个物理块的指针显式地存放在一张表中，即文件分配表FAT：file allocation table  

用户给出要访问的逻辑块号，操作系统找到该文件对应的目录项。访问速度比较快。 

![链接分配总结](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/链接分配总结.png)

### 索引分配

索引分配允许文件离散地分配在各个磁盘块中，系统会为每个文件建立一张索引表，索引表存放的磁盘块称为索引块，文件数据存放的磁盘块称为数据块。

索引分配方式可以支持随机访问。也可以容易实现拓展，但是索引表会消耗空间。

如果一个硬盘块都装不下索引表，  

1. 链接方案：多个索引块链接起来存放

2. 多层索引

3. 混合索引 

### 总结

![总结](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/总结.png)

## 文件存储空间管理

![文件存储空间管理](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/文件存储空间管理.png)

### 存储空间的划分和初始化

将物理磁盘分为一个个文件卷

![存储空间的划分和初始化](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/存储空间的划分和初始化.png)

### 存储空间管理：空闲表法

分配磁盘块：首次适应，最佳适应，最坏适应法

回收磁盘块：和内存管理一样，也要注意表项的合并

### 存储空间管理：空闲链表法

空闲盘块链：以盘块为单位组成一条空闲链

空闲盘区链：以盘区为单位

盘区：连续的空闲 盘块组成一个空闲盘区

### 存储空间管理：位示图法

![位示图法](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/位示图法.png)

0代表盘块空闲，1表示以分配


### 存储空间管理：成组链接法

linux采用的管理方式。
之前的策略组合起来，超级块：

### 总结

![存储空间管理总结](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/存储空间管理总结.png)

## 文件的基本操作

创建文件，删除文件，写文件，读文件，打开文件，关闭文件

### 创建文件：

![创建文件](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/创建文件.png)

### 删除文件

![删除文件](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/删除文件.png)

### 写文件

![写文件](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/写文件.png)

### 打开文件

![打开文件](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/打开文件.png)

### 关闭文件

![关闭文件](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/关闭文件.png)

### 读文件

![读文件](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/读文件.png)

### 总结

![文件操作总结](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/文件操作总结.png)

## 文件共享

![文件共享](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/文件共享.png)

### 基于索引的共享方式

回顾：索引结点

索引结点中设置一个链接计数变量count

### 基于链接的共享方式

快捷方式，链接一个路径信息

![文件共享总结](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/文件共享总结.png)

## 文件保护

口令保护，加密保护，访问控制

### 口令保护

为文件设置一个口令，用户请求访问该文件时需要提供口令，口令一般存在FCB或者索引结点中

优点：空间开销不多，验证口令的时间开销也很小

缺点：口令存放在系统中，不安全

### 加密保护

为文件设置密码。如异或加密。

![加密保护](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/加密保护.png)

### 访问控制

在每个文件的fcb或索引结点增加一个访问控制表（access control list），该表中记录了每个用户可以对该文件执行哪些操作（权限）。

![文件保护总结](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/文件保护总结.png)


## 文件系统的层次结构

![文件系统的层次结构](https://github.com/nilshao/cpp-notebook/raw/master/operation_system/images/chapter4/文件系统的层次结构.png)
