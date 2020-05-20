"""
File: dictionary.py
A simple program for
creating dictionary from a given
txt file
"""

def create_dictionary(filename):
    """
    Creates a dictionary
    from a given txt file with
    a given format as follows:
    
    keyword = meaning 
    """
    id_dict = {}

    with open(filename) as f:
        lines = f.read().split('\n')
        for line in lines:
            temp = line.split(' = ')
            if temp[0] in id_dict.keys():
                if not isinstance(id_dict[temp[0]], list):
                    first_entry = id_dict[temp[0]]
                    id_dict[temp[0]] = []
                    id_dict[temp[0]].append(first_entry)
                id_dict[temp[0]].append(temp[1])
            else:
                id_dict[temp[0]] = temp[1]
    
    return id_dict