#С помощью регулярных выражений найти и подсчитать все вхождения прилагательных во множественном числе
#(то есть таких разборов, в которых type=" начинается с "l" и содержит "f" на третьей позиции, например: type="lhfosf").
#Результат подсчётов напечатать в открытый для записи файл.
import re

def file_reading():
    f = open('iceland.xml','r',encoding = 'utf-8')
    strings = f.readlines()
    f.close
    return strings

def search(strings):
    adj = []
    for string in strings:
        m = re.search('(type=")1.f.+',string) 
        if m != None:
            adj.append(string)
    return adj

def count(adj):
    f2 = open('adjectives.txt','w',encoding = 'utf-8')
    quant = str(len(adj))
    f2.write(quant)
    f2.close()

def main():
    strings = file_reading()
    adj = search(strings)
    count(adj)

if __name__ == "__main__":
   main()

