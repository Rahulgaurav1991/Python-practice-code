class A:

    def run(self):
        i = 100
        j = "ABC"
        i = j
        print(i, j)

    def run(self, a):
        print("the value of a is --->" + str(a))


a = A()
a.run(10)
