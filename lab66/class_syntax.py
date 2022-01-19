class A:
    i = 99
    def __init__(self, i=100):
        self.i = i

class B(A):
    def __init__(self, j=0):
        # super().__init__(5)
        self.j = j

def main():
    b = B()
    print(b.i)

    # print(b.j)

main()