import csv
import re


amino_acids = ['Ala', 'Arg', 'Asn', 'Asp', 'Asn', 'Cys', 'Glu', 'Gln', 'Gly', 'His', 'Ile', 'Leu', 'Lys', 'Met', 'Phe', 'Pro', 'Ser', 'Thr', 'Trp', 'Tyr', 'Val']
exceptions = ['DiLeu4plex(145.132163)', 'FormylMet(159.035399)', 'DiLeu4plex118(145.140471)', 'DiLeu4plex117(145.128307)', 'DiLeu4plex115(145.120000)', 'UgiJoullieProGly(154.074228)']
def clean(in_file, out_file, Print = False):
    f = open(in_file, 'r') #input file
    o = open(out_file,'w') #output file
    header = f.readline() #pop header
    o.write(header) #write header to output file
    dropped_mods = set()
    for line in f:
        line = line.split("\t") #split tsv file by tabs
        item = line[3] #take the observed modifications item
        modifications = item.split(",") #spit the observed modifications by comma
        new_modifications = [] #create a list that will contain desired modifications
        
        for modification in modifications:
            modification = modification.strip()
            substitution = False
            for amino_acid in amino_acids:
                pattern = r'' + amino_acid + '[^A-z]'
                if re.search(pattern, modification) and modification not in exceptions:
                    if Print and '->' not in modification:
                        dropped_mods.add(modification)
                    substitution = True
                    break
            if not substitution:
                new_modifications.append(modification)               
        line[3] = ", ".join(new_modifications) #edit the line so that it contains the filtered modifications
        line = "\t".join(line)
        o.write(line) #write the edited line to the new file
    if Print:
        print(dropped_mods)
    o.close()
    f.close()


