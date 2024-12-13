import math
from datetime import date, datetime
import mysql.connector

########################################################
# Usage
# This is the Person class
# 
# Example:
# >>> p1 = Person("John", "Doe")
# >>> print(p1.fname)
# >>> print(p1.age)
# >>> print(p1)
# >>> p1.printname()
# >>> p1.myfunc()
#######################################################


class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
        self.age = None
        self.gender = None
        self.dob = None
        self.mydb = None

    def __str__(self):
        return f"{self.firstname} ({self.lastname})"
 
    def set_connect_db(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="rdavis",
            password="robadmin",
            database="people"
        )

        print(self.mydb)

    def insert_record(self):
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO person (firstname, lastname, age, gender, dob) values (%s, %s, %s, %s, %s)"
        val = (self.firstname, self.lastname, self.age, self.gender, self.dob)
        mycursor.execute(sql, val)

        self.mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        

    def printname(self):
        print(self.firstname, self.lastname)

    def myfunc(self):
        print("Hello my first name is " + self.firstname + " : " + " my last name is " + str(self.lastname))
        return f"Hello my first name is {self.firstname} : my last name is {self.lastname}"

    def set_gender(self, gender):
        self.gender = gender
        print(f'Gender was sent to: {self.gender}')

    def get_gender(self):
        return self.gender

    def set_dob(self):
        '''DOB format: YYYY-MM-DD'''
        print("Date of Birth (DOB) format must be: YYYY-MM-DD")
        dob = input("Please enter your DOB: ")
        checked_dob=self.check_dob(dob)
        #dob = str(dob)
        #dob = dob.split('-')
        #print(dob)
        #dob = date(int(dob[0]), int(dob[1]), int(dob[2]))
        #print(dob)
        print("You were born on: " + checked_dob.strftime("%B %d, %Y"))
        self.dob = checked_dob

    def get_dob(self):
        return self.dob
 
    def check_dob(self, dob):
        dob = str(dob)
        dob = dob.split('-')
        dob = date(int(dob[0]), int(dob[1]), int(dob[2]))
        return dob

    def set_age(self):
        if self.dob == None:
            print("you have to set the DOB variable first: ")
            print("run the set_dob() method")
        elif self.age != None:
            print(f'You are {self.age} years old!')
        else:
            print("Your DOB is: " + self.dob.strftime("%B %d, %Y"))
            curr_date = datetime.now()
            curr_date = date(curr_date.year, curr_date.month, curr_date.day)
            print("Today is: " + str(curr_date))
            delta = curr_date - self.dob
            print(f'Difference is {delta.days} days')
            self.age = math.floor(delta.days/365)
            print(f'You are {self.age} years old!')

    def get_age():
        return self.age

