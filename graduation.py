# Author: Lauren Huynh
# User ID: llh74
# Date: June 3, 2025
# Program Name: graduation.py
# Purpose: File that contains the GraduationCeremony class that
# includes adding graduates, speakers, and stage party members and
# a program text and a recessional

from queue import Queue, PriorityQueue, LifoQueue
from linkedlist import LinkedList, Node

class GraduationCeremony:
    def __init__(self, university, date):
        self.__university = university
        self.__date = date
        self.__speakers = PriorityQueue()
        self.__graduates = Queue()
        self.__undergraduates = Queue()
        self.__stageParty = LifoQueue()
        self.__photoManifest = LinkedList()
    
    # adds a graduate, speaker, or stage party member to
    # the corresponding attribute
    def addGraduate(self, graduate):
        if graduate.getDesignation() == "UG":
            self.__undergraduates.put(graduate)
        elif graduate.getDesignation() == "G":
            self.__graduates.put(graduate)
    
    def addSpeaker(self, speaker, priority):
        self.__speakers.put((priority, speaker))
    
    def addStagePartyMember(self, participant):
        self.__stageParty.put(participant)
    
    # prints out a program text that includes speakers,
    # graduates, and undergraduates
    def getProgramText(self):
        tempSpeakersQ = PriorityQueue()
        tempGradsQ = Queue()
        tempUndergradsQ = Queue()
        unsortedGradNames = []
        unsortedUndergradNames = []
        sortedGradNames = []
        sortedUndergradNames = []
        programStr = f"{self.__university} Commencement Ceremony\n{self.__date}\n"
        
        programStr += "\nSpeakers:"
        while not self.__speakers.empty():
            speaker = self.__speakers.get()
            programStr += f"\n- {speaker[1]}"
            tempSpeakersQ.put((speaker[0], speaker[1]))
        
        while not tempSpeakersQ.empty():
            speaker = tempSpeakersQ.get()
            self.__speakers.put((speaker[0], speaker[1]))
        
        programStr += "\n\nGraduate Students:"
        while not self.__graduates.empty():            
            graduate = self.__graduates.get()
            tempGradsQ.put(graduate)
            unsortedGradNames.append(graduate)
        
        for graduate in unsortedGradNames:
            isInserted = False
            for i in range(len(unsortedGradNames)):
                if graduate.getSortName() < unsortedGradNames[i].getSortName():
                    sortedGradNames.insert(i, graduate)
                    isInserted = True
                    break
            if not isInserted:
                sortedGradNames.append(graduate)
        
        for name in sortedGradNames:
            programStr += f"\n- {name}"
        
        while not tempGradsQ.empty():
            self.__graduates.put(tempGradsQ.get())
        
        programStr += "\n\nUndergraduate Students:"
        while not self.__undergraduates.empty():
            undergrad = self.__undergraduates.get()
            tempUndergradsQ.put(undergrad)
            unsortedUndergradNames.append(undergrad)
        
        for undergrad in unsortedUndergradNames:
            isInserted = False
            for i in range(len(unsortedUndergradNames)):
                if undergrad.getSortName() < unsortedUndergradNames[i].getSortName():
                    sortedUndergradNames.insert(i, undergrad)
                    isInserted = True
                    break
            if not isInserted:
                sortedUndergradNames.append(undergrad)
        
        for name in sortedUndergradNames:
            programStr += f"\n- {name}"
            
        while not tempUndergradsQ.empty():
            self.__undergraduates.put(tempUndergradsQ.get())
        
        return programStr
    
    # return true if there is another speaker
    def hasNextSpeaker(self):
        return not self.__speakers.empty()
    
    # gets the next speaker that has the next priority
    def getNextSpeaker(self):
        speaker = self.__speakers.get()
        self.__photoManifest.append(speaker[1])
        return speaker[1]
    
    # return true if there is another graduate waiting to walk
    def hasNextGraduate(self):
        return not self.__graduates.empty()
    
    # gets the next graduate; if there is a graduate waiting
    # to walk, return that graduate then return undergraduate
    def getNextGraduate(self):
        graduate = None
        
        if not self.__graduates.empty():
            graduate = self.__graduates.get()
        elif not self.__undergraduates.empty():
            graduate = self.__undergraduates.get()
        
        if graduate:
            self.__photoManifest.append(graduate)
            
        return graduate
    
    # returns a list of stage party members
    def getRecesssional(self):
        partyList = []
        while not self.__stageParty.empty():
            member = self.__stageParty.get()
            if isinstance(member, tuple):
                partyList.append(member[1])
            else:
                partyList.append(member)
            
        return partyList
    
    # returns the photo manifest
    def getPhotoManifest(self):
        return self.__photoManifest.getHead()
