# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 17:58:52 2020

@author: nihal


"""


import csv
import copy 

n = int(input("Enter number of inputs : ")) 
inp_list = list(map(int,input("\nEnter the input times : ").strip().split()))[:n]
def closest(lst, K): 
    # lst.sort()
    lst = list(filter(lambda x: x < K, lst))  

            
    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K) )] 

with open("./files/01_battery_log_4m.csv","r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    prod_list1 = list(map(lambda lines: float(lines['Battery Voltage'])* float(lines['Battery Current']), csv_reader))
    s1 = sum(prod_list1)
    total_power = s1
    d = [s1 - (sum(prod_list1[0:i+1])) for i, x in enumerate(prod_list1)]

        
with open("./files/02_battery_log_2.csv","r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    prod_list2 = list(map(lambda lines: float(lines['Battery Voltage'])* float(lines['Battery Current']), csv_reader))
    s2 = sum(prod_list2)
    e = [total_power - (sum(prod_list2[0:i+1])) for i, x in enumerate(prod_list2)]        
    e = list(filter(lambda x: x > 0, e))  

index = 0
counter = 0
for i, x in enumerate(inp_list):
    new_index = index + inp_list[i]-1
    if i % 2 == 0:
        b = copy.deepcopy(e)
        if new_index >= len(d):
            break
        else:
            index = e.index(closest(b,d[new_index]))
            counter+=1
    else:
        c = copy.deepcopy(d) 
        if new_index >= len(e):
            break
        else:
            index = d.index(closest(c,e[new_index]))
            counter+=1
if counter == len(inp_list):
    print('battery is sufficient')
else:
    print('battery is not sufficient')

