import re

text = '''
line1

  line3



  line5
  line6
line7
'''

rx = re.compile(r'[\n\r]{2,}')

replaced  = rx.sub('\n', text)
print(replaced)



