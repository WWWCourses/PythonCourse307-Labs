import re

text = '''
line1

  line3
# line 4
	#
  line5
  line6
line7
'''

# ---------------- Approach 1: match and capture what we need ---------------- #
rx = re.compile(r'(?m)^\s*([a-z]+)(\d+)')
res = rx.findall(text)

beautified_text = ''

for r in res:
  beautified_text += f'{r[0]}{r[1]}\n'

print(beautified_text)
# ------------------------------------- . ------------------------------------ #


# ------------------- Approach2: strip what we do not need ------------------- #
rx_comment = re.compile(r'^\s*#.*$', re.M)
rx_newlines = re.compile(r'[\n\r]+')
rx_leading_spaces = re.compile(r'^\s+',re.M)

stripped_comments =  rx_comment.sub('', text)
stripped_empty_rows = rx_newlines.sub('\n', stripped_comments)
aligned  = rx_leading_spaces.sub('', stripped_empty_rows)

print(aligned)


