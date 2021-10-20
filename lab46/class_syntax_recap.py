# the base class
class Person:
	def __init__(self,name, age):
		print(f'Person constructor execute')
		self.name = name
		self.age = age

	def greet(self):
		print(f'Hi, I\'m {self.name}. I\'m {self.age} years old!')


# the derived class, which inherits from base class:
class Student(Person):
	def __init__(self,name, age):
		print(f'Student constructor execute')
		super().__init__(name, age)


pesho = Student(name="Petar", age=23)
maria = Student("Maria", 21)

pesho.greet()
maria.greet()


