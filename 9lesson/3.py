# 3. Написать функцию, которая будет открывать файл №1 находить в нем целые числа и записывать их в файл №2 
# https://youtu.be/p7Csikz-Fk8
# Способ 2

import re

with open('C:/Users/user/Desktop/Python/phyton/9lesson/t1.txt', "r") as f1:
    with open('C:/Users/user/Desktop/Python/phyton/9lesson/t2.txt', "w") as f2:
        for i in f1:
            nums = re.findall(r"\b[1-9][0-9]*\b",i)
            if nums:
                f2.write(" ".join(nums) + "\n")
        
print(f2)

# ____________________
# Способ 1
with open('C:/Users/user/Desktop/Python/phyton/9lesson/t1.txt', "r") as file1:
    content = file1.read()
    numbers = " "
    for i in content:
        if i.isdigit():
            numbers += i
        if numbers:
            with open('C:/Users/user/Desktop/Python/phyton/9lesson/t2.txt', "w") as file2:
                file2.write(numbers)

