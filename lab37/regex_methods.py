import re

test_strings = [
	"song.mpr",
	"ng2.abc",
	"abcdef",
	"ab12"
]

rx = re.compile( r"[a-z]{3}" )
for ts in test_strings:
	match = rx.search(ts)
	print( match )
	fa_res = rx.findall(ts)
	print(fa_res, "\n")


