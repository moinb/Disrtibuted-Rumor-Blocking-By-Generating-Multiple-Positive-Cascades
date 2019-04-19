from array import *
import random

node_list = []
time_interval = 0
R_act_nodes = 0

class Node():
	def __init__(self, nodeId, flag):
		self.nodeId = nodeId
		self.flag = flag
		self.aOrder = []

def find_max_int_from_file(filename):
	largest = 0
	fp = open(filename, "r")
	lines = fp.readlines()
	for i in range(0, len(lines)):
		tmp = lines[i].split(" ")
		x = int(tmp[0])
		y = int(tmp[1])
		if largest < x:
			largest = x
		if largest < y:
			largest = y
	fp.close()
	return largest

def init_list(largest, filename, filename1):
	global node_list
	for i in range (0, largest+1):
		node_list.append(Node(i, 3))
	fp = open(filename, "r")
	lines = fp.readlines()
	for i in range (0, len(lines)):
		tmp = lines[i].split(" ")
		node_list[int(tmp[0])].flag = 2
		node_list[int(tmp[1])].flag = 2
	fp.close()
	fp = open(filename1, "r")
	lines = fp.readlines()
	for i in range (0, len(lines)):
		tmp = lines[i].split(" ")
		if int(tmp[0]) <= largest:
			node_list[int(tmp[0])].flag = int(tmp[1])
	fp.close()
	fp = open(filename, "r")
	lines = fp.readlines()
	for i in range (0, len(lines)):
		tmp = lines[i].split(" ")
		node_list[int(tmp[0])].aOrder.append([])
		l1 = len(node_list[int(tmp[0])].aOrder)
		node_list[int(tmp[0])].aOrder[l1 - 1].append(int(tmp[1]))
		node_list[int(tmp[0])].aOrder[l1 - 1].append(float(tmp[2]))
		node_list[int(tmp[1])].aOrder.append([])
		l2 = len(node_list[int(tmp[1])].aOrder)
		node_list[int(tmp[1])].aOrder[l2 - 1].append(int(tmp[0]))
		node_list[int(tmp[1])].aOrder[l2 - 1].append(float(tmp[3]))
	fp.close()
	for i in range (0, len(node_list)):
		node_list[i].aOrder.sort(key = lambda x:x[1], reverse = True)
	return


def first_thread():
	global counter
	global node_list
	active_nodes = []
	for i in range(0, len(node_list)):
		if (node_list[i].flag == 0) or (node_list[i].flag == 1):
			active_nodes.append(i)
	length = len(active_nodes)
	for i in range(0, length):
		ran_int = random.randint(0,len(active_nodes) - 1)
		tmp0 = active_nodes[ran_int]
		del active_nodes[ran_int]
		for j in range(0, len(node_list[tmp0].aOrder)):
			tmp1 = node_list[tmp0].aOrder[j]
			if node_list[tmp1[0]].flag == 2:
				node_list[tmp1[0]].flag = node_list[tmp0].flag
				break
			
				
		
def simulateP2P():
	counter = 0
	l = len(node_list)
	z = 0
	fp = open("55.txt", "w")
	while 1:
		rumor_act_nodes = 0
		counter = 0
		for i in range(0, len(node_list)):
			if node_list[i].flag == 0:
				rumor_act_nodes = rumor_act_nodes + 1	
			if node_list[i].flag != 2:
				counter = counter + 1
		fp.write(str(z)+" "+str(rumor_act_nodes)+"\n")
		if counter == l:
			break
		z = z + 1
		first_thread()
	fp.close()
	print("loop runs:", z)
	return	
	
def main():
	global node_list
	global time_interval
	global R_act_nodes
	filename = input("Enter File Name with all graph information:>").strip('\n') #1.txt
	filename1 = input("Enter File Name with seed node information:>").strip('\n') #2.txt
	#time_interval = input("Enter time interval for p2p:>").strip('\n')
	largest = find_max_int_from_file(filename)
	init_list(largest, filename, filename1)
	simulateP2P()
	#print(counter)
	filename2 = open("status_Random.txt", "w")
	for i in range(0, len(node_list)):
		#print(node_list[i].nodeId, node_list[i].flag)
		filename2.write(str(node_list[i].nodeId)+" "+str(node_list[i].flag)+"\n")
		if node_list[i].flag == 0:
			R_act_nodes = R_act_nodes + 1
	filename2.close()
	print("Rumor activated nodes are:", R_act_nodes)
	

main()
