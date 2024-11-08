class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Nom: ", self.name)
        print("Age: ", str(self.age))

class Employee(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def display_details(self):
        Person.display_details(self)
        print("Salaire: ", str(self.salary))

if __name__ == '__main__':
    bob = Employee("Bob", 31, 42000)
    bob.display_details()