# 2. Напишите функцию, которая будет выводить информацию о всех файлах и подкаталогах в произвольной папке на вашем пк


# Способ 1
import os
os.chdir('9lesson')
print(os.listdir('c://'))
print(os.getcwd())

# Способ 2
def info(path):
    print(os.listdir(path))

info('C://')

