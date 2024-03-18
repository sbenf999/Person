from bag import *

class Ears:
    def __init__(self):
        self.winking = False
        self.eyesClosed = False
        self.blinking = False
    
    def wink(self):
        print("Winking")
        self.winking = True
        
    def closeEyes(self):
        print("I cant see anything")
        self.eyesClosed = True
        
    def blink(self):
        print("Blinking")
        self.blinking = True
        
        
class Nose:
    def smell(self):
        print("Smelling")
        
class Mouth:
    def __init__(self):
        self.lipStickColour = None
    
    def speaks(self):
        print("Speaking")
        
    def changeLipStickColour(self, new):
        self.lipStickColour = new

class Head(Ears, Nose, Mouth):
    def __init__(self, iq=120):
        self.iq = iq
        
    def __str__(self):
        print(f"Winking is {self.winking}, Blinking is {self.blinking}, eyes closed is {self.eyesClosed}, lip stick colour is {self.lipStickColour}")
        
class Person(Head, Bag, Item):
    personID = 0
    attributes = {}
    
    def __init__(self, forname, surname, gender, height, weight, age, middlename=""):        
        self.forname = forname
        self.surname = surname
        self._gender = gender
        self.__height = height
        self.__weight = weight
        self._age = age
        self._middlename = middlename
        self.fullname = self.forname + " " + self._middlename+ " " + self.surname
        
        self.possessions = []
        
        newBag = Bag(maxSize = 20)
        self.possessions.append(newBag)
        
        Person.personID += 1
        self.personID = Person.personID
            
    def getInfo(self, item):
        item = item.lower()
        self.attributes: dict = {
            "forname": self.forname,
            "surname": self.surname,
            "gender": self._gender,
            "height": self.__height,
            "weight": self.__weight,
            "fullname": self.fullname,
            "age": self._age,
            "middlename": self._middlename
        }
        
        return self.attributes[item]

    def set_forname(self, new):
        self.forname = new
        
    def set_surname(self, new):
        self.surname = new
    
    def set_gender(self, new):
        self._gender = new
    
    def set_height(self, new):
        self.__height = new
        
    def set_weight(self, new):
        self.__weight = new
        
    def set_age(self, new):
        self._age = new
        
    def set_middlename(self, new):
        self._middlename = new
        
    def greet(self):
        return f"Hello {self.forname}"
        
    def isTallerThan(self, obj):
        if self.__height > obj.getInfo("height"):
            return True
        elif self.__height == obj.getInfo("height"):
            return None
        else:
            return False
        
    def isOlderThan(self, obj):
        if self._age > obj.getInfo("age"):
            return True
        
        else:
            return False
             
    def greeting(self):
        print(f"Hello, i'm {self.forname} {self.surname}")
    
    def getBMI(self):
        return round((self.__weight/self.__height**2)*10000, 2) 

    def howManyPeople():
        return Person.personID
    
    def shout(text):
        return text.upper()

    def __str__(self):
        return f"{self.forname}, {self._middlename}, {self.surname}, {self._gender}, {self.__height}, {self.__weight}, {self.personID}"
    
    def writeToFile(self, filename="people.txt"):
        tmp = f"{self.personID}, {self.forname}, {self.surname}, {self._gender}, {self.__height}, {self.__weight}, {self._middlename}" 
        file = open("people.txt", "a")
        file.write(tmp + "\n")
        file.close()

    def getBag(self):
        return self.possessions[0]
