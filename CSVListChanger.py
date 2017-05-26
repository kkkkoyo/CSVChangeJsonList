#coding:utf-8
from __future__ import print_function
from __future__ import unicode_literals
import argparse
import json
import csv
import io
import sys
import re
import uuid

parser = argparse.ArgumentParser()
parser.add_argument("csv_file_path")
parser.add_argument("json_file_path")
parser.add_argument("--encoding", default="utf_8")
options = parser.parse_args()

csv_reader = csv.reader(
     io.open(options.csv_file_path, "r", encoding=options.encoding),
)

print (options.csv_file_path.strip('.csv'))
mojiretu = ''
mojiretu +=  '"stage":[\n'
for i,row in enumerate(csv_reader):
    row.pop() #一つ余計だからpopする
    #sys.stdout.write("[")
    mojiretu += "["

    for j,data in enumerate(row):
        if (j==0):
            #sys.stdout.write('\"'+data+'\",')
            mojiretu += '\"'+data+'\",'

        elif (j==len(row)-1):
            #sys.stdout.write('\"'+data+'\"')
            mojiretu +='\"'+data+'\"'

        else:
            #sys.stdout.write('\"'+data+'\",')
            mojiretu +='\"'+data+'\",'

    if(i==sum(1 for line in open(options.csv_file_path))-1): #最後は点を取る
        #print("] ")
        mojiretu +="] \n"
    else:
        #print("], ")
        mojiretu +="], \n"

#print ('],')
mojiretu +='],\n'

print (mojiretu)

f = open(options.json_file_path, 'r')
test  = f
json = ''
for i,row in enumerate(f):
    json += row
    match = re.search(options.csv_file_path.strip('.csv'),str(row))
    if (match):
        json+=mojiretu
f = open(options.json_file_path, 'w')
f.write(json)
