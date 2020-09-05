print("Hello world")
import numpy as np
import pandas as pd
import csv

mylist = []
with open(file='data/entities.csv', mode='r') as f:
    myfile = csv.reader(f,delimiter=',')
    for row in myfile:
        for col in row:
            mylist.append(col)
name =
mylist[mylist.index('IT')+1]


# ds = pd.read_csv("data/entities.csv")
# ds['entity']
