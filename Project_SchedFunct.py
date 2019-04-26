import pandas as pd
import numpy as np

class Schedule: # Working on it
    def __init__(self, startTime, endTime, weekDays, roomID, courseID, year):
        tempSched = pd.read_excel('Summer.xlsx')
        self.newSched(roomID, courseID, startTime, endTime, weekDays)
        return
            
    def newSched(self, roomID, courseID, startTime, endTime, weekDays):
        tempSched = pd.DataFrame({'Room': [roomID], 'Meeting Days' : [weekDays], 'Time Start' : [startTime], 'Time End' : [endTime], 'Course' : [courseID]})
        tempSched.set_index('Room', inplace=True)
        excelEditor = pd.ExcelWriter('Summer.xlsx', engine='xlsxwriter')
        tempSched.to_excel(excelEditor, sheet_name='Sheet 1')
        excelEditor.save()
           
        
