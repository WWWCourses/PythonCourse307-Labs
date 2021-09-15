# TASK: from list1, generate list2, which elements are the squared elements of list1
def transform_elements(item):
	return item**2


list1 = [1,2,3,4]

# Solution with for loop:
# list2 = []
# for i in list1:
# 	list2.append(transform_elements(i))
# print(list2)

# Solution with map:
res  = map(transform_elements, list1)
print(list(res))


