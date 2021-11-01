def connect(f, x):
	print("I'll call a function only on even numbers")
	if x%2==0:
		f()

def callback():
	print('I\'m callback')
	return 5


connect( callback, 4)



