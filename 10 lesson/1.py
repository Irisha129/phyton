# Написать программу с классом One и создать два атрибута a и b . Написать 4 метода (умножение, сложение, деление и вычитание). Необходимо выполнить эти действия при передаче в методы параметров a и b.
class One:
   a = 1
   b = 1
   def umnoj(self):
      print("Proizvedenie =", self.a * self.b)
   def summa(self):
      print("Summa =", self.a + self.b)
   def razn(self):
      print("Raznost =", self.a - self.b)
   def delenie(self):
      if self.b != 0:
        print("Delenie =", self.a % self.b)

One1 = One()
One1.a = 15
One1.b = 20
One1.umnoj()
One1.summa()
One1.razn() 
One1.delenie()