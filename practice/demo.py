cars = {"model": "BMW", "engine": "automatic", "tyres": "radiane"}

print(cars.items())
print(cars.keys())
print(len(cars))
for k, v in cars.items():
    print(k + " " + v)

print()
car = (1, 2, 3)
for items in car:
    print(items)

print(len(car))


def sum_value(a, b):
    return a + b


print("the addition of two number is--->" + str(sum_value(1, 2)))

print(type(909))
print(type("hello"))

print(max(2, 99, 10))


def find_tax(gross, statevalue):
    state = {"NY": 10, " mixco": 20, " CA": 30}

    net = gross - (gross * .10)
    if statevalue in state:
        net = net - (gross * state[statevalue] / 100)
        print("the net value is:-->" + str(net))
        return net
    else:
        return None


find_tax(1000000, "NY")

a = 20.14
print(int(a))
print(type(a))
