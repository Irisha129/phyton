# 3. Написать функцию, которая будет открывать файл №1 находить в нем целые числа и записывать их в файл №2 

cifry = {0,1,2,3,4,5,6,7,8,9}
f0=open('C:/Users/user/Desktop/Python/phyton/9lesson/t2.txt', 'a')
with open('C:/Users/user/Desktop/Python/phyton/9lesson/t1.txt') as f1:
    print(f1)
    s=[]
    s = f1.readline()
    print(s)

    for stri in f1:
        if len(stri)>0:
           a = len(stri)
           for i in range (0, a-1):
               if stri[i] not in cifry:
                   break
           
           tmp =stri + " "
           f0.write(tmp)
print(f0)
f0.close()

