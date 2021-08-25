from collections import defaultdict
import pprint

class Graph:
	def __init__(self, n):
		#self.graph = defaultdict(list)
		self.graph = [[0 for x in range(n)] for y in range(n)]

	def print_graph(self):
		pprint.pprint(self.graph)


	def add_edge(self, edge, value):
		self.graph[edge].append(value)
		#self.graph[value].append(edge)		#undirected graph

	def grid_implementation(self, x, y):
		self.graph[x][y]=1


	def DFS(self, edge, visited=set()):
		print(edge, end=" ")
		visited.add(edge)
		for neighbour in self.graph[edge]:
			if neighbour not in visited:
				self.DFS(neighbour, visited)

	def check_cyclic(self, edge, visited=set()):
		#print(edge,"k")
		if edge in visited:
			return True

		if len(visited)==len(self.graph):
			return False
		visited.add(edge)
		for neighbour in self.graph[edge]:
			if neighbour not in visited:
				return self.check_cyclic(neighbour, visited)
			return True
 

	
	def BFS(self, edge, visited=set(), q=[]):
		print(edge,end=" ")
		visited.add(edge)
		for neighbour in self.graph[edge]:
			if neighbour not in visited and neighbour not in q:
				q.append(neighbour)
		while q:
			next_edge = q.pop(0)
			self.BFS(next_edge, visited, q)


	def disconnected(self, f):
		visited=set()
		print(f.__name__)
		for edge in list(self.graph):
			if edge not in visited:
				#print(edge,'g')
				f(edge, visited)
					


g = Graph(7)
#g.add_edge(0, 1)
##g.add_edge(0, 5)
##g.add_edge(0, 2)
#g.add_edge(1, 2)
##g.add_edge(2, 0)
#g.add_edge(2, 3)
##g.add_edge(3, 3)
#g.add_edge(3, 4)
#g.add_edge(5,6)
#g.add_edge(7,9)
g.grid_implementation(0,1)
g.grid_implementation(0,5)
g.grid_implementation(0,2)
g.grid_implementation(1,2)
g.grid_implementation(2,0)
g.grid_implementation(2,3)
g.grid_implementation(3,4)
g.grid_implementation(5,6)
g.grid_implementation(6,4)
g.print_graph()
#print()
#g.disconnected(g.BFS)
#print("\n")
##print()
#g.BFS(2)
#print("\n")
#g.DFS(2)
#print("\n")
#if g.check_cyclic(0):		#directed graph
#	print("yes")
#else:
#	print("NO") 
#print("\n")
#g.disconnected(g.DFS)