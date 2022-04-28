from graph import Graph
from node import Node
import string
import random

class GraphGenerator():
    def __init__(self):
        pass
    
    def generate_test_graph(self, name : string, num_of_nodes : int) -> Graph:
        G = Graph(name, [])
        while G.size() is not num_of_nodes:
            new_node = Node(str(G.size()), [])
            G.add_node(new_node)
        return G

    def generate_binary_tree(self, name : string, num_of_nodes : int) -> Graph:
        G = Graph(name, [])
        root = Node("root", [])
        G.add_node(root)
        while G.size() is not num_of_nodes:
            new_node = Node(str(G.size()), [])
            G.add_node(new_node)
            for node in G.nodes:
                if(node.degree() < 2 or (node.name != "root" and node.degree() < 3) ):
                    G.add_edge(node,new_node)
                    break
        return G

    def generate_simple_path(self, name : string, num_of_nodes : int) -> Graph:
        G = Graph(name, [])
        head = Node("0", [])
        while G.size() is not num_of_nodes:
            new_node = Node(str(G.size()), [])
            G.add_node(new_node)
            for node in G.nodes:
                if(node.name == str(G.size()-1)):
                    G.add_edge(node,new_node)
        return G

    def generate_sjoelbak(self, name : string, num_of_nodes : int, num_of_branches : int, gate_length : int, rand_par : float) -> Graph:
        G = Graph(name, [])
        if(num_of_nodes < (num_of_branches + gate_length) ):
            print("Number of nodes is " + str(num_of_nodes) + "\n")
            print("Number of branches is " + str(num_of_branches) + "\n")
            print("Gate length is " + str(gate_length) + "\n")
            print(str(num_of_nodes) + " < " + str(num_of_branches) + " + " + str(gate_length))
            raise Exception("Not enough nodes to divide over gate and branches")
        
        # Construct gate
        new_node = Node("g-" + str(0),[])
        for ii in range(1, gate_length+1):
            new_node = Node("g-" + str(ii),[])
            G.add_node(new_node)
            for node in G.nodes:
                if node.name == "g-" + str(ii-1):
                    G.add_edge(new_node, node)
        root_node = new_node

        # Construct sjoelbak       
        branch_lengths = [1 for i in range(num_of_branches)]
        nodes_to_do = num_of_nodes - num_of_branches - gate_length
        index = 0
        while nodes_to_do > 0:
            increase = 1 + round(random.uniform(0,1)*rand_par*(nodes_to_do-1))
            branch_lengths[index] += increase
            nodes_to_do -= increase
            index = ( index + 1 ) % num_of_branches

        for ii in range(num_of_branches):
            new_node = Node("b-" + str(ii) + "-p-0",[])
            G.add_node(new_node)
            G.add_edge(new_node,root_node)
            for jj in range(1, branch_lengths[ii]):
                new_node = Node("b-" + str(ii) + "-p-" + str(jj),[])
                G.add_node(new_node)
                for node in G.nodes:
                    if ( node.name == ("b-" + str(ii) + "-p-" + str(jj-1) )):
                        G.add_edge(new_node, node)
        return G

    def generate_carrousel(self, name : string, num_of_nodes : int, num_of_branches : int, gate_length : int, rand_par : float) -> Graph:
        G = self.generate_sjoelbak(name, num_of_nodes, num_of_branches, gate_length, rand_par)
        heads = [None for branch in range(G.num_of_branches())]
        for node in G.nodes:
            if node.name[0] != "b":
                continue
            for branch in range(G.num_of_branches()):
                if node.in_branch(branch):
                    if heads[branch] == None:
                        heads[branch] = node
                    elif heads[branch].dist_to_root() < node.dist_to_root():
                        heads[branch] = node
        for branch in range(G.num_of_branches()-1):
            G.add_edge(heads[branch], heads[branch+1])
        return G

    def generate_grid(self, name: string, num_of_nodes: int, width : int) -> Graph:
        G = Graph(name, [])
        if num_of_nodes % width != 0:
            raise Exception("Num of nodes not divisible by width")
        height = int(num_of_nodes / width)

        # Generate Nodes
        for y1 in range(height):
            for x1 in range(width):
                neighbors = []
                for x2 in [x1+1, x1, x1-1]:
                    for y2 in [y1+1, y1, y1-1]:
                        if abs(x1-x2) + abs(y1-y2) == 1 and x2 >= 0 and y2 >= 0  and x2 < width and y2 < height:
                            n2 = Node("(" + str(x2) + "," + str(y2) + ")", [])
                            neighbors.append(n2)
                n = Node("(" + str(x1) + "," + str(y1) + ")", neighbors)                
                G.add_node(n)
        return G