from Animlas import animal
def test_get_name():
    testanimal = animal("Bob", "Bobcat", 27, "M", "Epic")
    name = testanimal.get_name()
    assert name == "Bob"

