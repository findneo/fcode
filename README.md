# fcode - encode and decode in one place in real time

一个即时编码转换工具，目前支持ASCII, BASE64, BASE32, 十六进制(BASE16), 十进制, 八进制, INT, URL编码, HTML编码, 摩斯密码, Rotation 加密(含凯撒密码), 栅栏密码等。

A simple Python tool to make real-time conversions among different encoded forms. ASCII, BASE64, BASE32, HEX(BASE16), DEC, OCT, INT, URL ENCODE, HTML ENCODE, Morse code, Rotation Encryption(include Caesar cipher), The Rail-Fence Cipher, etc. are currently supported.

Inspired by [Tamás Koczka's work](https://koczkatamas.github.io).

# Usage
```python 
python fcode.py
# GUI is written mainly by Tkinter , 
# thus what it looks like varies with system.
```
![demo_linux.gif](https://i.loli.net/2018/03/01/5a981de5a272d.gif)
![demo.gif](https://i.loli.net/2018/03/01/5a981de5a3b05.gif)
    

<!---
    <img src="https://github.com/findneo/fcode/blob/master/demo_linux.gif" width="400" height="400">
    <img src="https://github.com/findneo/fcode/blob/master/demo.gif" width="400" height="400">

   <img src="https://i.loli.net/2018/03/01/5a981de5a272d.gif" width="400" height="400">
    <img src="https://i.loli.net/2018/03/01/5a981de5a3b05.gif" width="400" height="400">
-->

# Shortcut

| Press         | To                                    |
|:------        |   :------                             |
| CTRL+C/X/V    | Copy/Cut/Paste.                       |
| TAB/SHIFT+TAB |Move forward/backward through fileds.  |
| ENTER         |Select all.                            |
| ESC           |Quit.                                  | 

# Requirements：
Python2
  * Tkinter
  * base64
  * re
  * hashlib
