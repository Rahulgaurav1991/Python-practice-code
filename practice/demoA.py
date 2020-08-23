class runner(object):
    wheel = 4

    def __init__(self, model, price):
        self.model = model
        self.price = price

    def info(self):
        print("the model of cars is-->" + self.model)
        print("the price of cars is --->" + str(self.price))


c = runner("Tata", 50000)
print(c.info())
print(runner.wheel)
