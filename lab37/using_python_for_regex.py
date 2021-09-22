import re

# ---------------------- compiled vs re modules methods ---------------------- #
# pattern = r"[a-z]+"
# test_string = "23bfhfd"


# # test for match - variant 1:
# regex = re.compile(pattern)
# res1 = regex.search(test_string)
# print(res1)

# # test for match - variant 2:
# res2 = re.search(pattern, test_string)
# print(res2)


# ----------------------- match multiple test strigns: ----------------------- #
pattern = r"[a-z]+"
test_strings = [
	"abdnfjdhjd",
	"hdfj3434hjd",
	"3244354"
]

# this is not efficient
# for ts in test_strings:
# 	res2 = re.search(pattern, ts)
# 	print(res2)

# more efficient (first compile the regex)
rx = re.compile(pattern)
for ts in test_strings:
	res2 = rx.search(ts)
	print(res2)


