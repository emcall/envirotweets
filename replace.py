f1 = open("table.txt", "r");
f2 = open("table.csv", "w");
for line in f1:
	editline = line.replace("\t", ";", 39)
	f2.write(editline.replace("\t", ""))

f1.close()
f2.close()