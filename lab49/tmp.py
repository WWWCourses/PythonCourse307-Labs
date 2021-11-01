# def connect(f, x):
# 	print("I'll call a function only on even numbers")
# 	if x%2==0:
# 		f(x**2)

# def callback(x):
# 	print(x)


# connect( callback, 4)

def caller(f):
	print(f(3))

# def greet():
# 	print('Hello')


# lambda arguments : expression

# def foo(x):
# 	return x**2

# caller(foo)
caller( lambda x: x**2 )




