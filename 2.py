import re

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

def main():
    string = file_reading()
    search(string)

if __name__ == "__main__":
   main()


 
