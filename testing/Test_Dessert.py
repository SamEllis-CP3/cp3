from Dessert_Shop import *

def test_candy():
    testweight = Candy("Jolly Ranchers", 2, 6.50)
    weight = testweight.get_name()
    assert weight == 2