# Written by:           John Mezzanotte
# Date Created:         4-20-15
# Date Last Modified:   4-21-15
# Last Modified by:     John Mezzanotte
# Usage:                from the command line pass the program:
#                           param 1: the full file path to the excel doc (xlsx or .xls)
#                           param 2: file path of output directory.  
#
#
# Description: This module contains one method called parse_to_json that will parse a .xls or .xlsx file 
#              to valid json. Json is the  There is a loop that indexes
#              the excel file and places each data row into an individual OrderedDictionary
#              object. Those OrderedDictionaries are then appended to a list. The list is passed
#              into the json encoder.
#
#
# modules used:
#               xlrd ---
#                   This is a non-standard module and will need be downloaded. You can run:
#
#                           pip install xlrd
# 
#                   to install the module.
#
#                   There are several helpful methods to help in parsing an
#                   excel file:
#
#                       wb = xlrd.open_workbook( file ) -- opens a workbookl
#                       sheet = wb.sheet_by_index( 0 ) -- opens a worksheet
#                       sheet.nrows -- shows the number of rows in the workbook
#                       sheet.ncols -- shows the number of columns
#
#                   you can index the rows and columns by ( row, col )
#
#               json ---
#                   Since python lists and dictionaries map very well to json, you can
#                   parse the excel file into dictionaries and lists and then use the
#                   json module to encode data to json
#
#                       json.dumps( var, indent = 4 ) -- will encode info passed into json
#
#               collections ---- OrderedDictionary
#                   Dictionaries do not maintain order. The OrderedDictionary class of the collections
#                   module allows you to do this.
#


import json
from collections import OrderedDict

#import non-standard  modules, requires download
try:
    import xlrd
except ImportError:
    msg = "install the module xlrd to run this script."
    raise ImportError( msg )


def parse_to_json( file_location ):

    """
        Params:              file path as string 
        return value:        string ( formatted as json )
        modules used:        collections, json, xlrd

        Great resource for testing the validity of json files : http://jsonlint.com/
    """

    #open the workbook
    workbook = xlrd.open_workbook( file_location )

    # first sheet is indexed by zero 
    sheet = workbook.sheet_by_index( 0 )

    # number of rows in the sheet
    total_rows = sheet.nrows

    # number of columns in the sheet
    total_columns = sheet.ncols

    # the loop will create an individual dictionary object, this list will hold each object. We will eventually pass this list to the
    # json encoder
    dict_list = []

    for i in range( 1, total_rows ):
        data_object = OrderedDict()
        for j in range( 0, total_columns ):
            # need to split indents at 'and' and hold them in a seperate list
            if j == 3 :
                data_object[ sheet.cell_value( 0, j ) ] = sheet.cell_value( i, j ).split( 'and' )
            # need to split subjects out into a separate list, since a single cell can hold multiple subjects. Subjects are separated by and in the spreadsheet
            #elif j == 4 :
            # data_object[ sheet.cell_value( 0, j).encode('ascii', 'replace' ) ] = sheet.cell_value( i, j ).encode( 'ascii', 'replace' ).split( 'and' )
            else:
                data_object[ sheet.cell_value( 0, j ) ] = \
                    str(sheet.cell_value( i, j )).strip()
        dict_list.append( data_object )
        

    # return the json string 
    return  json.dumps( dict_list, indent = 4 )


if __name__ == '__main__' :

    # Run the module as a program from the command line.
    # Takes two command line arguments a path to the source file and a path to the save location for the output file.
    from sys import argv

    try:
        script, path, outpath = argv
    except ValueError:
        err_msg = "Please input a file path to a .xls or xlsx file as well as a file path for the location of the output file." 
        raise ValueError( err_msg )

    print parse_to_json.__doc__
    
    # set you file location; escape the forward slashes.
    file_path = path
    output =  outpath + '\\powerup_add_test.json'

    # open a file object
    f = open( output, 'w+' )
    f.write( parse_to_json( file_path ) )
    f.close()
    print "\n\nOutput file has been saved here: %s" % output

    
   




    
