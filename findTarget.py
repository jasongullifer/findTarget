#!/usr/bin/python
'''findTargey.py - Jason W. Gullifer - 2013

This program will loop through many trials in a csv input file
(readFileName) to find the position in a sentence, starting at 0, of a
given target word. The new data set will be output as a csv file
(writeFileName).

Sentence should be supplied under a column (sentenceColumn), and each
target word is supplied by column entitled (targetWordColumn"). The
position will be output as column (targetROIColumn).

ReadFile and WriteFile are supplied for easy reading and writing of
csv files.
'''
import csv
import nltk
import re
import codecs


readFileName = 'merged_cleaned.csv'
writeFileName = 'data_marked.csv'

targetROIColumn = 'TargetNumber'
targetWordColumn = 'exactTarget'
sentenceColumn = 'Sentence'

codingScheme = 'utf8'


def ReadFile(filename):
    '''Function to read a csv file into a list of dictionaries.  The
    data and header information are returned separately. Make sure if
    you add columns or dictionary keys to the file, also update the
    header for when you write the file.'''
    lines = list()
    openFile = open(filename, 'r')
    myReader = csv.DictReader(openFile) 
    for line in myReader:
        lines.append(line)
        
    openFile.close()
    openFile = open(filename, 'r')
    header = openFile.readline().strip("\n").split(",")
    openFile.close()
    return lines, header

def WriteFile(stuff,filename,ordering=0):
    '''Function to write a list of dictionaries to a csv file. You may
    optionally supply header information to maintain the ordering from
    your original read file.'''
    if ordering == 0:
        ordering = stuff[0].keys()
        
    outFile = open(filename, 'w')
    myWriter=csv.DictWriter(outFile, ordering)
    outFile.write(','.join(ordering) + '\n') 
    myWriter.writerows(stuff)
    outFile.close()

def FindTarget(target, sentence):
    ''' This function will search a sentence for a target word and
return the position of that word starting at 0. If the target isn't
found, 0 is output.'''
    try:
        position = re.split('\s*', sentence).index(target)
    except:
        return 0
    return position

if __name__ == "__main__":
    sents,header = ReadFile(readFileName)
    for line in sents:
        line[targetROIColumn] = FindTarget(line[targetWordColumn], line[sentenceColumn])
        
    header.append(targetROIColumn)
    WriteFile(sents, writeFileName, header)
