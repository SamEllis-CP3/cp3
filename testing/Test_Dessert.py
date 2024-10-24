from Dessert_Shop import *

def test_candy():
    testcandy_1 = Candy("Jolly Ranchers", 2, 6.50)
    testcandy_2 = Candy("M&M", 1, 7.25)
    testcandy_3 = Candy("Jelly Beans", 27, 3.50)
    
    assert testcandy_1.get_weight() == 2
    assert testcandy_1.get_cost() == 6.50
    assert testcandy_1.get_name() == "Jolly Ranchers"

    assert testcandy_2.get_weight() == 1
    assert testcandy_2.get_cost() == 7.25
    assert testcandy_2.get_name() == "M&M"

    assert testcandy_3.get_weight() == 27
    assert testcandy_3.get_cost() == 3.50
    assert testcandy_3.get_name() == "Jelly Beans"


def test_cookie():
    test_cookies_1 = Cookie("choclate chip", 36, 3.75)
    test_cookies_2 = Cookie("Snicker doodle", 24, 5.50)
    test_cookies_3 = Cookie("Sugar", 48, 3.50)
    
    assert test_cookies_1.get_amount() == 36
    assert test_cookies_1.get_cost() == 3.75
    assert test_cookies_1.get_name() == "choclate chip"

    assert test_cookies_2.get_amount() == 24
    assert test_cookies_2.get_cost() == 5.50
    assert test_cookies_2.get_name() == "Snicker doodle"

    assert test_cookies_3.get_amount() == 48
    assert test_cookies_3.get_cost() == 3.50
    assert test_cookies_3.get_name() == "Sugar"


def test_ice_cream():
    test_icecream_1 = IceCream("Starwberry", 2, 2.50)
    test_icecream_2 = IceCream("Chocolate", 3, 1.75)
    test_icecream_3 = IceCream("Pecan", 1, 3.50)
    
    assert test_icecream_1.get_cost() == 2.50
    assert test_icecream_1.get_scoop() == 2
    assert test_icecream_1.get_name() == "Starwberry"

    assert test_icecream_2.get_cost() == 1.75
    assert test_icecream_2.get_scoop() == 3
    assert test_icecream_2.get_name() == "Chocolate"

    assert test_icecream_3.get_cost() == 3.50
    assert test_icecream_3.get_scoop() == 1
    assert test_icecream_3.get_name() == "Pecan"

def test_sundae():
    test_sun1 = Sundae("Starwberry", 2, 2.50, "sprinkles", 0.25)
    test_sun2 = Sundae("Chocolate", 3, 1.75, "Fudge", 0.75)
    test_sun3 = Sundae("Pecan", 1, 3.50, "Nuts", 0.50)
    
    assert test_sun1.get_cost() == 2.50
    assert test_sun1.get_scoop() == 2
    assert test_sun1.get_name() == "Starwberry"
    assert test_sun1.get_topping() == "sprinkles"
    assert test_sun1.get_topping_price() == 0.25

    assert test_sun2.get_cost() == 1.75
    assert test_sun2.get_scoop() == 3
    assert test_sun2.get_name() == "Chocolate"
    assert test_sun2.get_topping() == "Fudge"
    assert test_sun2.get_topping_price() == 0.75

    assert test_sun3.get_cost() == 3.50
    assert test_sun3.get_scoop() == 1
    assert test_sun3.get_name() == "Pecan"
    assert test_sun3.get_topping() == "Nuts"
    assert test_sun3.get_topping_price() == 0.50

    

