import pytest


def test_valuerahul():
    a = "10"
    print("the value of a is --->" + a)


def test_name():
    text = "$120.00"
    print(text[::-1])


def test_list():
    list = ["rahul","gaurav","test","test"]
    print(len(list))
    print((list.count("test")))
    for i in list:
        print(i)
