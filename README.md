# fcode - encode and decode in one place in real time
A simple Python tool to make real-time conversions among different encoded forms. ASCII, BASE64, BASE32, HEX(BASE16), DEC, OCT, INT, URL ENCODE, HTML ENCODE, Morse code, Rotation Encryption(include Caesar cipher), The Rail-Fence Cipher, etc. are currently supported.

Inspired by [Ph0en1x kt.pe tools mirror](http://tool.ph0en1x.com/hashtool/tools.html#conv/).

# Usage
```python 
python fcode.py
# GUI is written mainly by Tkinter , thus what it looks like varies with system.
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
