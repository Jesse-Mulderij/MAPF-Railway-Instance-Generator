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
        if(num_of_nodes < num_of_branches + gate_length):
            raise Exception("Not enough nodes to divide over gate and branches")
        
        # Construct gate
        new_node = Node("g" + str(0),[])
        for ii in range(1, gate_length+1):
            new_node = Node("g" + str(ii),[])
            G.add_node(new_node)
            for node in G.nodes:
                if node.name == "g" + str(ii-1):
                    G.add_edge(new_node, node)
        root_node = new_node

        # Construct sjoelbak       
        branch_lengths = [1 for i in range(num_of_branches)]
        nodes_to_do = num_of_nodes - num_of_branches - gate_length
        index = 0
        while nodes_to_do >= 0:
            increase = 1 + round(random.uniform(0,1)*rand_par*(nodes_to_do-1))
            branch_lengths[index] += increase
            nodes_to_do -= increase
            index = ( index + 1 ) % num_of_branches

        for ii in range(num_of_branches):
            new_node = Node("b" + str(ii) + "p0",[])
            G.add_node(new_node)
            G.add_edge(new_node,root_node)
            for jj in range(1, branch_lengths[ii]):
                new_node = Node("b" + str(ii) + "p" + str(jj),[])
                G.add_node(new_node)
                for node in G.nodes:
                    if ( node.name == ("b" + str(ii) + "p" + str(jj-1) )):
                        G.add_edge(new_node, node)
        return G
