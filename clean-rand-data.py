import os
import csv

counter = 0
if os.path.isfile('data/rand-terrorism-dataset.txt'):
	print("Previous dataset is removed")
	os.remove('data/rand-terrorism-dataset.txt')

with open('data/RAND_Database_of_Worldwide_Terrorism_Incidents.csv','rt',encoding='latin-1') as f:
	output_txt = open('data/rand-terrorism-dataset.txt','w',encoding='utf-8')
	reader = csv.reader(f)
	for line in reader:
			output_txt.write(line[7]+'\n')

print("All done")