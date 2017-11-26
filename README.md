# fcode - encode and decode in one place in real time

## Overview
inspired by [an on-line tool](http://tool.ph0en1x.com/hashtool/tools.html#conv/)

A simple Python tool to make real-time conversions among different encoded forms.

ASCII,BASE64,BASE32,HEX(BASE16),DEC,OCT,INT,URL ENCODE,HTML ENCODE,Morse code,

Rotation Encryption(include Caesar cipher),The Rail-Fence Cipher,etc. are currently supported.

GUI is written mainly by Tkinter,thus it is follows system.

## Usage
```python 
python fcode.py
```


    <img src="https://github.com/findneo/fcode/blob/master/demo_linux.gif" width="400" height="400">
    <img src="https://github.com/findneo/fcode/blob/master/demo.gif" width="400" height="400">

## Shortcut

| Press         | To                                    |
|:------        |   :------                             |
| CTRL+C/X/V    | Copy/Cut/Paste.                       |
| TAB/SHIFT+TAB |Move forward/backward through fileds.  |
| ENTER         |Select all.                            |
| ESC           |Quit.                                  | 

## Requirements：
Python2
  * Tkinter
  * base64
  * re
  * hashlib
