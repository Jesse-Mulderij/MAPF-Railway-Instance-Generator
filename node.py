import string

class Node:
    def __init__(self, name : string , neighbors : list):
        self.name = name
        self.neighbors = neighbors

    def add_neighbor(self, name : string):
        if(self.neighbors.count(name) == 0):
            self.neighbors.append(name)

    def remove_neighbor(self, name : string):
        assert(self.neighbors.count(name) == 0)
        self.neighbors.remove(name)

    def degree(self) -> int:
        return self.neighbors.__len__()

    def to_string(self) -> string:
        return self.name

    def rename(self, new_name : string):
        self.name = new_name

    def in_branch(self, branch : int)-> bool:
        if self.name[0] == "g":
            return True
        if self.name[0] == "root":
            return False
        if self.name[0] != "b":
            raise Exception("Node not in gate nor in branch nor gate")
        b1 = int(self.name.split("-")[1])
        return b1 == branch

    def dist_to_root(self) -> int:
        if self.name[0] == "g":
            raise Exception("dist to root not implemented for gate nodes")
        if self.name[0] == "root":
            return 0
        if self.name[0] != "b":
            raise Exception("Node not in gate nor in branch nor gate")
        return int(self.name.split("-")[3])
