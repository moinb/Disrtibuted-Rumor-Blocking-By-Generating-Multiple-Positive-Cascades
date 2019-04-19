import pandas as pd

#filename=input("Enter File Name :>").strip('\n')
filename = "degree_of_each_node.txt"
data = pd.read_csv(filename, sep='\s+')
data.sort_values([data.columns[1], data.columns[0]], axis=0, ascending=[False, True], inplace=True)
data.to_csv("degree_of_each_node(sorted).txt", sep = ' ', index = False)

#INPUT -> degree_of_each_node.txt
#OUTPUT -> degree_of_each_node(sorted).txt
