class emp:
    num_of_emp = 0
    amount=1000
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
        self.email=fname + ' . ' + lname

        emp.num_of_emp += 1
    def fullname(self):
        return '{} {}'.format(self.fname,self.lname)
    @classmethod
    def setamount(cls,price):
        cls.amount=price
    @classmethod
    def from_str(cls,e_str):
        fname,lname = e_str_2.split('-')
        return cls(fname,lname)
    @staticmethod
    def is_goodday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return True
        return False        
        




""" print(emp.num_of_emp)
e_1 = emp('siva','raj')
e_2 = emp('raj','siva')
print(e_1.fullname())
emp.setamount(5000)
print(emp.amount) """
e_str_1 = 'john-don'
e_str_2 = 'jane-smith'

new_e_1=emp.from_str(e_str_1)
new_e_2=emp.from_str(e_str_2)
print(new_e_1.fullname())
print(new_e_2.fullname())

import datetime

new_day=datetime.date(2016,7,10)
print(emp.is_goodday(new_day))