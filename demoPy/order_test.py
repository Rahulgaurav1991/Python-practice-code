import pytest


def test_B():
    print(" i ma method B")



def test_C():
    print(" i am method c")


@pytest.mark.run(order=1)
def test_A():
    print(" i am method A")
