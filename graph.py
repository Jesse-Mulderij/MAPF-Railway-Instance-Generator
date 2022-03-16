from platform import node
import string
from node import Node

class Graph:
    def __init__(self, name : string , nodes : list[Node]):
        self.name = name
        self.nodes = nodes

    def size(self) -> int:
        return self.nodes.__len__()

    def add_node(self, node : Node):
        if(self.nodes.count(node) == 0):
            self.nodes.append(node)

    def remove_node(self, node : Node):
        assert(self.nodes.count(node) == 0)
        self.nodes.remove(node)

    def add_edge(self, node1 : Node, node2 : Node):
        for node in self.nodes:
            if(node == node1):
                node.add_neighbor(node2)
            if(node == node2):
                node.add_neighbor(node1)
    
    def remove_edge(self, node1 : Node, node2 : Node):
        for node in self.nodes:
            if(node == node1):
                node.remove_neighbor(node2)
            if node == node2:
                node.remove_neighbor(node1)
            
    def average_degree(self) -> float:
        num_of_nodes = self.size()
        num_of_edges = sum(node.degree() for node in self.nodes) / 2
        return num_of_edges / num_of_nodes

    def write_to_file(self, dir : string):
        file_name = self.name + ".graph"
        first_lines = "type graph" + "\n"
        first_lines += "nodes " + str(self.nodes.__len__()) + "\n"
        first_lines += "map"
        body = ""
        for node in self.nodes:
            body += "\n"
            body += node.to_string()
            for neighbor in node.neighbors:
                body += " " + neighbor.to_string()
        f = open(dir + file_name,'w')
        f.write(first_lines + body)
        f.close()

