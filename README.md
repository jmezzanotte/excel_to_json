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

# Usage 
Here is an example of how I have used this module in the past to parse .xls or .xlsx files to json. This example accepts 
arguments from the command line. 
```
    from sys import argv

    try:
        script, path, outpath = argv
    except ValueError:
        err_msg = "Please input a file path to a .xls or xlsx file as well as a file path for the location of the output file." 
        raise ValueError( err_msg )

    print parse_to_json.__doc__
    
    # set you file location; escape the forward slashes.
    file_path = path
    output =  outpath + '\\test.json'

    # open a file object
    f = open( output, 'w+' )
    f.write( parse_to_json( file_path ) )
    f.close()
    print "\n\nOutput file has been saved here: %s" % output
  ```

#Background 
I Contributed to a web development team that needed a solution to parse a client's excel file into valid json. 
I developed and implemented a solution in Python to parse and convert this data to JSON. The script began very customized 
to the needs of the project, but I have began work to make it more of a general use module. 
