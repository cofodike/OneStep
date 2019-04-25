import re
import datetime
import pandas as pd

class setCourse:
    def __init__(self, courseID):
        self.courseID = courseID # <----- Defines the user course though input. Modify it to take input from the GUI as a command
        return
    
    def searchCourse(self):
        courseMatches = []
        if self.courseID in courseList:
            print(self.courseID) # <----- Shows the course the user was looking for. Modify it to show it in the GUI rather than in the Shell
        else:
            for i in range(len(courseList)):
                check_room = re.search(self.courseID, courseList[i]) # Finds courses that start with what the user has input
                if check_room is not None:
                    courseMatches.append(courseList[i]) # Adds possible courses that the user may be looking for
            for j in range(len(courseMatches)):
                print(courseMatches[j]) # <----- Shows the course Suggestions to the user. Modify it to show it in the GUI rather than in the Shell
        return
    
class setRoom:
    def __init__(self, roomID):
        self.roomID = roomID # <---- Defines the user room thorugh input. Modify it to take input from the GUI as a command
        return      
        
    def searchRoom(self):
        roomMatches = []
        if self.roomID in roomList:
            print(self.roomID) # <---- Shows the room the user was looking for. Modify it to show it in the GUI rather than in the Shell
        else:
            for i in range(len(roomList)):
                check_room = re.search(self.roomID, roomList[i]) # Finds courses that start with what the user has input
                if check_room is not None:
                    roomMatches.append(roomList[i]) # Adds possible courses that the user may be looking for
            for j in range(len(roomMatches)):
                print(roomMatches[j]) # <---- Shows the course Suggestions to the user. Modify it to show it in the GUI rather than in the Shell
        return
    
class setDate:
    # Defaul values for month and year are the current date
    def __init__(self, month = datetime.datetime.now().strftime("%m"), year = datetime.datetime.now().strftime("%Y")):
        # Get values of day, month, year from the user as inputs from GUI
        #-------------------------------------------------------------------------------------------------------------
        self.month = month
        self.year = year
        #-------------------------------------------------------------------------------------------------------------
        return
    
    def combineDate(self):
        convertDate = str(self.month + "/" + self.year) # Convince month, day, and year
        date = datetime.datetime.strptime(convertDate, "%m/%Y") # Converts the previous date to a MM/DD/YYYY format
        return date

class setDays: # Sets the days of the meeting
    def __init__(self):
        self.day = "" # This variable will be a string conteining all the days the user wants a meeting to occur
        return
                
    def weekDays(self, day, m = False, t= False, w = False, th = False, f = False, s = False, sun = False): # <---- Change m,t,w,th,f,s,sun values to True if the user wants a meeting that day
        # If the user wants to input a date rather than choosing a day, change the value of 'day' to the user's value
        # m,t,w,th,f,s,sun represent the days of the week. Turn to true to add them as a meeting day.
        if m or t or w or th or f or s or sun:
            if m:
                self.day.append("Monday ")
            if t:
                self.day.append("Tuesday ")
            if w:
                self.day.append("Wednesday ")
            if th:
                self.day.append("Thursday ")
            if f:
                self.day.append("Friday ")
            if s:
                self.day.append("Saturday ")
            if sun:
                self.day.append("Sunday")
        else:
            self.day.append(day.strftime("%A")) # If the user enters a date the
            
class setTime:
    def __init__(self):
        self.startHours = None
        self.endHours = None
        self.startMin = None
        self.endMin = None
        return
        
    def checkTime(self, startHours, startMin, endHours, endMin, start_PM = False, end_PM = False): 
        # Get values from the user in hours
        #-------------------------------------------------------------------------------------------------------------
        if ((startHours <= 12) and (endHours <= 12)) and (startHours != 0) and (endHours != 0): # The time format can only be between 0 and 12
            if (startHours <= endHours):
                if (start_PM is False): # Checks if the course is in the afternoon
                    self.startHours = startHours # Sets the hours for a course to start
                else :
                    self.startHours = startHours + 12 # If the course is in the afternoon, the program will add 12 hours
                
                if (end_PM is False): # Checks if the course is in the afternoon
                    self.endHours = endHours # Sets the hours for a course to end
                else :
                    self.endHours = endHours + 12 # If the course is in the afternoon, the program will add 12 hours
            else :
                return # <----- There should be a way for the GUI to ask the user for a different time input
        else :
            return # <----- There should be a way for the GUI to ask the user for a different time format
        #-------------------------------------------------------------------------------------------------------------
        # Get values from the user in minutes
        #-------------------------------------------------------------------------------------------------------------
        if (startMin < 60) and (endMin < 60):
            if (startHours == endHours) :
                if (startMin < endMin):
                    self.startMin = startMin
                    self.endMin = endMin
                else :
                    return # <----- There should be a way for the GUI to ask the user for a different minte span input
            elif (startMin < endMin):
                self.startMin = startMin
                self.endMin = endMin
            else :
                return # <----- There should be a way for the GUI to ask the user for a different minte span input
        else :
            return # <----- There should be a way for the GUI to ask the user for a different minte span input
        #-------------------------------------------------------------------------------------------------------------
        return
              
    def timeStart(self): # This method will convert the user input for the start time of the course into a string with format HH:MM
        convertStart = str(str(self.startHours) + ":" + str(self.startMin))
        startTime = datetime.datetime.strptime(convertStart, "%H:%M").time()
        return startTime # <---- Returns the starting time with format HH:MM
    
    def timeEnd(self): # This method will convert the user input for the ending time of the course into a string with format HH:MM
        convertEnd =  str(str(self.endHours) + ":" + str(self.endMin))
        endTime = datetime.datetime.strptime(convertEnd, "%H:%M").time()
        return endTime # <---- Returns the finishing time with format HH:MM
