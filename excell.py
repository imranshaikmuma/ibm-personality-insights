import xlsxwriter
import csv
import json
import os
from os import listdir
from os.path import isfile,join

workbook = xlsxwriter.Workbook('finaloutputnew.xlsx')
worksheet = workbook.add_worksheet()

merge_format = workbook.add_format({
    'bold': 1,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter'})

worksheet.merge_range('A1:A3', 'DOCUMENT ID',merge_format)
worksheet.merge_range('B1:BS1', 'BIG5',merge_format)
worksheet.merge_range('BT1:CQ1', 'NEEDS',merge_format)
worksheet.merge_range('CR1:DA1', 'VALUES',merge_format)

worksheet.merge_range('B2:C2', 'Openness',merge_format)
worksheet.merge_range('D2:E2', 'Adventurousness',merge_format)
worksheet.merge_range('F2:G2', 'Artistic interests',merge_format)
worksheet.merge_range('H2:I2', 'Emotionality',merge_format)
worksheet.merge_range('J2:K2', 'Imagination',merge_format)
worksheet.merge_range('L2:M2', 'Intellect',merge_format)
worksheet.merge_range('N2:O2', 'Authority-challenging',merge_format)
worksheet.merge_range('P2:Q2', 'Conscientiousness',merge_format)
worksheet.merge_range('R2:S2', 'Achievement striving',merge_format)
worksheet.merge_range('T2:U2', 'Cautiousness',merge_format)
worksheet.merge_range('V2:W2', 'Dutifulness',merge_format)
worksheet.merge_range('X2:Y2', 'Orderliness',merge_format)
worksheet.merge_range('Z2:AA2', 'Self-discipline',merge_format)
worksheet.merge_range('AB2:AC2', 'Self-efficacy',merge_format)
worksheet.merge_range('AD2:AE2', 'Extraversion',merge_format)
worksheet.merge_range('AF2:AG2', 'Activity level',merge_format)
worksheet.merge_range('AH2:AI2', 'Assertiveness',merge_format)
worksheet.merge_range('AJ2:AK2', 'Cheerfulness',merge_format)
worksheet.merge_range('AL2:AM2', 'Excitement-seeking',merge_format)
worksheet.merge_range('AN2:AO2', 'Outgoing',merge_format)
worksheet.merge_range('AP2:AQ2', 'Gregariousness',merge_format)
worksheet.merge_range('AR2:AS2', 'Agreeableness',merge_format)
worksheet.merge_range('AT2:AU2', 'Altruism',merge_format)
worksheet.merge_range('AV2:AW2', 'Cooperation',merge_format)
worksheet.merge_range('AX2:AY2', 'Modesty',merge_format)
worksheet.merge_range('AZ2:BA2', 'Uncompromising',merge_format)
worksheet.merge_range('BB2:BC2', 'Sympathy',merge_format)
worksheet.merge_range('BD2:BE2', 'Trust',merge_format)
worksheet.merge_range('BF2:BG2', 'Emotional range',merge_format)
worksheet.merge_range('BH2:BI2', 'Fiery',merge_format)
worksheet.merge_range('BJ2:BK2', 'Prone to worry',merge_format)
worksheet.merge_range('BL2:BM2', 'Melancholy',merge_format)
worksheet.merge_range('BN2:BO2', 'Immoderation',merge_format)
worksheet.merge_range('BP2:BQ2', 'Self-consciousness',merge_format)
worksheet.merge_range('BR2:BS2', 'Susceptible to stress',merge_format)

worksheet.merge_range('BT2:BU2', 'Challenge',merge_format)
worksheet.merge_range('BV2:BW2', 'Closeness',merge_format)
worksheet.merge_range('BX2:BY2', 'Curiosity',merge_format)
worksheet.merge_range('BZ2:CA2', 'Excitement',merge_format)
worksheet.merge_range('CB2:CC2', 'Harmony',merge_format)
worksheet.merge_range('CD2:CE2', 'Ideal',merge_format)
worksheet.merge_range('CF2:CG2', 'Liberty',merge_format)
worksheet.merge_range('CH2:CI2', 'Love',merge_format)
worksheet.merge_range('CJ2:CK2', 'Practicality',merge_format)
worksheet.merge_range('CL2:CM2', 'Self-expression',merge_format)
worksheet.merge_range('CN2:CO2', 'Stability',merge_format)
worksheet.merge_range('CP2:CQ2', 'Structure',merge_format)


worksheet.merge_range('CR2:CS2', 'Conservation',merge_format)
worksheet.merge_range('CT2:CU2', 'Openness to change',merge_format)
worksheet.merge_range('CV2:CW2', 'Hedonism',merge_format)
worksheet.merge_range('CX2:CY2', 'Self-enhancement',merge_format)
worksheet.merge_range('CZ2:DA2', 'Self-transcendence',merge_format)

for i in range(1,105,2):
	worksheet.write(2,i,'percentage',merge_format)
	worksheet.write(2,i+1,'error',merge_format)



inputpath =  r'C:\Users\acer\Downloads\watsonpersonalityinsights\imrannew1'
filenames = [f for f in listdir(inputpath) if isfile(join(inputpath,f))]
print 'filenames', filenames
os.chdir(inputpath)

filecount = 0
wrow = 2



for file in filenames:
	sfile = file.split(".")	

	filecount += 1
	wcol = 1
	rowcount = 0
	colcount = 0
	f = open(file,'r')
	wrow += 1
	reader = csv.reader(f)
	
	print reader
	for row in reader:
		rowcount += 1
		colcount =0
		if rowcount > 1:
			
			worksheet.write(wrow,0,sfile[0],merge_format)
			for col in row:
				colcount +=1
				if colcount == 2:
					percentage = round((float(col)*100),3)					 
					worksheet.write(wrow,wcol,percentage,merge_format)
					wcol = wcol + 1
					
				if colcount ==4:
					errorvalue = round((float(col)*100),3)
					worksheet.write(wrow,wcol,errorvalue,merge_format)
					wcol = wcol + 1
						 
						
	     
#f.close()
#workbook.close()






























workbook.close()