#coding:utf-8
from __future__ import print_function
from __future__ import unicode_literals
import argparse
import csv
import io
import sys

parser = argparse.ArgumentParser()
parser.add_argument("csv_file_path")
parser.add_argument("--encoding", default="utf_8")
options = parser.parse_args()

csv_reader = csv.reader(
     io.open(options.csv_file_path, "r", encoding=options.encoding),
)

for i,row in enumerate(csv_reader):
    row.pop() #一つ余計だからpopする
    sys.stdout.write("[")
    for j,data in enumerate(row):
        if (j==0):
            sys.stdout.write('\"'+data+'\",')
        elif (j==len(row)-1):
            sys.stdout.write('\"'+data+'\"')
        else:
            sys.stdout.write('\"'+data+'\",')
    if(i==sum(1 for line in open(options.csv_file_path))-1): #最後は点を取る
        print("] ")
    else:
        print("], ")
