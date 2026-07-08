# Author: Lauren Huynh
# User ID: llh74
# Date: June 3, 2025
# Program Name: main.py
# Purpose: Simulate a graduation ceremony that includes a program text,
# a list of the recessional, and the stage party

from queue import Queue, PriorityQueue, LifoQueue
from linkedlist import LinkedList, Node
from participants import Participant, Graduate, Faculty, Guest
from graduation import GraduationCeremony

if __name__ == '__main__':
    faculty1 = Faculty("Dr.", "Paul", "Jensen", "Provost")
    faculty2 = Faculty("Dr.", "Jeremy", "Johnson", "Computer Science")
    undergraduate1 = Graduate("Margaret", "Hamilton", "UG", "B.S.", "Mathematics", ["Cum Laude", "Medal of Freedom"])
    undergraduate2 = Graduate("Katherine", "Johnson", "UG", "B.S", "Mathematics", [])
    graduate1 = Graduate("Joy", "Buolamwini", "G", "M.S.", "Media Arts & Sciences", ["Cum Laude"])
    graduate2 = Graduate("Radia", "Perlman", "G", "Ph.D", "Computer Science", [])
    guest1 = Guest("Mr.", "Bob", "Jones", "Amazon")
    
    cer = GraduationCeremony("Drexel", "June 25, 2025")
    cer.addSpeaker(faculty1, 0)
    cer.addSpeaker(faculty2, 1)
    cer.addSpeaker(undergraduate1, 2)
    cer.addGraduate(undergraduate1)
    cer.addGraduate(undergraduate2)
    cer.addGraduate(graduate1)
    cer.addGraduate(graduate2)
    cer.addStagePartyMember(faculty1)
    cer.addStagePartyMember(undergraduate2)
    print(cer.getProgramText())
    print(cer.hasNextSpeaker())
    print(cer.getNextSpeaker())
    print(cer.getNextSpeaker())
    print(cer.getNextSpeaker())
    print(cer.hasNextSpeaker())
    print(cer.hasNextGraduate())
    print(cer.getNextGraduate())
    print(cer.getNextGraduate())
    print(cer.getNextGraduate())
    print(cer.getNextGraduate())
    print(cer.hasNextGraduate())
    print(cer.getRecesssional())
    print(cer.getPhotoManifest())
    
    print(undergraduate1.getFirstName())
    print(undergraduate1.getLastName())
    print(faculty1.getFullName())
    print(faculty1.getSortName())
    print(graduate2.getDesignation())
    print(graduate2.getDegree())
    print(graduate2.getMajor())
    print(graduate2.getDistinctions())
    print(graduate2)
    print(graduate2.getAnnouncerCard())
    print(faculty2)
    print(faculty2.getTitle())
    print(faculty2.getDepartment())
    print(guest1.getTitle())
    print(guest1.getAffiliation())
