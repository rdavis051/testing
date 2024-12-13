from person import Person

# Builds employee class

class Employee(Person):
    def __init__(self, fname, lname, company):
        super().__init__(fname, lname)
        self.company = company
        self.employee_id = None
        self.salary = None
        self.title = None

    def __str__(self):
        return f'{self.firstname} {self.lastname} {self.company}'

    def get_company(self):
        print(f'You work for: {self.company}')
        return company

    def set_salary(self, salary):
        self.salary = salary
        print('Your salary is: $' + str(self.salary))

    def get_salary(self):
        if self.salary == None:
            print('Your salary has not been set,')
            print('Set it by using the set_salary() method')
        else:
            print('Your salary is: $' + str(self.salary))
            return self.salary

    def print_salary(self):
        if self.salary == None:
            print('Your salary has not been set,')
            print('Set it by using the set_salary() method')
        else:   
            print(f'Your salary is: ${self.salary}')
            monthly_sal = self.salary/12
            bimonthly_sal = self.salary/24
            biweekly_sal = self.salary/26
            weekly_sal = self.salary/52
            print(f'-Your salary monthly is: ${monthly_sal}')
            print(f'-Your salary bi-monthly is: ${bimonthly_sal}')
            print(f'-Your salary bi-weekly is: ${biweekly_sal}')
            print(f'-Your salary weekly is: ${weekly_sal}')

