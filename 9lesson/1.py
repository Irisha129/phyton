# 2. Напишите функцию, которая будет открывать заранее созданый тхт файл и выводить содержимое на экран (тхт создать самим и наполнить)

# Способ 1
import os
def openfile(file):
    with open(file) as document:
        read_file = document.read()
    print(read_file)

openfile('C:/Users/user/Desktop/Python/phyton/9lesson/t1.txt')

# Способ 2
with open('C:/Users/user/Desktop/Python/phyton/9lesson/t1.txt') as f1:
    rf = f1.read()
    print(rf)

