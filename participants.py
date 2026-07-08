# Author: Lauren Huynh
# User ID: llh74
# Date: June 3, 2025
# Program Name: participants.py
# Purpose: File that contains the abstract class Participant and
# derived classes Graduate, Faculty, and Guest

from abc import ABC, abstractmethod

# abstract participant class
class Participant(ABC):
    def __init__(self, firstName, lastName):
        self.__firstName = firstName
        self.__lastName = lastName
    
    # getter methods
    def getFirstName(self):
        return self.__firstName
    
    def getLastName(self):
        return self.__lastName
    
    def getFullName(self):
        nameStr = ""
        if (isinstance(self, Faculty) or isinstance(self, Guest)) and self.getTitle():
            nameStr += f"{self.getTitle()} "
        nameStr += f"{self.getFirstName()} {self.getLastName()}"
        return nameStr
    
    # returns the name last name, first name
    def getSortName(self):
        return f"{self.getLastName()}, {self.getFirstName()}"
    
    @abstractmethod
    def __str__(self):
        pass
   
# derived class Graduate
class Graduate(Participant):
    def __init__(self, firstName, lastName, designation, degree, major, distinctions):
        super().__init__(firstName, lastName)
        self.__designation = designation
        self.__degree = degree
        self.__major = major
        self.__distinctions = distinctions
    
    # getter methods
    def getDesignation(self):
        return self.__designation
    
    def getDegree(self):
        return self.__degree
    
    def getMajor(self):
        return self.__major
    
    def getDistinctions(self):
        return self.__distinctions
    
    # overloaded method for when it is printed out
    def __str__(self):
        gradStr = f"{self.getFullName()}, {self.getDegree()} in {self.getMajor()}"
        distincList = self.getDistinctions()
        if len(distincList) >= 1:
            gradStr += f", {distincList[0]}"
        if len(distincList) > 1:
            gradStr += "*"
        
        return gradStr
    
    # method that returns the announcer card such as name,
    # degree, major, and distinctions
    def getAnnouncerCard(self):
        cardStr = f"{self.getFullName()}\n- {self.getDegree()} in {self.getMajor()}"
        distincList = self.getDistinctions()
        
        for distinc in distincList:
            cardStr += f"\n- {distinc}"
        return cardStr

# derived class Faculty
class Faculty(Participant):
    def __init__(self, title, firstName, lastName, department):
        super().__init__(firstName, lastName)
        self.__title = title
        self.__department = department
    
    # getter methods
    def getTitle(self):
        return self.__title
    
    def getDepartment(self):
        return self.__department
    
    # prints this out when the object is printed
    def __str__(self):
        return f"{self.getTitle()} {self.getFirstName()} {self.getLastName()}, {self.getDepartment()}"

# derived class Gust
class Guest(Participant):
    def __init__(self, title, firstName, lastName, affiliation):
        super().__init__(firstName, lastName)
        self.__title = title
        self.__affiliation = affiliation
      
    # getter methods
    def getTitle(self):
        return self.__title
    
    def getAffiliation(self):
        return self.__affiliation
    
    # prints this out when the object is printed
    def __str__(self):
        return f"{self.getTitle()} {self.getFirstName()} {self.getLastName()}, {self.getAffiliation()}"
