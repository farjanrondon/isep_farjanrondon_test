
class Triangle():

	def __init__(self, a, b, c):
		self.__a = a
		self.__b = b
		self.__c = c

	def area(self):
		
		import math as mt

		s = (self.__a + self.__b + self.__c) / 2
		A = mt.sqrt(s * (s - self.__a) * (s - self.__b) * (s - self.__c))
		return A

	def my_object(self):
		return f'{self.__a}, {self.__b}, {self.__c}'


triangle1 = Triangle(12, 12, 12)

area1 = triangle1.area()
print(area1)

print(triangle1.my_object())