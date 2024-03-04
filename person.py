from bag import *

class Ears:
    def wink(self):
        print("Winking")
        
class Nose:
    def smell(self):
        print("Smelling")
        
class Mouth:
    def speak(self):
        print("Speaking")

class Head(Ears, Nose, Mouth):
    def __init__(self, iq=120):
        self.iq = iq
        
class Person(Head, Bag, Item):
    personID = 0
    
    def __init__(self, forname, surname, gender, height, weight, age, middlename=""):        
        self.forname = forname
        self.surname = surname
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.middlename = middlename
        self.fullname = self.forname + " " + self.middlename+ " " + self.surname
        
        self.possessions = []
        
        newBag = Bag(maxSize = 20)
        self.possessions.append(newBag)
        
        Person.personID += 1
        self.personID = Person.personID
    
    def give_info(self, item):
        item = item.lower()
        attributes: dict = {
            "forname": self.forname,
            "surname": self.surname,
            "gender": self.gender,
            "height": self.height,
            "weight": self.weight,
            "fullname": self.fullname,
            "age": self.age,
            "middlename": self.middlename
        }
        
        return attributes[item]

    def set_forname(self, new):
        self.forname = new
        
    def set_surname(self, new):
        self.surname = new
    
    def set_gender(self, new):
        self.gender = new
    
    def set_height(self, new):
        self.height = new
        
    def set_weight(self, new):
        self.weight = new
        
    def set_age(self, new):
        self.age = new
        
    def set_middlename(self, new):
        self.middlename = new
        
    def greet(self):
        return f"Hello {self.forname}"
        
    def isTallerThan(self, obj):
        if self.height > obj.give_info("height"):
            return True
        elif self.height == obj.give_info("height"):
            return None
        else:
            return False
        
    def isOlderThan(self, obj):
        if self.age > obj.give_info("age"):
            return True
        
        else:
            return False
             
    def greeting(self):
        print(f"Hello, i'm {self.forname} {self.surname}")
    
    def getBMI(self):
        return round((self.weight/self.height**2)*10000, 2) 

    def howManyPeople():
        return Person.personID
    
    def shout(text):
        return text.upper()

    def __str__(self):
        return f"{self.forname}, {self.middlename}, {self.surname}, {self.gender}, {self.height}, {self.weight}, {self.personID}"
    
    def writeToFile(self, filename="people.txt"):
        tmp = f"{self.personID}, {self.forname}, {self.surname}, {self.gender}, {self.height}, {self.weight}, {self.middlename}" 
        file = open("people.txt", "a")
        file.write(tmp + "\n")
        file.close()

    def getBag(self):
        return self.possessions[0]
        

