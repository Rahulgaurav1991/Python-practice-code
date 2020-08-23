class cars(object):

    def __init__(self):
        print("this is single constructor")

    def start(self):
        print("the cars starts")

    def stop(self):
        print("the cars stop")

    def carName(self):
        print("this is Maruthi cars")


class BMW(cars):
    def __init__(self):
        cars.__init__(self)  ### constructor calling process
        print("the instance of sub class")

    def drive(self):
        print("the cars driver")

    def start(self):
        super(BMW, self).start()
        print("Bmw started ")

    def carName(self):
        print("car name is Bmw")


bmw = BMW()
bmw.start()
bmw.drive()
bmw.stop()
bmw.carName()
