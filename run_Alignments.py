from sys import argv
from os import listdir
import os

files = argv[1]
files = listdir(files)

for file in files:
    """filepath = "Gene_FASTA_Files/" + file
    f = open(filepath, "r")
    lineCount = 0
    for line in f:
        lineCount += 1
    if lineCount < 1:
        pass"""
    fileName = (file.rsplit('.', 1)[0])
    command = ""
    command += "megacc -a muscle_align_protein.mao -d /Gene_FASTA_Files/"
    command += file
    command += " -o Alignments/"
    command += fileName
    os.system(command)






