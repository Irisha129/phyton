# Написать программу с классом Студент, у которого будет 3 атрибута: имя, номер и возраст. Hеобходимо создать пять методов: - для получения данных об имени студента; - для получения данных о возрасте; - для номера студента; - для изменения данных возраста; - для изменения данных группы.

class Student:
   name = " "
   nomer = 0
   age = 0
   
   def nameStud(self):
      print("Name Studenta: ", self.name)
   def nomerStud(self):
      print("Nomer Studenta: ", self.nomer)
   def ageStud(self):
      print("AgeStudenta: ", self.age)

   def reNomerStud(self):
      print("New Nomer Studenta: ")
      self.nomer = int(input())
      
   def reAgeStud(self):
      print("New AgeStudenta: ")
      self.age = int(input())

Student1 = Student()
Student1.name = "Irina"
Student1.nomer = 256
Student1.age = 25

Student1.nameStud()
Student1.nomerStud()
Student1.ageStud()
Student1.reAgeStud() 
Student1.reNomerStud()
