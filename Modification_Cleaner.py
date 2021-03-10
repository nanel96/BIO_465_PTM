import csv
import re

def clean(in_file, out_file):
    f = open(in_file, 'r') #input file
    o = open(out_file,'w') #output file
    header = f.readline() #pop header
    o.write(header) #write header to output file
    for line in f:
        line = line.split("\t") #split tsv file by tabs
        item = line[3] #take the observed modifications item
        item = item.split(",") #spit the observed modifications by comma
        new_item = [] #create a list that will contain desired modifications
        for thing in item:
            if "->" not in thing:
                pattern = r'\(\d+\.\d+\)'
                thing = re.sub(pattern, '', thing)
                new_item.append(thing)
        line[3] = ", ".join(new_item) #edit the line so that it contains the filtered modifications
        line = "\t".join(line)
        o.write(line) #write the edited line to the new file
    o.close()
    f.close()

