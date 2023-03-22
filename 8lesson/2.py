# 2. Написать функцию, для удаления всех дубликатов в произвольном массиве. Массив расматриваем как список.

def get_unique(in_list):
   # объявление пустого списка
   unq_list = []
   # Итерация по списку
   for x in in_list:
      # если значения x нету в unq_list то его добавляем
      if x not in unq_list:
         unq_list.append(x)
   # вывод списка
   for x in unq_list:
      print(x, end=" ")   
   print()
   print("Список без дубликатов: " + str(unq_list))
   
# ввод элементов списка
t = []
for i in range(int(input('k: '))):
    t.append(str(input('element '+str(i)+': ')))

print("Список {0} без дубликатов:".format(t))
get_unique(t)
print()




