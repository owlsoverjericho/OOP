class Rectangle:
	def __init__(self, length = 1, width = 1):
		self._length = length
		self._width = width
	def perimeter(self):
		print(f"Perimeter:{2 * (self._length + self._width)}")
	def area(self):
		print(f"Area:{self._length * self._width}")
	def set(self, length, width):
		if (length > 0.0 and width > 0.0):
			self._length = length
			self._width = width
		else:
		    print('Both values must be greater than zero')
	def get(self):
		print(f"Length:{self._length}\nWidth:{self._width}")
		
x = Rectangle()

x.set(5, 5)
x.get()
x.perimeter()
x.area()
	
