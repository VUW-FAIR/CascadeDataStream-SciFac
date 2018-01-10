#!/usr/bin/env python3

from file_io import file_reader
from file_io import csv_writer
import sys

# Input and output file names
InFile = "examples/wikipedia.csv"
# InFile = sys.argv[1]
InFileName = InFile.split('\\').pop().split('/').pop().rsplit('.', 1)[0]

Data = file_reader.FileReader(InFile)
AllData = Data.extractdata(InFile)
#################################################################################################################################################
###   Definition of useful functions to be used later
#################################################################################################################################################

# --------------------------------------------------------------- #
# Define a function to convert the csv data to nodes structure    #
# --------------------------------------------------------------- #
# ---------------------- Start of Function ---------------------- #
def data_to_nodes(list_of_all_data):
    node_list = []
    for item in list_of_all_data:
        if item[2] != "":
            sublist = [item[0], item[1]] # Append the node id and timestamp to sublist if the identifiers is not empty
            identifier_list = []  # This list will contain all the identifiers
            identifiers = item[2].split(",")
            for identifier in identifiers:
                identifier_list.append(identifier)
            sublist.append(identifier_list)  # Append all the identifiers to sublist as a list
            node_list.append(sublist)
    return node_list
# ----------------------- End of Function ----------------------- #

# ------------------------------------------------------------------ #
# Define a function to convert the nodes list to csv desired format  #
# ------------------------------------------------------------------ #
# ---------------------- Start of Function ---------------------- #
def nodes_to_formatted_nodes(list_of_nodes):
    formatted_nodes = []
    for item in list_of_nodes:
        sublist = []
        sublist.append(str(item[0]))
        sublist.append(item[1])
        sublist.append(','.join(map(str, item[2])))
        formatted_nodes.append(sublist)
    return formatted_nodes
# ----------------------- End of Function ----------------------- #
#################################################################################################################################################
###############################################################################
#                                                                             #
#                    The Main Part of the Program Starts Here                 #
#                                                                             #
###############################################################################
# =========================================================================== #
#          Creation of nodes by calling the function defined above            #
# =========================================================================== #
nodes = data_to_nodes(AllData)

# Formatting the nodes to make suitable for writing to desired csv file
nodes_formatted = nodes_to_formatted_nodes(nodes)

# Write nodes to a csv file
csv_writer.FileWriter.writeCSV(csv_writer,nodes_formatted,'output_files/'+InFileName+'-nodes.csv')
#for a in nodes_formatted:
#    print(a)

#print('#################################################################################################################################################')
# =========================================================================== #
#   Creation of Links between nodes. links is the list containing the links   #
# =========================================================================== #
links = []
for ii, elem in enumerate(nodes[:-1]): # -1 is for keeping the elements to the second last sublist in nodes
    for jj in range(ii + 1, len(nodes)):
        common = set(elem[-1]).intersection(set(nodes[jj][-1])) # This -1 is for the identifiers, or to start looking at the list from backwards
        if len(common) > 0 and common != {''}:  # If you want to keep the empty identifiers then comment before the word "and"
            links.append([elem[0], nodes[jj][0], ','.join(map(str, list(common)))]) # Append ID of node1 , ID of node2, and the common Identifiers\
                                                                                    # Common indetifiers are changed to list first and then to string

# Write links to a csv file
csv_writer.FileWriter.writeCSV(csv_writer,links,'output_files/'+InFileName+'-links.csv')

#for b in links:
#    print(b)

print('#################################################################################################################################################')

# =========================================================================== #
#                               Creation of roots                             #
# =========================================================================== #
roots = []
unique = []
for elements in nodes:
    for item in elements[2]:
        if item not in unique:
            roots.append([elements[0], item])
            unique.append(item)

### Other way of doing it. Sets are more memory intensive that is why for bigger data I am not sure to use them. But one fact that they are fast for big data
'''unique = set()   # This list is just for comparison of identifiers to avoid duplicates
for identity, _, identifiers in nodes:
    for identifier in identifiers:
        if identifier not in unique:
            roots.append([identity, identifier])
            unique.add(identifier)
print(roots)'''

# Write roots to a csv file
csv_writer.FileWriter.writeCSV(csv_writer,roots,'output_files/'+InFileName+'-roots.csv')
print(roots)
print('#################################################################################################################################################')


