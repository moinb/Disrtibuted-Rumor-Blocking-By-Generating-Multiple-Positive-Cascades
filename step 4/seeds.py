import random
from random import sample
import networkx as nx

if __name__ == "__main__":
	nodes = []
	nodes_copy = []
	filename1 = input("Enter File Name containing edge information:>").strip('\n')
	filename = input("Enter file SORTED ON DEGREE:>").strip("\n")
	k = input("Enter k value(Budget):>").strip("\n")
	g = nx.read_edgelist(filename1 , nodetype = int, data = (('weight',float),), create_using = nx.Graph())
	fp = open(filename, "r")
	lines = fp.readlines()
	for i in range(0, len(lines)):
		tmp = lines[i].split(" ")
		nodes.append(int(tmp[0]))
		nodes_copy.append(int(tmp[0]))
	flag = input("How to select rumor seed node?\nmanual: 0\nrandom: 1\n").strip("\n")
	if flag == "0":
		rumor_seed = int(input("Enter rumor seed node ID:>").strip("\n"))
	else:
		rumor_seed = random.choice(nodes)
		
	for i in range(0, len(nodes)):
		if nodes[i] == rumor_seed:
			del nodes_copy[i]
			break
	#print(rumor_seed)
	#print(nodes_copy)
	
	#NoBlocking	
	fp1 = open("NoBlocking_seeds.txt", "w")
	fp1.write(str(rumor_seed)+" "+"0"+"\n")
	fp1.close()
	
	#random
	fp1 = open("Random_seeds.txt", "w")
	fp1.write(str(rumor_seed)+" "+"0"+"\n")
	random_seeds = sample(nodes_copy, int(k))
	for i in range(0, len(random_seeds)):
		fp1.write(str(random_seeds[i])+" "+"1"+"\n")
	fp1.close()
	
	#MaxDegree
	fp1 = open("MaxDegree_seeds.txt", "w")
	fp1.write(str(rumor_seed)+" "+"0"+"\n")
	for i in range(0, int(k)):
		fp1.write(str(nodes_copy[i])+" "+"1"+"\n")
	fp1.close()
	
	nodes_copy = []
	for i in range(0, len(nodes)):
		nodes_copy.append(nodes[i])
	#print(nodes_copy)	
	
	
	agents = []
	for i in range(0, int(k)):
		agents.append(sample(nodes_copy, random.choice([2, 3, 4])))
		for j in range(0, len(agents[i])):
			nodes_copy.remove(agents[i][j])
		#print(agents[i])
		
	#Game
	game_seeds = []
	for i in range(0, int(k)):
		min_dist = nx.shortest_path_length(g,source = agents[i][0], target = rumor_seed)
		min_dist_node_index = 0
		for j in range(0, len(agents[i])):
			tmp = nx.shortest_path_length(g,source = agents[i][j], target = rumor_seed)
			if (min_dist > tmp):
				min_dist = tmp
				min_dist_node_index = j
		min_dist_nodes = []
		for j in range(0, len(agents[i])):
			if (min_dist == nx.shortest_path_length(g,source = agents[i][j], target = rumor_seed)):
				min_dist_nodes.append(agents[i][j])
		max_degree_node = min_dist_nodes[0]
		for j in range(0, len(min_dist_nodes)):
			if g.degree(max_degree_node) < g.degree(min_dist_nodes[j]):
				max_degree_node = min_dist_nodes[j]	
		game_seeds.append(max_degree_node)
	fp1 = open("Game_seeds.txt", "w")
	fp1.write(str(rumor_seed)+" "+"0"+"\n")
	for j in range(0, len(game_seeds)):
		fp1.write(str(game_seeds[j])+" "+"1"+"\n")
	fp1.close()
	#print(game_seeds)
	
	#Greedy
	greedy_seeds = []
	for i in range(0, int(k)):
		max_degree_node = agents[i][0]
		for j in range(0, len(agents[i])):
			if g.degree(agents[i][j]) > g.degree(max_degree_node):
				max_degree_node = agents[i][j]
		greedy_seeds.append(max_degree_node)
	fp1 = open("Greedy_seeds.txt", "w")
	fp1.write(str(rumor_seed)+" "+"0"+"\n")
	for j in range(0, len(greedy_seeds)):
		fp1.write(str(greedy_seeds[j])+" "+"1"+"\n")
	fp1.close()
	'''
	count = 1
	for i in range(0, 5):
		fp1 = open("NoBlocking_seeds.txt", "w")
		fp2 = open("Random_seeds.txt", "w")
		fp3 = open("MaxDegree_seeds.txt", "w")
		
		fp1.write(str(rumor_seed)+" "+"0"+"\n")
		fp1.close()
		fp2.write(str(rumor_seed)+" "+"0"+"\n")
		fp3.write(str(rumor_seed)+" "+"0"+"\n")
		
		for j in range(0, count):
			fp2.write(str(random_seeds[j])+" "+"1"+"\n")
			fp3.write(str(nodes_copy[j])+" "+"1"+"\n")
		count = count + 1
		tmp = input("enter any key").strip("\n")
		fp2.close()
		fp3.close()
	'''
