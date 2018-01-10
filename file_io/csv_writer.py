import csv


class FileFormatException(Exception):
    pass


class FileWriter(object):
    """ This class will write the csv files, by reading the data from list of tuples of the form:
    columns id|timestamp|[identifier1,identifier2,...]:
    """

    def __init__(self, file):
        self.file = file

    #----------------------------------------------------------------------#
    # Define a function to write the output csv file                       #
    #----------------------------------------------------------------------#
    #------------------------ Start of Function ------------------------#
    def writeCSV(self, list_to_write, OutputFileName):
        file = open(OutputFileName, 'w', newline='')
        writer = csv.writer(file, quotechar='"', delimiter=';',quoting=csv.QUOTE_ALL, skipinitialspace=True)
        for row in list_to_write:
            writer.writerow(row)
    # ------------------------- End of Function ------------------------#