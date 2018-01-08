import csv


class FileFormatException(Exception):
    pass


class FileReader(object):
    """ This class will read the csv file, and store the data in the form:
    columns id|timestamp|[identifier1,identifier2,...]:
    """

    def __init__(self, file):
        self.file = file

    #----------------------------------------------------------------------#
    # Define a function to read the input file and extract the data in it  #
    #----------------------------------------------------------------------#
    #------------------------ Start of Function ------------------------#
    def extractdata(self, file):
        List_of_Data = [] # A list to save all the csv data in it
        f = open(file, 'r')
        file_read = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE)
        for row in file_read:
            List_of_Data.append(row)
        return List_of_Data
    # ------------------------- End of Function ------------------------#