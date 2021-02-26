from sys import argv
from os import listdir
import os

files = argv[1]
files = listdir(files)

exportFolder = argv[2]

for file in files:
    fileName = (file.rsplit('.', 1)[0])
    os.system("echo megaa comand")



