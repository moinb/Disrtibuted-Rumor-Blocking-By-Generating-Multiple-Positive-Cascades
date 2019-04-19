import matplotlib.pyplot as plt

if __name__ == "__main__":
	x1=[]
	y1=[]
	x2=[]
	y2=[]
	x3=[]
	y3=[]
	x4=[]
	y4=[]
	x5=[]
	y5=[]
	graph_title=input("Enter graph title:>").strip("\n")
	x_label=input("Enter X-axis label:>").strip("\n")
	y_label=input("Enter Y-axis label:>").strip("\n")
	filename1=input("Enter file name (NoBlocking Method Result):>").strip("\n")
	filename2=input("Enter file name (Game Method Result):>").strip("\n")
	filename3=input("Enter file name (Greedy Method Result):>").strip("\n")
	filename4=input("Enter file name (MaxDegree Method Result):>").strip("\n")
	filename5=input("Enter file name (Random Method Result):>").strip("\n")
	fp1=open(filename1)
	fp2=open(filename2)
	fp3=open(filename3)
	fp4=open(filename4)
	fp5=open(filename5)
	lines1=fp1.readlines() 
	lines2=fp2.readlines() 
	lines3=fp3.readlines() 
	lines4=fp4.readlines() 
	lines5=fp5.readlines() 
	fp1.close()
	fp2.close()
	fp3.close()
	fp4.close()
	fp5.close()
	
	for i in range(0, len(lines1)):
		tmp = lines1[i].split(" ")
		x1.append(float(tmp[0]))
		y1.append(float(tmp[1]))
		
	for i in range(0, len(lines2)):
		tmp = lines2[i].split(" ")
		x2.append(float(tmp[0]))
		y2.append(float(tmp[1]))
	for i in range(0, len(lines3)):
		tmp = lines3[i].split(" ")
		x3.append(float(tmp[0]))
		y3.append(float(tmp[1]))
		
	for i in range(0, len(lines4)):
		tmp = lines4[i].split(" ")
		x4.append(float(tmp[0]))
		y4.append(float(tmp[1]))
		
	for i in range(0, len(lines5)):
		tmp = lines5[i].split(" ")
		x5.append(float(tmp[0]))
		y5.append(float(tmp[1]))
		
	fig=plt.figure()
	fig.suptitle(graph_title, fontsize=20)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.plot(x1, y1, label="NoBlocking", marker='o')
	plt.plot(x2, y2, label="Game", marker='o')
	plt.plot(x3, y3, label="Greedy", marker='o')
	plt.plot(x4, y4, label="MaxDegree", marker='o')
	plt.plot(x5, y5, label="Random", marker='o')
	plt.legend(loc="best")
	plt.show()
	fig.savefig("xy_graph.png")
	
'''	
fig = plt.figure()
x = [1,2,3,4]
y = [1,4,9,16]
z = [14, 15, 15, 16]
plt.xlabel("x_label")
plt.ylabel("y_label")
plt.plot(x, y, label="line1")
plt.plot(x, z, label="line2")
plt.legend(loc="best")
#plt.axis([0, 6, 0, 20])
plt.show()
fig.suptitle("Title is here", fontsize=20)
fig.savefig("xy_graph.png")
'''
