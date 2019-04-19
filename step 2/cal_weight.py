#filename1=input("Enter File Name containing edges:>").strip('\n')
#filename2=input("Enter File Name containing degree of each node:>").strip('\n')

filename1 = "1.txt"
filename2 = "degree_of_each_node.txt"

fp1 = open(filename1, "r")
fp2 = open(filename2, "r")
fp3 = open("weight_of_each_edge.txt", "w")

print("usage: a b weight(a->b) weight(b->a)")
line1 = fp1.readline()
line2 = fp2.readlines()

while line1:
	a = line1.split(" ")
	x = int(a[0])
	y = int(a[1])
	b = line2[y].split(" ")
	c = line2[x].split(" ")
	fp3.write(str(x) + " " + str(y) + " " + str(float(b[2])) + " " + str(float(c[2])) + "\n")
	line1 = fp1.readline()

