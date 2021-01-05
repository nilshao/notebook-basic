1. 头文件
```C++
#include<queue>
```
2. 定义
```C++
priority_queue<int> p;
```

3. 优先输出大数据

    priority_queue<Type, Container, Functional>

Type为数据类型， Container为**保存数据的容器**，Functional为元素比较方式。
如果不写后两个参数，那么容器默认用的是vector，比较方式**默认**用operator<，也就是优先队列是大顶堆，**队头元素最大。**

例如：

```C++
#include<iostream>
#include<queue>

using namespace std;
 

int main(){
	priority_queue<int> p;

	p.push(1);
	p.push(2);
	p.push(8);
	p.push(5);
	p.push(43);

    for(int i=0;i<5;i++){
        std::cout << p.top() << std::endl;  
		p.pop();
	}
    return 0;
}
```

输出：







4、优先输出小数据(小顶堆)

**方法一：**
priority_queue<int, vector<int>, greater<int> > p;

例如：

```C++

#include<iostream>
#include<queue>
#include<vector>

int main(){

	std::priority_queue<int, std::vector<int>, std::greater<int> > p;

	p.push(1);
	p.push(2);
	p.push(8);
	p.push(5);
	p.push(43);

    for(int i=0;i<5;i++){
        std::cout << p.top() << std::endl;
		p.pop();
	}

    return 0;
}
```

输出：





**方法二：自定义优先级** 重载默认的 < 符号

例子：

```C++
#include<iostream>
#include<queue>
#include<cstdlib>

using namespace std;

struct Node{
    int x,y;
	Node(int a=0, int b=0):
    x(a), y(b) {}
};

struct cmp{

    bool operator()(Node a, Node b){
        if(a.x == b.x)	return a.y>b.y;
        return a.x>b.x;
    }
}; 

int main(){
	std::priority_queue<Node, std::vector<Node>, cmp> p;
    
    for(int i=0; i<10; ++i)
        p.push(Node(rand(), rand()));
    while(!p.empty()){
        std::cout<<p.top().x<<' '<<p.top().y<<std::endl;
        p.pop();

        }//while

    //getchar();

    return 0;
}
```

输出：