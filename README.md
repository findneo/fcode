# fcode

## 概述：
这个小工具能够实时互转ASCII，BASE64，BASE32，HEX(BASE16)，DEC，OCT，INT，URL ENCODE，HTML ENCODE，MORSE，ROT，栅栏密码等，灵感来自于一个[在线编解码工具](http://tool.ph0en1x.com/hashtool/tools.html#conv/) 。

工具主要使用Tkinter编写，可在Windows/Linux上运行，UI跟随系统。

## 使用：
```python 
python fcode.py
```

<center class="half">
    <img src="https://github.com/findneo/fcode/blob/master/demo_linux.gif" width="400">
    <img src="https://github.com/findneo/fcode/blob/master/demo.gif" width="400">
</center>

## 快捷键
* ESC 退出
* TAB 切换
* SHIFT+TAB 切换
* ENTER 全选
* CTRL+X/C/V  剪切/复制/粘贴

## 依赖：
Python2
  * Tkinter
  * base64
  * re
  * hashlib
