from person import Person

# This is a test for the Person class
# Instantiates a Person Object
p=Person("John", "Doe")

def test_firstname():
    assert p.firstname == "John"

def test_lastname():
    assert p.lastname == "Doe"

def test_age():
    p.age = 34
    assert p.age == 34

def test_str():
    assert p.__str__() == "John (Doe)"

def test_myfunc():
    assert p.myfunc() == "Hello my first name is John : my last name is Doe" 

def test_gender():
    p.set_gender('male')
    assert p.gender == "male"

   
