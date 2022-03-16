from platform import node
import string
from node import Node
from agent import Agent
from graph import Graph

class Scenario:
    def __init__(self, name : string , graph : Graph, agents : list[Agent]):
        self.name = name
        self.graph = graph
        self.agents = agents

    def size(self) -> int:
        return self.agents.__len__()

    def add_agent(self, agent : Agent):
        self.agents.append(agent)

    def remove_agent(self, agent : Agent):
        self.agents.remove(agent)

    def invert_agent(self, agent : Agent):
        self.agents.remove(agent)
        new_agent = Agent(agent.name, agent.goal, agent.start)
        self.agents.append(new_agent)

    def invert(self):
        agents_copy = self.agents.copy()
        for agent in agents_copy:
            self.invert_agent(agent)
    
    def write_to_file(self, filename : string, dir : string):
        file_name = filename + ".scen"
        first_lines = "version 1 graph" + "\n"
        first_lines += self.graph.name + ".graph" + "\n"
        first_lines += "Num_of_Agents " + str(self.agents.__len__()) + "\n"
        body = "types" + "\n" # types not implemented
        body += "agents starts" + "\n"
        for agent in self.agents:
            body += agent.to_string() + " " + agent.start.to_string() + "\n"
        body += "goals"
        for agent in self.agents:
            body += "\n" + agent.to_string() + " " + agent.goal.to_string()
        f = open(dir + "/" + file_name, 'w')
        f.write(first_lines + body)
        f.close()

        