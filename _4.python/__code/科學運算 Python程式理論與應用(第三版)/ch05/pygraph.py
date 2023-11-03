# -*- coding:utf-8 -*-
# file: pygraph.py
#
def searchGraph(graph, start, end):				# 搜尋樹
	results = []                
	generatePath(graph, [start], end, results)		# 產生路徑
	results.sort(key=lambda x:len(x))		# 按路徑長短排序
	return results
def generatePath(graph, path, end, results):			# 產生路徑
	state = path[-1]
	if state == end:
		results.append(path)
	else:
		for arc in graph[state]:
			if arc not in path: 
				generatePath(graph, path + [arc], end, results)
if __name__ == '__main__':
	Graph = {'A':  ['B', 'C', 'D'],				# 建構樹
	         'B':  ['E'],
	         'C':  ['D', 'F'],
	         'D':  ['B', 'E', 'G'],
	         'E':  [],
	         'F':  ['D', 'G'],
	         'G':  ['E']}
	r = searchGraph(Graph, 'A','D')				# 搜尋A到D的所有路徑
	print('************************')
	print('     path A to D')
	print('************************')
	for i in r:
		print(i)
	r = searchGraph(Graph, 'A','E')				# 搜尋A到E的所有路徑
	print('************************')
	print('     path A to E')
	print('************************')
	for i in r:
		print(i)
	r = searchGraph(Graph, 'C','E')				# 搜尋C到E的所有路徑
	print('************************')
	print('     path C to E')
	print('************************')
	for i in r:
		print(i)
