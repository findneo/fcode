# -*-coding:utf8 -*-
# by https://findneo.github.io/
# esc退出,tab切换,回车/双击全选，剪切复制粘贴，仅处理可打印字符
from Tkinter import *
from functions import *
import time

root = Tk()
root.title("fcode v0.1")
root.geometry("600x420")
printable_chars = ''.join([chr(i) for i in range(32, 127)])
frame = Frame(root)
width = 400
# ---------------------------------------------------------------
my_ascii = StringVar(frame)
my_base64 = StringVar(frame)
my_base32 = StringVar(frame)
my_hex = StringVar(frame)
my_dec = StringVar(frame)
my_oct = StringVar(frame)
my_bin = StringVar(frame)
my_int = StringVar(frame)
my_url = StringVar(frame)
my_html = StringVar(frame)
my_rev = StringVar(frame)
my_upper = StringVar(frame)
my_lower = StringVar(frame)
my_md5 = StringVar(frame)
my_morse = StringVar(frame)
my_rot = StringVar(frame)
my_zhalan = StringVar(frame)

R0 = Entry(frame, width=width, textvariable=my_ascii)
R1 = Entry(frame, width=width, textvariable=my_base64)
R2 = Entry(frame, width=width, textvariable=my_base32)
R3 = Entry(frame, width=width, textvariable=my_hex)
R4 = Entry(frame, width=width, textvariable=my_dec)
R5 = Entry(frame, width=width, textvariable=my_oct)
R6 = Entry(frame, width=width, textvariable=my_bin)
R7 = Entry(frame, width=width, textvariable=my_int)
R8 = Entry(frame, width=width, textvariable=my_url)
R9 = Entry(frame, width=width, textvariable=my_html)
R10 = Entry(frame, width=width, textvariable=my_rev)
R11 = Entry(frame, width=width, textvariable=my_upper)
R12 = Entry(frame, width=width, textvariable=my_lower)
R13 = Entry(frame, width=width, textvariable=my_md5)
R14 = Entry(frame, width=width, textvariable=my_morse)
R15 = Entry(frame, width=width, textvariable=my_rot)
R16 = Entry(frame, width=width, textvariable=my_zhalan)

tags = ["ASCII", "BASE64", "BASE32", "HEX", "DEC", "OCT",
        "BIN", "INT", "URL", "HTML", "REV", "UPPER", "LOWER", "MD5", "MORSE", "ROT", "栅栏"]
entry_list = [R0, R1, R2, R3, R4, R5, R6,
              R7, R8, R9, R10, R11, R12, R13, R14, R15, R16]
var_list = [my_ascii, my_base64, my_base32, my_hex, my_dec, my_oct,
            my_bin, my_int, my_url, my_html, my_rev, my_upper, my_lower, my_md5, my_morse, my_rot, my_zhalan]

f_decode = {
    R0: de_ascii,
    R1: de_base64,
    R2: de_base32,
    R3: de_hex,
    R4: de_dec,
    R5: de_oct,
    R6: de_bin,
    R7: de_int,
    R8: de_url,
    R9: de_html,
    R10: de_rev,
    R11: de_upper,
    R12: de_lower,
    R13: de_md5,
    R14: de_morse,
    R15: de_rot,
    R16: de_zhalan
}
f_encode = {
    R0: en_ascii,
    R1: en_base64,
    R2: en_base32,
    R3: en_hex,
    R4: en_dec,
    R5: en_oct,
    R6: en_bin,
    R7: en_int,
    R8: en_url,
    R9: en_html,
    R10: en_rev,
    R11: en_upper,
    R12: en_lower,
    R13: en_md5,
    R14: en_morse,
    R15: en_rot,
    R16: en_zhalan
}
for i in range(len(tags)):
    Label(frame, text=tags[i]).grid(row=i, column=0)
for i, j in enumerate(entry_list):
    j.grid(row=i, column=1)
# -------------------------------------------------------------
ev = [entry_list, var_list]


def tr_ev(foo):
    """transfer between entry_list and var_list
    """
    return ev[1][ev[0].index(foo)] if foo in ev[0] else ev[0][ev[1].index(foo)]


def refresh(event):
    if event.keysym == 'Escape':
        root.quit()
    if event.keysym == 'Return':
        event.widget.selection_range(0, END)
        return 0
    # event.widget(an instance) is the widget(entry,here) which generated the event.
    # entry.get(self) returns the text.
    data_entry = event.widget
    data_in = event.widget.get()

    for i in data_in:
        if i not in printable_chars:
            return 0
    try:
        raw_plain = f_decode[data_entry](data_in)
    except:
        raw_plain = ""

    for i in entry_list:
        if i is data_entry:
            continue
        else:
            try:
                tr_ev(i).set(f_encode[i](raw_plain))
            except:
                tr_ev(i).set("( ´◔ ‸◔')")


root.bind("<Key>", refresh)
R0.focus_set()


# def frame2():
#     frame.grid_remove()
#     frame2.grid(row=1, sticky=N)


# frame2 = Frame(root)
# label = Label(frame2, text='foo')
# label.grid()
# frame2.grid(row=1, sticky=N)


# def fram():
#     frame.grid()
#     frame2.grid_remove()


# navi = Frame(root)
# bnt1 = Button(navi, text="pe.tk", command=frame)
# bnt2 = Button(navi, text="pe.tk2", command=frame2)
# bnt1.grid(column=0)
# bnt2.grid(column=1)
# frame.grid(row=1, sticky=N)
# navi.grid(row=0, sticky=W)


# root.mainloop()
# root.destroy()


label = Label(frame, text='tab;shift+tab;enter;ctrl+x/c/v;esc\t\tby https://findneo.github.io/')
label.grid(column=1, sticky=W)
frame.grid(row=1, sticky=N)
root.mainloop()
