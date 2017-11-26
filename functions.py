# -*-coding:utf8 -*-
# https://findneo.github.io/
import base64
import re
import hashlib

en_ascii = de_ascii = (lambda x: x)
en_base64 = lambda s: base64.b64encode(s)
en_base32 = lambda s: base64.b32encode(s)
de_base64 = lambda s: base64.b64decode(s)
de_base32 = lambda s: base64.b32decode(s, casefold=True)
en_lower = de_upper = de_lower = lambda s: s.lower()
en_upper = lambda s: s.upper()
en_rev = de_rev = lambda s: s[::-1]
en_md5 = lambda s: hashlib.md5(s).hexdigest() if s != '' else ""
de_md5 = de_rot = de_zhalan = lambda s: ""
en_morse = de_morse = lambda s: morse(s) if s != '' else ""
en_rot = lambda s: caesar(s) if s != '' else ""
en_zhalan = lambda s: rail_fence(s) if s != '' else ""


def rail_fence(s):
    ll = len(s)
    res = dict()
    res[1] = "total len=" + str(ll)
    for i in range(2, ll):
        r = ''
        if ll % i == 0:
            for j in range(i):
                for k in range(ll / i):
                    r += s[k * i + j]
            res[i] = r
    return res

# test
# print railFence('hello world , 2017 ! ')
# {1: 'hello world , 2017 ! ', 3: 'hlwl,0 eood 1!l r 27 ', 7: 'ho2er0ll1ld7o   ,!w  '}


def en_oct(s):
    return ' '.join([oct(ord(i))[1:].zfill(3) for i in s])


def de_oct(s):
    s = re.sub('\s+', '', s)
    for i in s:
        if i not in '01234567':
            return ""
    t = s.zfill(len(s) / 3 * 3 + 3 if len(s) % 3 else len(s))
    return ''.join([chr(int(i, 8)) for i in re.match(len(t) / 3 * '(.{3})', t).groups()])


def en_dec(s):
    return ' '.join([str(ord(i)) for i in s])


def de_dec(s):
    s = re.sub('\s+', ' ', s.strip())
    for i in s:
        if i not in '0123456789 ':
            return ""
    return ''.join(chr(int(i)) for i in s.split(' '))


def en_bin(s):
    return ' '.join([bin(ord(i))[2:].zfill(8) for i in s])


def de_bin(s):
    s = re.sub('\s+', '', s)
    for i in s:
        if i not in '01':
            return ""
    t = s.zfill(len(s) / 8 * 8 + 8 if len(s) % 8 else len(s))
    return ''.join([chr(int(i, 2)) for i in re.match(len(t) / 8 * '(.{8})', t).groups()])


def en_hex(s):
    # t = base64.b16encode(s)
    # return ' '.join(re.match(len(t) / 2 * '(..)', t).groups())
    return ' '.join([hex(ord(i))[2:] for i in s])


def de_hex(s):
    # s = ''.join([i for i in s if i in '0123456789ABCDEFabcdef'])
    # s = '0' + s if len(s) % 2 else s
    # return base64.b16decode(s, casefold=True)
    s = ''.join([bin(int(i, 16))[2:].zfill(4)
                 for i in s if i in '0123456789ABCDEFabcdef'])
    return de_bin(s)


def en_int(s):
    if s == '':
        return ""
    t = ''.join([bin(ord(i))[2:].zfill(8) for i in s])
    return int(t, 2)


def de_int(s):
    if s == '':
        return ""
    return de_bin(bin(int(s))[2:])


def en_url(s):
    todo = ["!", "#", "$", "&", "'",
            "(", ")", "*", "+", ",", "/", ":", ";", "=", "?", "@", "[", "]", " "]
    return ''.join([i if i not in todo else "%" + hex(ord(i))[2:] for i in s])


def de_url(s):
    real_len = len(s) - 2 * len(re.findall('%[0-9a-fA-F]{2}', s))
    # print real_len, len(re.findall('%[^%]{2}', s))
    return ''.join([i if len(i) == 1 else chr(int(i[1:], 16))
                    for i in re.match("(%[0-9a-fA-F]{2}|[ -~])" * real_len, s).groups()])


def en_html(s):
    d = {'"': "&quot;", "'": "&apos;", '<': "&lt;", '>': "&gt;"}
    return ''.join([d[i] if i in '\'"<>' else i for i in s.replace('&', "&amp;")])


def de_html(s):
    s = s.replace('&amp;', '&').replace('&lt;', '<').replace(
        '&gt;', '>').replace('&quot;', '"').replace('&apos;', "'")
    return s.replace('&amp', '&').replace('&lt', '<').replace(
        '&gt', '>').replace('&quot', '"').replace('&apos', "'")


def morse(s):
    morseChart = ['.-',       '-...',     '-.-.',     '-..',      '.',        '..-.',     '--.',
                  '....',     '..',       '.---',     '-.-',      '.-..',     '--',       '-.',
                  '---',      '.--.',     '--.-',     '.-.',      '...',      '-',        '..-',
                  '...-',     '.--',      '-..-',     '-.--',     '--..',     '-----',    '.----',
                  '..---',    '...--',    '....-',    '.....',    '-....',    '--...',    '---..',
                  '----.',    '.-.-.-',   '--..--',   '..--..',   '-....-',   '.----.',   '---...',
                  '.-..-.',   '-..-.',    '.--.-.',   '-.-.-.',   '-...-',    '-.-.--',   '..--.-',
                  '-.--.',    '-.--.-',   '...-..-',  '.-...',    '.-.-.',    ' ',        '*'
                  ]
    alphaChart = ['a',        'b',        'c',        'd',        'e',        'f',        'g',
                  'h',        'i',        'j',        'k',        'l',        'm',        'n',
                  'o',        'p',        'q',        'r',        's',        't',        'u',
                  'v',        'w',        'x',        'y',        'z',        '0',        '1',
                  '2',        '3',        '4',        '5',        '6',        '7',        '8',
                  '9',        '.',        ',',        '?',        '-',        "'",        ':',
                  '"',        '/',        '@',        ';',        '=',        '!',        '_',
                  '(',        ')',        '$',        '&',        '+',        ' ',        '#'
                  ]

    # or as a dict ->  {c[1][i]: c[0][i] for i in xrange(len(c[0]))}
    c = [morseChart, alphaChart]

    s = s.strip().lower()

    # replace characters not in alphaChart with '#' ,which shall be '*' in
    # encoded string
    s = re.sub('[^a-z0-9.,?\-\':"/@;=!_()$&+ ]', '#', s)

    # for convenience sake, I choose not to deal with space in morse.
    s = re.sub('\s+', ' ', s)

    m = 1  # default to decode
    # if mot mismatch that condition,we are to encode.
    if not re.match('[^-._ ]', s):
        # occasionally we meet [ ._]+ instead of [ .-]+
        s = s.replace('_', '-')
        s = re.split(' ', s)
        m = 0  # we are  to encode by morse

    r = []
    # list().extend(foo) returns None so we use 'or r'
    return (m * ' ').join(r.extend([c[1 - m][c[m].index(i)] for i in s]) or r)

# test
# print morse('Hello word,2017!')
# print morse('.... . .-.. .-.. ---   .-- --- .-. -.. --..-- ..--- -----
# .---- --... -.-.--')


def caesar(s):
    cycle = 26
    res = []
    for offset in range(26):
        r = ''
        for i in str(s):
            if 'a' <= i <= 'z':
                r += chr((ord(i) - ord('a') + offset) % cycle + ord('a'))
            elif 'A' <= i <= 'Z':
                r += chr((ord(i) - ord('A') + offset) % cycle + ord('A'))
            else:
                r += i
        res.append([offset, r])
    present = '\t'.join(['13:' + res[13][1]] +
                        [str(i[0]) + ":" + i[1] for i in res if i[0] != 13])
    return present

# test
# print caesar('h3llo')
#[  [0, 'h3llo'], [1, 'i3mmp'], [2, 'j3nnq'], [3, 'k3oor'], [4, 'l3pps'], [5, 'm3qqt'], [6, 'n3rru'], [7, 'o3ssv'],
#   [8, 'p3ttw'], [9, 'q3uux'], [10, 'r3vvy'], [11, 's3wwz'], [12, 't3xxa'], [13, 'u3yyb'], [14, 'v3zzc'],
#   [15, 'w3aad'], [16, 'x3bbe'], [17, 'y3ccf'], [18, 'z3ddg'], [19, 'a3eeh'], [20, 'b3ffi'], [21, 'c3ggj'],
#   [22, 'd3hhk'], [23, 'e3iil'], [24, 'f3jjm'], [25, 'g3kkn']]
