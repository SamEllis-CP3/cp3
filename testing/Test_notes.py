from Animlas import animal
def test_get_name():
    testanimal = animal("Bob", "Bobcat", 27, "M", "Epic")
    name = testanimal.get_name()
    assert name == "Bob"

def test_get_namep2():
    testanimal = animal("Jarrod", "Frog", 2, "F", "Legendary")
    name = testanimal.get_name()
    assert name == "Jarrod"


