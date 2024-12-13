from person import Person

##############################################################
# Usage
# This is the Student Class
#
# Example:
# >>> x = Student("Mike", "Olsen", 2019)
# >>> x.welcome()
# >>> x.printname()
#
# This class inherits from the Person Class and builds
# the Student class with additional setters and getters 
# methods to set variables.
#############################################################

class Student(Person):
    '''this is the Student class'''
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
        self.student_id = None
        self.major = None
        self.minor = None
        self.gpa = None
        self.unversity = None
  
    def __str__(self):
        return f"{self.firstname} {self.lastname}" + " " +  str(self.graduationyear)

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
        return f"Welcome {self.firstname} {self.lastname} to the class of" + " " + str( self.graduationyear)

    def set_studentid(self, s_id):
        self.student_id = s_id
        print(f'Student ID is now set: {self.student_id}')

    def get_studentid(self):
        return self.student_id
