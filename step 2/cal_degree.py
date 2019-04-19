import networkx as nx
import matplotlib.pyplot as plt

filename=input("Enter File Name :>").strip('\n')

g = nx.read_edgelist(filename , nodetype = int, data = (('weight',float),), create_using = nx.Graph())

print("usage: node degree 1/degree")
fp=open("degree_of_each_node.txt", "w")
for i in g.nodes():
	fp.write(str(i) + " " + str(g.degree(i)) + " " + str(1/g.degree(i)) + "\n")
fp.close()

#INPUT -> OUT.TXT
#OUTPUT -> degree_of_each_node.txt
