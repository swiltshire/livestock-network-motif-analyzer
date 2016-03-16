__author__ = 'Serge'

from scipy.misc import comb
from collections import Counter
import matplotlib.pyplot as plt
import networkx as nx
import itertools
import numpy as np
import pandas as pd
import xlrd

#import anylogic output xls file
this_adjmatrix = pd.read_excel('LivestockNetworkMotifStudyOutput.xlsx', sheetname='Sheet1').as_matrix()
# print pd.DataFrame (this_adjmatrix)

this_graph = nx.from_numpy_matrix(this_adjmatrix)
n = nx.number_of_nodes(this_graph)
triangle_tracker = []

m1_count_dir = 0
m2_count_dir = 0
m3_count_dir = 0
m4_count_dir = 0
m5_count_dir = 0
m6_count_dir = 0
m7_count_dir = 0
m8_count_dir = 0
m9_count_dir = 0
m10_count_dir = 0
m11_count_dir = 0
m12_count_dir = 0
m13_count_dir = 0

#generate list of unique connected triangles
for node1 in range(n):
	print "Processing Node " + str(node1 + 1) + " of " + str(n)
	for node2 in [x for x in xrange(n) if x != node1 and (this_adjmatrix.item(x, node1) >= 1 or this_adjmatrix.item(node1, x) >= 1)]:
		for node3 in [x for x in xrange(n) if x != node1 and x != node2 and (this_adjmatrix.item(x, node1) >= 1 or this_adjmatrix.item(node1, x) >= 1)]:
			this_triangle = sorted([node1, node2, node3])
			if not this_triangle in triangle_tracker:
				triangle_tracker.append(this_triangle)

#determine motif of each triangle
i = 1
num_tri = len(triangle_tracker)
for triangle in triangle_tracker:
	print "Processing Triangle " + str(i) + " of " + str(num_tri)
	i += 1
	node1, node2, node3 = triangle[0], triangle[1], triangle[2]
	m_code = np.zeros((6,), dtype=np.int)
	m_code_permutations = []
	if this_adjmatrix.item(node2, node1) >= 1:
		m_code[0] = 1
	if this_adjmatrix.item(node1, node2) >= 1:
		m_code[1] = 1
	if this_adjmatrix.item(node3, node2) >= 1:
		m_code[2] = 1
	if this_adjmatrix.item(node2, node3) >= 1:
		m_code[3] = 1
	if this_adjmatrix.item(node1, node3) >= 1:
		m_code[4] = 1
	if this_adjmatrix.item(node3, node1) >= 1:
		m_code[5] = 1

	#generate various permutations for each motif (starting with each node: 3 forward, 3 backward)
	m_code_permutations.append("".join(str(x) for x in m_code))
	m_code_permutations.append("".join(str(x) for x in m_code[2:])+"".join(str(x) for x in m_code[0:2]))
	m_code_permutations.append("".join(str(x) for x in m_code[4:])+"".join(str(x) for x in m_code[0:4]))
	m_code = np.fliplr([m_code])[0]
	m_code_permutations.append("".join(str(x) for x in m_code))
	m_code_permutations.append("".join(str(x) for x in m_code[2:])+"".join(str(x) for x in m_code[0:2]))
	m_code_permutations.append("".join(str(x) for x in m_code[4:])+"".join(str(x) for x in m_code[0:4]))

	#tabulate motifs
	if m_code_permutations.__contains__("100001"):
		m1_count_dir +=1
	elif m_code_permutations.__contains__("010010"):
		m2_count_dir +=1
	elif m_code_permutations.__contains__("010001"):
		m3_count_dir +=1
	elif m_code_permutations.__contains__("010011"):
		m4_count_dir +=1
	elif m_code_permutations.__contains__("100011"):
		m5_count_dir +=1
	elif m_code_permutations.__contains__("110011"):
		m6_count_dir +=1
	elif m_code_permutations.__contains__("101001"):
		m7_count_dir +=1
	elif m_code_permutations.__contains__("101010"):
		m8_count_dir +=1
	elif m_code_permutations.__contains__("101101"):
		m9_count_dir +=1
	elif m_code_permutations.__contains__("011110"):
		m10_count_dir +=1
	elif m_code_permutations.__contains__("011101"):
		m11_count_dir +=1
	elif m_code_permutations.__contains__("011111"):
		m12_count_dir +=1
	elif m_code_permutations.__contains__("111111"):
		m13_count_dir +=1

print "Motif 1 Count: " + str(m1_count_dir)
print "Motif 2 Count: " + str(m2_count_dir)
print "Motif 3 Count: " + str(m3_count_dir)
print "Motif 4 Count: " + str(m4_count_dir)
print "Motif 5 Count: " + str(m5_count_dir)
print "Motif 6 Count: " + str(m6_count_dir)
print "Motif 7 Count: " + str(m7_count_dir)
print "Motif 8 Count: " + str(m8_count_dir)
print "Motif 9 Count: " + str(m9_count_dir)
print "Motif 10 Count: " + str(m10_count_dir)
print "Motif 11 Count: " + str(m11_count_dir)
print "Motif 12 Count: " + str(m12_count_dir)
print "Motif 13 Count: " + str(m13_count_dir)

# pos=nx.spring_layout(this_graph)
# nx.draw_networkx_nodes(this_graph, pos)
# nx.draw_networkx_edges(this_graph, pos)
# nx.draw_networkx_labels(this_graph, pos)
# plt.show()