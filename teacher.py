from person import Person
import secrets

class Teacher(Person):
    #create teacher ID
    teacherID = 0
    
    def __init__(self, taughtSubject, roomTaughtIn, school="Attleborough-Academy", office=False):
        self.taughtSubject = taughtSubject
        self.school = school
        self.roomTaughtIn = roomTaughtIn
        self.office = office
        self.set_forname("Teacher")
        self.emailAddress = self.getInfo("forname") + "@" + self.school + ".com"
        
        Teacher.teacherID += 1
        self.teacherID = Teacher.teacherID
        
    def getInfo(self, item):
        item = item.lower()
        attributes: dict = ({
            "taughtSubject": self.taughtSubject,
            "school": self.school,
            "roomTaughtIn": self.roomTaughtIn,
            "office": self.office,
            "emailAddress": self.emailAddress,
            })
        
        return attributes[item]   
    
    def setSchool(self, newSchool):
        self.school = newSchool
        
    def setRoomTaughtIn(self, newRoom):
        self.roomTaughtIn = newRoom
    
    def setOffice(self, newOffice):
        self.office = newOffice
    
    def __str__(self):
        print(f"{self.taughtSubjects}, {self.school}, {self.roomTaughtIn}, {self.office}, {self.emailAddress}")
        