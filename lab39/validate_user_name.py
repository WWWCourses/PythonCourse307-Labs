import re
# TASK:
# A valid user name must follow next rules

# Must consists of 3 to 10 characters inclusive.
# Username can only contain alphanumeric characters, underscores (_) and  dashes (-).
# The first character of the username must be an alphabetic character

user_names = [
  "ada", 	# yes
  "a__", 	# yes
  "a12345",	# yes
  "a1234567890", # no (rule 1)
  "1aaaaaaa",	# no (rule 3)
  "aaa#", 	# no (rule 2)
  "a", 		# no (rule 1)
]

# word characters
# \w === [a-z0-9_]

rx = re.compile(r'^[a-z]\w{2,9}$', re.I)

for un in user_names:
	m = rx.search(un)
	if m:
		print(f'{un} => {m.group()}')
	else:
		print(f'{un} => No match')





