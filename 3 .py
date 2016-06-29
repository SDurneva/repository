#3 (10 баллов). Для каждого найденного в предыдущем пункте случая отделить
#имя (или инициалы) от фамилии, для каждой фамилии создать отдельную папку,
#а внутри неё для каждого сочетания "инициалы + фамилия" или "имя + фамилия"
#создать текстовый файл с предложением, в котором упоминается это вхождение.

import re
import os

def file_reading():
    f = open('mzamok.txt','r',encoding = 'utf-8')
    string = f.read()
    f.close()
    return string

def search(string):
    hnames = []
    snames = []
    enames = []
    h = re.findall('[^А-Я][^\.] ?([А-Я][а-я]+ ?[А-Я][а-я]+)[^А-Яа-я]',string)
    s = re.findall('[^А-Я][^\.] ?([А-Я][\.] ?[А-Я][\.] ?[А-Я][а-я]+)[^А-Яа-я]',string)
    e = re.findall('[^А-Я][^\.] ?([А-Я][\.] ?[А-Я][а-я]+)[^А-Яа-я]',string)
    if h:
        for piece in h:
            hnames.append(piece)
            for name in hnames:
                print(name)
    if s:
        for piece in s:
            snames.append(piece)
            for name in snames:
                print(name)
    if e:
        for piece in e:
            enames.append(piece)
            for name in enames:
                print(name)
    all = []
    for piece in h and s and e:
        all.append(piece)
    return(all)

def third(h,s,e):
    h1 = '  '.join(h)
    s1 = '  '.join(s)
    e1 = '  '.join(e)
    h1names = []
    s2names = []
    e3names = []
    rt = '[^А-Я][^\.] ?([А-Я][а-я]+)[^А-Яа-я]'
    a = re.findall(rt,h1)
    b = re.findall(rt,h2)
    c = re.findall(rt,h3)
    if h1:
        for piece in a:
            h1names.append(piece)
            for name in h1names:
                os.makedirs(name)
    if s1:
        for piece in b:
            s1names.append(piece)
            for name in s1names:
                os.makedirs(name)
    if e1:
        for piece in c:
            e1names.append(piece)
            for name in e1names:
                os.makedirs(name)

def main():
    third(search(file_reading()))


if __name__ == "__main__":
   main()
