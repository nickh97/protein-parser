"""Parse a file containing protein sequences and format them in a table."""
import re
#import numpy as np
import pandas as pd
import os


def ReadSequences(filename):
    #Condense protein sequences into an array from a fasta file.
    try:
        if re.search(".*\.fasta", filename) == None:
            raise ValueError
    except ValueError:
        print("Please supply a .fasta file")
    proteins = []
    try:
        with open(filename) as file:
            newProtein = ""
            for line in file:
                if (line[0] == '>'):
                    if newProtein != "":
                        proteins.append(newProtein)
                    proteins.append(line.strip())
                else:
                    newProtein += line.strip()
            proteins.append(newProtein)
    
        file.close()
        return proteins
    except FileNotFoundError:
        print("The selected file was not found. Double-check your file path and try again.")

def FormatSequences(proteinArray):
    #Formats all proteins in an array into a dictionary
        
    proteinDict = {}        #Add protein sequences/loci to a dictionary
    proteinName = ""
    for protein in proteinArray:
        if protein[0] == '>':
            proteinName = protein[1:10].rstrip('_')
        else:
            proteinDict[proteinName] = protein
    
    return proteinDict

def ParseSequences(proteinDict, loci, area=5):
    #Takes a dictionary of protein names and sequences and formats them to a pandas DataFrame,
    #displaying a table with the selected sequence regions highlighted

        
    proteinDict = SequenceHighlighter(proteinDict, loci, area)    #change out whole sequence for a list of highlighted slices
        
    table = pd.DataFrame.from_dict(proteinDict, orient='index', columns=loci)
    
    return table

def SequenceHighlighter(proteinDict, loci, area):
    #Accepts a dict of protein names & sequences and a list of loci to highlight
    #Returns a modified dictionary with the sequences reduced to only the areas of interest
    #Also takes an optional parameter of how many amino acids to include on either side of the
    #selected locus
    
    #Take slices of each sequence equal to +/- area (default 5) amino acids on either side of 
    #a given locus; append the slices to a list and replace the current dict value with this list
    for name, sequence in proteinDict.items():
        highlightedSequence = []
        for locus in loci:
            locus += 1  #correct for off-by-one errors
            highlightedSequence.append(sequence[(locus - area) : (locus + area) + 1])
            
        proteinDict[name] = highlightedSequence
    
    return proteinDict

def PrintSequences(table, filename='output.txt'):
    #Accepts a pandas table and prints it to an output file for viewing
    
    with open(filename, 'w') as outfile:
    #    output = table.to_string(justify='center')
        output = table.to_string(justify="center")
        outfile.write(output)
    outfile.close()
    
    
#START MAIN SCRIPT:

fileInputMessage = "Please enter the path to the .fasta file you want to process, or just type the name of the file if it's in the same folder as this script:\n"
lociInputMessage = "\nPlease enter the base pairs you want to focus on and compare to one another. Type 'stop' when done:"
areaInputMessage = "\n(Optional) Enter the number of base pairs to display on either side of the target bases. Can be any number from 0 - 10. Defaults to 5 if left blank:"
outfileInputMessage = "\n(Optional) Enter the name of the file to output to. PLEASE NOTE: if you plan on running multiple times, make sure each output file has a unique name or they will overwright each other:"

file = input(fileInputMessage)          #Get the name of the input file from the user

loci = []

print(lociInputMessage)                 #Get the loci to compare from the user and store them in a list of ints
while True:
    x = input()
    if x == 'stop':
        break
    try:
        element = int(x)
        loci.append(element)
    except ValueError:
        print("Please enter a valid integer\n")

print(areaInputMessage)                 #Get the display range from the user and check that it's a valid integer
area = 5                                #Default to 5 if nothing is entered
y = input()
if y != '':
    try:
        area = int(y)
    except ValueError:
        print("Please enter a valid integer\n")

print(outfileInputMessage)              #Get the name of the file to write to from the user
outfile = "outfile.txt"
z = input()
if z != '':
    outfile.replace("\\s", "_")
    outfile = z

proteinArray = ReadSequences(file)
proteinDict = FormatSequences(proteinArray)
proteinTable = ParseSequences(proteinDict, loci, area)
PrintSequences(proteinTable, outfile)
