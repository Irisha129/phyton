# 3. Напишите функцию, которая берет 2 списка сравнивает их и если есть хотя бы 1 общей компонент выводит надпись TRUE

def sravnenie(list1,list2):
   # Итерация по списку
   for x in list1:
      # если значения x есть в list2, то выводим надпись TRUE
      if x in list2:
         print("TRUE")
         break 
   
# ввод элементов списков
s1 = []
print("Вводим список1")
for i in range(int(input('Количество элементов: '))):
    s1.append(str(input('element '+str(i)+': ')))
s2 = []
print("Вводим список2")
for i in range(int(input('Количество элементов: '))):
    s2.append(str(input('element '+str(i)+': ')))
sravnenie(s1,s2)
print()

