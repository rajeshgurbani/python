class Person:
    count=0
    def __init__(self):
        Person.count += 1

    def numberOfObjectsCreated(self):
        print('Number of objects created of this class ' + str(Person.count))

p1 = Person()
p2 = Person()
p3 = Person()
p4 = Person()
p5 = Person()

Person.numberOfObjectsCreated()