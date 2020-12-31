# 第二章 线性表

## 线性表定义

线性表是具有相同数据类型的n(n>=0)个数据元素的有限序列,其中n为表长,当n=0时线性表是一个空表。若用L命名线性表,则其一般表示为：

L=(a1,a2,a3...ai,ai+1,...an)

**概念** 每个数据元素所占空间一样大。位序i；表头元素；表位元素；前驱；后驱

## 线性表基本操作

* InitList(&L):**初始化**操作。构造一个空的线性表L,分配内存空间。
* DestroyList(&):**销毁**操作。销毁线性表,并释放线性表L所占用的内存空间。
* ListInsert(&L,i,e):**插入**操作。在表L中的第i个位置上插入指定元素e
* ListDelete(&L,i,&e):**删除**操作。删除表L中第i个位置的元素,并用e返回删除元素的值。
* LocateElem(L,e):**按值査找**操作。在表L中査找具有给定关键字值的元素。
* GetElem(L,i):**按位查找**操作。获取表L中第i个位置的元素的值
  
其他常用操作:
* Length(L):**求表长**。返回线性表L的长度,即L中数据元素的个数。
* Prigtlist(L):**输出**操作。按前后顺序输出线性表L的所有元素值。
* Empty(L):**判空**操作。若L为空表,则返回tue,否则返回false。


## 顺序表

回忆：

![线性表存储物理结构](https://github.com/nilshao/cpp-notebook/raw/master/data_structure/chapter02/images/线性表存储物理结构.png)

### 顺序表定义

**顺序表**。用顺序存储的方式实现线性表 
**顺序存储**。把逻辑上相邻的元素存储在物理 位置上也相邻的存储单元中,元素之间的关系由存储单元的邻接关系来体现

![顺序表定义](https://github.com/nilshao/cpp-notebook/raw/master/data_structure/chapter02/images/顺序表定义.png)

**数据元素大小**。C语言：sizeof(ele)

### 顺序表的实现————静态分配

注意：没有设置数据元素的默认值，内存中会有遗留的“脏数据”，有的会元素初始化为奇怪的数字。

如果数据存满了怎么办：存储空间是静态的，顺序表的表长确定后就无法更改。

### 顺序表的实现————动态分配

![动态分配](https://github.com/nilshao/cpp-notebook/raw/master/data_structure/chapter02/images/动态分配.png)  

malloc函数的参数指明了要分配多大的连续内存空间。

C++：new，delete

可以增加动态数组的长度

![动态分配增加数组长度](https://github.com/nilshao/cpp-notebook/raw/master/data_structure/chapter02/images/动态分配增加数组长度.png) 

### 顺序表特点

1. 随机访问，在O(1)找到第i个元素
2. 存储密度高，每个节点只存储数据元素
3. 拓展容量不方便(即便采用动态分配的方式实现,拓展长度的时间复杂度也比较高) 
4. 插入、删除操作不方便,需要移动大量元素
   








![](https://github.com/nilshao/cpp-notebook/raw/master/data_structure/chapter02/images/.png)