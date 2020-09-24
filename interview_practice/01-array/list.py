# CLASS EXAMPLE
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myName(self):
        print("Hello my name is " + self.name)

def personTest():
    p1 = Person("JOHN", 23)
    p1.myName()

# CLASS DVD
class DVD:
    def __init__ (self, name, releaseYear, director):
        self.name = name
        self.releaseYear = releaseYear
        self.director = director
    
    def __repr__(self):
        return 'info: [name:%s, releaseYear: %s, director: %s]' % (self.name, self.releaseYear, self.director)

    def __str__(self):
        return self.name + ", directed by " + self.director + ", released in " + self.releaseYear

def dvdClient():
    dvdList = []
    d0 = DVD('adrian poopy', '2020', 'adrian')
    d1 = DVD('the chonky', '2012', 'Si')
    d2 = DVD('the alit', '1997', 'alita')
    dvdList.append(d0)
    dvdList.append(d1)    
    print('--------------')

    # insert in specific index, does not remove
    dvdList.insert(0, d2)
    for dvd in dvdList:
        print(dvd)
    print('--------------')
    
    # changes the index
    dvdList[0] = d0
    for dvd in dvdList:
        print(dvd)

    print(dvdList[:2])

def test1():
    list1 = []
    print(len(list1))

test1()