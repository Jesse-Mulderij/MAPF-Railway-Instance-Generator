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