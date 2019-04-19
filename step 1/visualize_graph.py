import networkx as nx
import matplotlib.pyplot as plt

filename=input("Enter File Name :>").strip('\n')

g = nx.read_edgelist(filename , nodetype=int,
  data=(('weight',float),), create_using=nx.Graph())

sp = nx.spring_layout(g) # positions for all nodes
nx.draw(g, sp, with_labels = False)
labels = nx.get_edge_attributes(g,'weight')
nx.draw_networkx_edge_labels(g,pos=sp,edge_labels=labels)
plt.savefig('fbgraph.png')
plt.show()

#input -> out.txt
