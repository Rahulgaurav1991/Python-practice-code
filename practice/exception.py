from traceback import print_stack


class Demo:

    def value(self):
        try:
            a = 10
            b = 20
            d = 30

            print((a + b) / 0)

        except:
            raise Exception

    def practice(self):
        try:
            cars = {"make": "Bmw", "Model": "Automatic", " Year": " 2012"}
            print(cars["color"])

        except:
            print("this key not present ")
            print_stack()
        finally:
            print("please close the file")


demo = Demo()
demo.practice()
