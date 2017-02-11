import json
import os
from os.path import join, dirname
from os import listdir
from os.path import isfile,join
from watson_developer_cloud import PersonalityInsightsV2

personality_insights = PersonalityInsightsV2(username = "38adf6a6-6378-4717-abb4-7941215994b7", password = "ZPpbmgkqOW6z")

inputpath =  r'C:\Users\acer\Downloads\inpuf files'
filenames = [f for f in listdir(inputpath) if isfile(join(inputpath,f))]
print 'filenames', filenames
os.chdir(inputpath)

print 'number of input files:' , len(filenames)
count = 0

for file in filenames: 
	count += 1
	
	with open(file) as personality_text:
		outputfile = open(file+'jsonoutput.txt','wb')
		jsonoutput = json.dumps(personality_insights.profile(text=personality_text.read(), accept = 'application/json'))
		jsonparsed = json.loads(jsonoutput)
		print >>outputfile, json.dumps(jsonparsed,indent =10, sort_keys=True, separators = (',',':'))
		#print >>outputfile, jsonoutput
	