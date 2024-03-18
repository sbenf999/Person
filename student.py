from person import *
import random

class Student(Person):
    #create student ID
    studentID = 0

    #create candidate number
    usedCandidateNumbers = []
    candidateNumber = random.randint(1001, 9999)
    
    while candidateNumber in usedCandidateNumbers:
        candidateNumber = random.randint(1001, 9999)
    
    usedCandidateNumbers.append(candidateNumber)
    
    def __init__(self, subjects, score=0, candidateNumber=usedCandidateNumbers[len(usedCandidateNumbers)-1], detentions=[]):
        self.score = score
        self.candidateNumber = candidateNumber
        self.subjects = subjects
        self.detentions = detentions
        self.detentionsCount = 0
        self.detentionRemoved = False
        
        Student.studentID += 1
        self.studentID = Student.studentID
    
    def setScore(self, newScore):
        self.score = newScore
        
    def addDetention(self, detention: str):
        modifier = 0
        if sscoreelf.detentionRemoved == True:
            modifier = 1
            
        identifier = "D" + str(detentionsCount+modifier)
        self.detentions.append([identifier, newDetention])
        self.detentionsCount += 1
        print(f"Detention identifier: {identifier}")
        
    def removeDetention(self, identifier: str):
        for detention in self.detentions:
            if detention[0] == identifier:
                self.detentions.remove(detentions)
                self.detentionsCount -= 1
                self.detentionRemoved = True
                print(f"Detention with identifier {identifier} removed")
    
    def getInfo(self, item):
        item = item.lower()
        attributes.update({
            "score": self.score,
            "candidateNumber": self.candidateNumber,
            "subjects": self.subjects,
            "detentions": self.detentions,
            "detentionsCount": self.detentionsCount,
            "detentionRemoved": self.detentionRemoved
            })
        
        return attributes[item] 
                
    def addSubject(self, newSubject: str):
        self.subjects.append(newSubject)

    def __str__(self):
        print(f"{self.studentID}, {self.candidateNumber}, {self.subjects}, {self.detentions}")