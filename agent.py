import string
from node import Node

class Agent:
    def __init__(self, name : string , start : Node, goal : Node):
        self.name = name
        self.start = start
        self.goal = goal

    def to_string(self) -> string:
        return self.name