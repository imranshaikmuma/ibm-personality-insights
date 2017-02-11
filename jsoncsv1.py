import json

import csv
import os
from os import listdir
from os.path import isfile,join


inputpath =  r'C:\Users\acer\Downloads\watsonpersonalityinsights\imrannew'
filenames = [f for f in listdir(inputpath) if isfile(join(inputpath,f))]
print 'filenames', filenames
os.chdir(inputpath)

print 'number of input files:' , len(filenames)
count = 0

for file in filenames: 
	count += 1
	
	f = open(file,'r')
	
	jsonparsed = json.load(f)
		
	output = open(file+'json.csv','wb')
	print 'outputfilename' , output
	csvwriter = csv.writer(output)
	
	personality = jsonparsed['tree']['children'][0]	
	needs = jsonparsed['tree']['children'][1]
	values = jsonparsed['tree']['children'][2]
	
	openness_parent = personality['children'][0]
	openness = openness_parent['children'][0]
	
	header = ['category','percentage','id','sampling_error','name']
	csvwriter.writerow(header)
	

	for i in range(0,5):
		column = openness_parent['children'][i]
		big5 = dict()
		big5['category']= openness_parent['children'][i]['category']
		big5['sampling_error']= openness_parent['children'][i]['sampling_error']
		big5['id']= openness_parent['children'][i]['id']
		big5['percentage']= openness_parent['children'][i]['percentage']
		big5['name']= openness_parent['children'][i]['name']
		csvwriter.writerow(big5.values())
		column_types = column['children']
		for type in column_types:
			csvwriter.writerow(type.values())

	harmony_parent = needs['children'][0]
	needs_columns = harmony_parent['children']
	for type in needs_columns:
		csvwriter.writerow(type.values())

	conservation_parent = values['children'][0]
	values_columns = conservation_parent['children']

	for type in values_columns:
		csvwriter.writerow(type.values())
output.close()












