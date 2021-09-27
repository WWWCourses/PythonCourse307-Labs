import re

rx = re.compile(r"\btom|jerry\b")
test_strings = [
	"he is tom",	# ok
	"atom!", 		# not ok
	"toma",			# not
	"jerry is ..",	# ok
	"jerrys",		# not ok
]

for ts in test_strings:
	m = rx.search(ts)
	if m:
		print(f"{ts} => {m}")
