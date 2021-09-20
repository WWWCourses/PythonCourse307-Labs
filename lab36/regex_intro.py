import re

pattern = r"[A-Za-z0-9]\+[0-9]"

test_strings = [
	"2+2", # not
	"a+b", # not
	"a+3", # ok
	"c+9", # ok
	"gdahgahsa2"
]

for ts in test_strings:
	# do the test for each string:
	match = re.search(pattern, ts)

	if match:
		print(f"{ts} => OK")
	else:
		print(f"{ts} => NOT OK")


