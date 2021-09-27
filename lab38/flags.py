import re

rx = re.compile(r"""
a
\s* # match whitespace (0 to infinity)
a
""", re.I|re.M|re.S|re.X)
test_strings = [
	"a a",
	"a	a",
	"""a
a"""
]


for ts in test_strings:
	m = rx.search(ts)
	if m:
		print(f"{ts} => OK")