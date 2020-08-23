class Fruits(object):

    def __init__(self):
        print("this is single constructor")

    def nutrition(self):
        print("this will give required nutrition")

    def fruit_shape(self):
        print("this will give fruit shape")


class Orange(Fruits):

    def __init__(self, value):
        self.value = value
        Fruits.__init__(self)
        print("this is orange ")

    def color(self):
        print("the color of fruits is --->" + self.value)

    def nutrition(self):
        print("this will give vitamin c")

    def fruit_shape(self):
        print('this is having 0 figure ')


orange = Orange("orange")
orange.color()
orange.nutrition()
orange.fruit_shape()

