# Напишите функцию (имя можете выбрать любое) которая будет сумировать все целые числа от первого до второго параметра, если первый параметр будет больше второго, то поменяйте их местами.

x = int(input('x = '))
y = int(input('y = '))

def summAB(a, b):
    if a > b:
        n = a
        a = b
        b = n
    sum = 0
    for i in range(a, b+1):
        sum += i
    return sum

s = summAB(x, y)
print('S = ',s)
