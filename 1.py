import re

def file_reading():
    f = open('mzamok.txt','r',encoding = 'utf-8')
    string = f.read()
    f.close()
    return string

def search(string):
    names = []
    m = re.findall('[^А-Я][^\.] ?([А-Я][\.] ?[А-Я][а-я]+)[^А-Яа-я]',string)              
    if m:
        for piece in m:
            names.append(piece)
            for name in names:
                print(name)

def main():
    string = file_reading()
    search(string)

if __name__ == "__main__":
   main()


