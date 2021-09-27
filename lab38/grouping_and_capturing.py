import re

# reference to captured group:
rx = re.compile(r"(\d+)a\1")

# reference to named captured group:
# rx = re.compile(r"(?P<digit>\d+)a(?P=digit)")

test_strings = [
	"1a1", 	# ok
	"3a2", 	# not
	"34a34" # ok
]


for ts in test_strings:
	m = rx.search(ts)
	if m:
		print(f"{ts} => {m}")
