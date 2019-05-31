"""
Task 4. 
Write an algorithm which, given a graph G and a number k, returns a clique of 
at least size k, or False if no clique exists.
Then write a function that finds the largest clique in a graph. 

For this first function, we are just going to use back tracking. 
To do so, we should answer the following questions:
1. How do we represent a partial solution?
2. What is our starting partial solution?
3. How do we extend a partial solution?
4. How do we know if we have found a complete solution?
"""

def find_clique(G, k, partial = []):

	# Terminate if length of the partial solution is sufficient length
	if len(partial) >= k:
		return partial
	
	# Look at each possible extension and build up partial solution
	# Call find_clique on partial solution to continually build
	# Up the partial solution until it is of sufficient length
	possible_extensions = extensions(G, partial)
	for v in possible_extensions:
		extended_partial = partial + [v]
		clique = find_clique(G, k, extended_partial)
		if clique:
			return clique
	
	return False



def extensions(G, partial):	
	# Need to iterate over every node after last node in
	# partial solution and add to list of viable nodes if 
	# they share an edge with every node in partial solution.
	
	# Find last node:
	if len(partial) == 0:
		last_vertex = -1
	else:
		last_vertex = partial[-1]

	possible_extensions = []  # List to add extensions to
	
	# Iterate over all possible nodes with index
	# greater than the last vertex
	for v in range(last_vertex+1, len(G)):
		possible = True  # Boolean to track if node is viable

		# Iterate over each node in partial and check if 
		# v shares an edge with all of them
		for u in partial:
			if G[v][u] == 0:
				# If no edge, the node is not viable, update boolean
				possible = False
		
		# If node is a possible extension, add to list
		if possible:
			possible_extensions.append(v)

	return possible_extensions


def find_largest_clique(G):
	# Iterate from maximum size clique to minimum
	for k in range(len(G), -1, -1):
		clique_size_k = find_clique(G, k)
		# If it exists, we're done, return it
		if clique_size_k:
			return clique_size_k



example_graph =\
       [[0, 1, 0, 0, 0, 0, 0],
		[1, 0, 1, 1, 0, 0, 0],
		[0, 1, 0, 1, 1, 1, 0],
		[0, 1, 1, 0, 1, 1, 0],
		[0, 0, 1, 1, 0, 1, 1],
		[0, 0, 1, 1, 1, 0, 1],
		[0, 0, 0, 0, 1, 1, 0]]

example_graph_complement =\
	   [[0, 0, 1, 1, 1, 1, 1],
		[0, 0, 0, 0, 1, 1, 1],
		[1, 0, 0, 0, 0, 0, 1],
		[1, 0, 0, 0, 0, 0, 1],
		[1, 1, 0, 0, 0, 0, 0],
		[1, 1, 0, 0, 0, 0, 0],
		[1, 1, 1, 1, 0, 0, 0]]


if __name__ == "__main__":
	print(find_clique(example_graph, 3))
	print(find_clique(example_graph_complement, 3))

	print(find_largest_clique(example_graph))
	print(find_largest_clique(example_graph_complement))







































"""
1. List of vertices in the clique. 
2. An empty subset of vertices. (Empty list)
3. Each vertex has an index. Look at the last vertex in the partial solution. 
   Consider every node in the graph with an index larger than the last vertex
   in the partial solution. If any of these vertices have an edge connecting it
   to every node in the partial solution, it is a viable extension. 
4. We have a partial solution of length k or greater. 
"""
