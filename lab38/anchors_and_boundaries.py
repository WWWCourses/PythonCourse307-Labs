import re

# ^, $, \b

rx = re.compile(r"\btest\b")
test_strings = [
	"test",			# ok
	"test!", 		# ok
	"test,x",		# ok
	"test-ok",		# ok
	"test_ok",		# NOT
	"atestation",	# NOT

]

for ts in test_strings:
	m = rx.search(ts)
	if m:
		print(f"{ts} => {m}")
