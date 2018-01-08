#!/usr/bin/env python3

from file_io import file_reader

Data = file_reader.FileReader("examples/wikipedia.csv")
AllData = Data.extractdata("examples/wikipedia.csv")


# --------------------------------------------------------------- #
# Define a function to convert the csv data to nodes structure    #
# --------------------------------------------------------------- #
# ---------------------- Start of Function ---------------------- #
def data_to_nodes(list_of_all_data):
    node_list = []
    for item in list_of_all_data:
        sublist = [item[0], item[1]]  # Append the node id and timestamp to the sublist
        identifier_list = []  # This list will contain all the identifiers
        identifiers = item[2].split(",")
        for identifier in identifiers:
            identifier_list.append(identifier)
        sublist.append(identifier_list)  # Append all the identifiers to sublist as a list
        node_list.append(sublist)
    return node_list
# ----------------------- End of Function ----------------------- #

# Creation of nodes by calling the function defined above
nodes = data_to_nodes(AllData)
for a in nodes:
    print(a)

# Creation of Links between nodes. links is the list containing the links
links = []
for ii, elem in enumerate(nodes[:-1]): # -1 is for keeping the elements to the second last sublist in nodes
    for jj in range(ii + 1, len(nodes)):
        common = set(elem[-1]).intersection(set(nodes[jj][-1])) # This -1 is for the identifiers, or to start looking at the list from backwards
        if len(common) > 0 and common != {''}:  # If you want to keep the empty identifiers then comment before the word "and"
            links.append([elem[0], nodes[jj][0], list(common)]) # Append ID of node1 , ID of node2, and the common Identifiers

print('#################################################################################################################################################')

for b in links:
    print(b)


print('#################################################################################################################################################')

# Creation of roots
roots = []
unique = set()   # This list is just for comparison of identifiers to avoid duplicates
for identity, _, identifiers in nodes:
    for identifier in identifiers:
        if identifier not in unique:
            roots.append([identity, identifier])
            unique.add(identifier)
### Other way of doing it
'''unique = []
for elements in nodes:
    for item in elements[2]:
        if item not in unique:
            roots.append([elements[0], item])
            unique.append(item)
print(roots)'''




print(roots)
print('#################################################################################################################################################')


