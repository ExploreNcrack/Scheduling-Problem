def all_combination(all_order,current_order, used, Vertices):
	#generate all possible combination orders of the graph nodes in which they will be colored first
	if len(current_order) == len(Vertices):
		tmp = []
		for i in current_order:
			tmp.append(i)
		all_order.append(tmp)
		return
	else:
		for vertex in Vertices:
			if vertex not in used:
				used[vertex] = None
				current_order.append(vertex)
				all_combination(all_order,current_order, used, Vertices)
				del used[vertex]
				current_order.pop()


def color_in_order_comb(color_used, color_map, count_and_comb, l, Edges, comb):
	
	if l == len(comb):
		#all nodes are colored
		#collect the color map and number of color used
		count_and_comb.append([len(color_used),comb,color_map])
	else:
		#keep coloring the nodes
		color_cannot_use = {}
		current_node = comb[l]
		for edge in Edges[current_node]:
			if edge in color_map:
				color_cannot_use[color_map[edge]] = None
		#find which old color can be reused
		color_can_use = []
		# old color set minus color cannot use set = colors can reuse
		for color in color_used:
			if color not in color_cannot_use:
				color_can_use.append(color)
		if len(color_can_use) == 0:
			#new color is needed
			new_color = color_used[-1]+1
			color_used.append(new_color)
			color_map[current_node]=new_color
			color_in_order_comb(color_used, color_map, count_and_comb, l+1, Edges, comb)
		else:
			#can reuse old color
			for color in color_can_use:
				color_map_copy = color_map.copy()
				color_map_copy[current_node]=color
				color_used_copy = []
				for i in color_used:
					color_used_copy.append(i)
				color_in_order_comb(color_used_copy, color_map_copy, count_and_comb, l+1, Edges, comb)





def main():
	Vertices = [1,2,3,4,5]
	Vertices1 = [1,2,3,4,5,6]
	Edges = {2:[1,3,4], 1:[2,3], 3:[1,2,4], 4:[2,3,5], 5:[4]}
	Edges1 = {1:[2,3,4,5], 2:[1,3,4,6], 3:[1,2,5,6], 4:[1,2,5,6], 5:[1,3,4,6], 6:[2,3,4,5]}
	all_order = []
	current_order=[]
	used={}
	all_combination(all_order,current_order, used, Vertices)
	count_and_comb=[]
	for comb in all_order:
		color_used = [0]
		color_map = {comb[0]:0}
		color_in_order_comb(color_used, color_map, count_and_comb, 1, Edges, comb)
	count_and_comb = sorted(count_and_comb, key=lambda x: x[0])
	for i in count_and_comb:
		print(i)
	print(len(count_and_comb))
	print("Minimum different colors needed to color the graph is: %d"%(count_and_comb[0][0]))
main()

