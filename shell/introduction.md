# Introduction

## First shell

在根目录中新建文件夹shell

```python
#!/bin/sh
#!/usr/bin/python

mkdir shell
cd shell
```

终端在这个路径下执行
```
chmod +x newdir.py
./newdir.py
```

## Hello World

```python
#!/bin/sh

echo "Hello World !"
```

## upload github v1

只需要把命令行挨个写上去就行了

```py
#!/bin/sh
#!/usr/bin/python

chmod +x merge.py 
./merge.py

git add .
git commit -m "update"
git push
```