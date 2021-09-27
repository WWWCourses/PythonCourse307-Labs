import re

# ^, $, \b

#TASK: match strings containing only letters and numbers, at least 3 symbols long
rx = re.compile(r"^[a-z0-9]{3,}$", re.I)
test_strings = [
	"a_a",			# not ok
	"aa", 			# not ok
	"ada123", 		# ok
	"ada", 			# ok
	"ada!", 		# not
	"ada 123", 		# not
]


for ts in test_strings:
	m = rx.search(ts)
	if m:
		print(f"{ts} => OK")
