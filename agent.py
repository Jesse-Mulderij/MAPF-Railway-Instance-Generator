import string
from node import Node

class Agent:
    def __init__(self, name : string, type: string, start : Node, goal : Node):
        self.name = name
        if type == None:
            self.type = name
        else:
            self.type = type
        self.start = start
        self.goal = goal

    def match(self, num_of_types : int):
        self.type = str( int(self.name) % num_of_types )

    def to_string(self) -> string:
        return self.name