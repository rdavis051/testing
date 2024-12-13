from student import Student

# Test Student class methods

s = Student("Robert", "Davis", 2019)

def test_firstname():
    assert s.firstname == "Robert"

def test_lastname():
    assert s.lastname == "Davis"

def test_graduationyear():
    assert s.graduationyear == 2019

def test_str():
    assert s.__str__() == "Robert Davis 2019"

def test_welcome():
    assert s.welcome() == "Welcome Robert Davis to the class of 2019"

def test_studentid():
    s.set_studentid('123456789')
    assert s.get_studentid() == '123456789'

