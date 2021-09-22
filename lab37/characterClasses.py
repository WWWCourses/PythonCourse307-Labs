import  re

test_strings = [
	"!2324!", # ok
	"!23-4!", # not
	"!23", # not
	"23!", # not
	"@23@", # not
	"!!", # not
]


rx = re.compile(r"!\d+!")

for ts in test_strings:
	res2 = rx.search(ts)
	print(f"{ts} => {res2}")