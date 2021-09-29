import  re

name = "Popov Ivan"

rx = re.compile(r'^([A-Z][a-z]+)')

m = rx.search(name)
print( m.groups()[0] )


# "Ivan Popova"

