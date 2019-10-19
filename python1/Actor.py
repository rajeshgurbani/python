class Actor:

    def __init__(self, name):
        self.name = name

    def act(self):
        print(self.name + ' is dancing')

a1 = Actor('SRK')
a1.act()
print(a1)
a2 = Actor('Rani')
a2.act()
print(a2)
