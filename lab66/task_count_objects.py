class Base1:
	def __init__(self):
		print('Base1 init')

	def foo(self):
		print('foo in Base1')

class Base2:
	def __init__(self):
		print('Base2 init')

	def foo(self):
		print('foo in Base2')


class A(Base1,Base2):
	count = 0

	def __init__(self):
		super(Base1,self).__init__()
		# super(Base2).__init__()
		print(f'init on A called')

class B(Base1):
	count = 0
	def __init__(self):
		super().foo()
		print(f'init on {self} called')

a1 = A()
# b1 = B()

# OUTPUT:
# Base init
# init on A called
