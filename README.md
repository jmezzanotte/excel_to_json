# excel_to_json

#Purpose and Overview
This module contains one method called parse_to_json that will parse an .xls or .xlsx to valid json. Json is the 
There is a loop that indexes the excel file and places each data row into an individual OrderedDictionary object. 
Those OrderedDictionaries are then appended to a list. The list is passed into the json encoder.

#Author 
John Mezzanotte

#Date Created
4-21-2015 

# External Modules Required
This module requires xlrd.py 


#Background 
I Contributed to a web development team that needed a solution to parse a client's excel file into valid json. 
I developed and implemented a solution in Python to parse and convert this data to JSON. The script began very customized 
to the needs of the project, but I have began work to make it more of a general use module. 
