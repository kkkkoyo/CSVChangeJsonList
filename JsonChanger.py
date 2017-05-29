import argparse
import subprocess
import re

parser = argparse.ArgumentParser()
parser.add_argument("csv_file_path")
parser.add_argument("json_file_path")
parser.add_argument("--encoding", default="utf_8")
options = parser.parse_args()

pattern=r'([+-]?[0-9]+\.?[0-9]*)'

name = options.csv_file_path.strip('.csv')
file_name = re.sub(pattern, "", name)

list01 = []
f = open(options.json_file_path, 'r')

isStart = False

for i,row in enumerate(f):
    match = re.search(file_name,str(row))
    writted = re.search(name,str(row))
    if(writted):
        isStart = True
    if(match and isStart):
        list01.append(row[match.start():match.end()+4])

args = ['python','CSVListChanger.py',options.csv_file_path,options.json_file_path]

try:
    for num in list01:
        print("added:"+num)
        args[2] = num+'.csv'
        res = subprocess.check_call(args)
except:
    print "Error."
