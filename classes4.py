class Person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(Person):
    def __init__(self, name, idnumber, salary, post):
        Person.__init__(self, name, idnumber)
        self.salary = salary
        self.post = post
a = employee("Tommy Nguyen", 12345, 100000, "Software Engineer")
a.display()
