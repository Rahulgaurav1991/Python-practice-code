class cars(object):

    def __init__(self):
        print(" this is single constructor")

    def start(self):
        print("the cars starts")

    def stop(self):
        print("the cars stop")


class BMW(cars):
    def __init__(self):
        cars.__init__(self)
        print("the instance of sub class")

    def drive(self):
        print("the cars driver")


bmw = BMW()
bmw.start()
bmw.drive()
bmw.stop()
