# TASK: print line by line the ocntent of readme.txt file:
from os import getcwd
import os.path

print(getcwd())


file_name = 'readme.txt'
abs_file_path = '/home/nemsys/projects/courses/netIT/PythonCourseNetIT/PythonCourse307-Labs/lab55/my_python_project/data/'
relative_file_path = './data/'

# print(abs_file_path+file_name)

with open(relative_file_path+file_name) as f:
	print( f.read())

