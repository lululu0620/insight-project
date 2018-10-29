#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 15:36:52 2018

@author: luxie
"""


import os
import heapq
import argparse

class Object:
    """
    Save Occupation and State object in this new class
    Sort these objects by its count in a increasing order
    If there is a tie, sort them by its name in a decreasing order
    """
    def __init__(self, name, count):
        self.name = name.replace("\"", "")
        self.count = count
        
    def __cmp__(self, other):
        if self.count == other.count:
            return cmp(other.name, self.name)
        return self.count - other.count
        
    def output(self, total):
        percent = round(self.count * 100.0 / total, 1)
        return self.name + ";" + str(self.count) + ";" + str(percent) + "%\n"

def addparse():
    """
    Use the package argparse to add some arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", "-d", nargs='?')
    parser.add_argument("--occupation", "-o", nargs='?')
    parser.add_argument("--state", "-s", nargs='?')
    try:
        args = parser.parse_args()
    except IOError as msg:
        parser.error(str(msg))
    return args
    
def openfile(filename, method):
    """
    Find the corrent directname and open the file
    """
    dirname = os.path.dirname(os.path.abspath("__file__"))
    f = open(dirname + filename, method)
    return f

def getColIndex(col):
    """
    Since data files in different year have different layout, we have to find 
    the correct column index that we need
    I collect all possible column names of status, state, and occupation
    If the new data file has new layout, we should add new column names here
    """
    status_col_name = set(["CASE_STATUS", "STATUS", "APPROVAL_STATUS"])
    state_col_name = set(["WORKSITE_STATE", "LCA_CASE_WORKLOC1_STATE", "STATE_1"])
    occupation_col_name = set(["SOC_NAME", "LCA_CASE_SOC_NAME", "OCCUPATION_TITLE"])
    col_map = [-1, -1, -1]
    for i in range(len(col)):
        if col[i] in status_col_name:
            col_map[0] = i
        if col[i] in state_col_name:
            col_map[1] = i
        if col[i] in occupation_col_name:
            col_map[2] = i
    return col_map

def removeNoise(line):
    """
    Replace semicolons which is not a separate sign with another sign
    """
    return line.replace("&AMP;", "&")

def process(f, occupation, state):
    """
    File resource: https://www.foreignlaborcert.doleta.gov/performancedata.cfm
    We have converted the Excel files into a semicolon separated ";" format
    Process the data file line by line
    Count the case and group by occupation and state
    Save two group and their respective count in two dictionaries
    Return total number of certified h1b cases
    """
    total_count = 0
    start = True
    sep = ";"
    line_index = 0
    for line in f:
        h1b = removeNoise(line).split(sep)
        if start:
            col = getColIndex(h1b)
            start = False
        else:
            status = h1b[col[0]]
            state_name = h1b[col[1]]
            name = h1b[col[2]]
            if status == "CERTIFIED":
                if name in occupation:
                    occupation[name] += 1
                else:
                    occupation[name] = 1
                if state_name in state:
                    state[state_name] += 1
                else:
                    state[state_name] = 1
                total_count += 1
        line_index += 1
    return total_count

def sortResult(dic):
    """
    Convert the dictionary to a heap with respective objects
    Since we have defined cmp funcion in class Object, we just loop the dictionary,
    create a object with its name and count, and put it in the heap
    The top element of heap has largest count
    Because we only want to get top 10 objects, when the size of heap is more
    than 10, we just pop one element
    In this case, We can get top 10 objects in the heap finally
    We put them in a list and return this list
    """
    heap = []
    for name in dic:
        heapq.heappush(heap, Object(name, dic[name]))
        if len(heap) > 10:
            heapq.heappop(heap)
    results = [0] * len(heap)
    for i in range(len(heap)):
        results[i] = heapq.heappop(heap)
    return results

def writefile(dic, outfile, total, class_name):
    """
    Get the top 10 objects and write them in the file
    """
    res = sortResult(dic)
    if class_name == "o":
        outfile.write("TOP_OCCUPATIONS;")
    else:
        outfile.write("TOP_STATES;")
    outfile.write("NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
    for i in range(len(res)-1, -1, -1):
        outfile.write(res[i].output(total))

def main():
    """
    Read the csv file and process the data
    Output top 10 occupations and top 10 states for certified visa applications
    """
    # add parser
    args = addparse()
    
    # get arguments
    infile = openfile(args.data, "r")
    outfile_occupations = openfile(args.occupation, "w")
    outfile_states = openfile(args.state, "w")
    
    # process data
    occupation = {}
    state = {}
    total = process(infile, occupation, state)
    
    # write output file
    writefile(occupation, outfile_occupations, total, "o")
    writefile(state, outfile_states, total, "s")
    
if __name__ == '__main__':
    main()
