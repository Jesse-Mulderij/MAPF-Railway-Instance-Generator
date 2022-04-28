from platform import node
import string
from random import sample
from numpy import random
import numpy as np

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
        new_agent = Agent(agent.name, agent.color, agent.goal, agent.start)
        self.agents.append(new_agent)

    def invert(self):
        agents_copy = self.agents.copy()
        for agent in agents_copy:
            self.invert_agent(agent)
    
    def swap_starts_pair(self, a1: Agent, a2: Agent):
        start1 = a1.start
        start2 = a2.start
        a1.start = start2
        a2.start = start1

    def swap_goals_pair(self, a1: Agent, a2: Agent):
        goal1 = a1.goal
        goal2 = a2.goal
        a1.goal = goal2
        a2.goal = goal1

    def swap_goals(self, i : int):
        agent_sample = sample(self.agents, i)
        for a1 in agent_sample:
            agent_sample.remove(a1)
            try:
                otheragents = [1 for agent in self.agents]
                otheragents[self.agents.index(a1)] = 0
                a2 = sample(self.agents, 1, counts=otheragents).pop()
                self.swap_goals_pair(a1, a2)
                # print("(" + a1.name + "," + a2.name + ")")
            except Exception: # as e:
                #print(e)
                continue

    def get_types(self) -> list:
        types = []
        for agent in self.agents:
            if types.count(agent.type) == 0:
                types.append(agent.type)
        return types

    def swap_starts(self, i : int):
        agent_sample = sample(self.agents, i)
        for a1 in agent_sample:
            agent_sample.remove(a1)
            try:
                otheragents = [1 for agent in self.agents]
                otheragents[self.agents.index(a1)] = 0
                a2 = sample(self.agents, 1, counts=otheragents).pop()
                self.swap_starts_pair(a1, a2)
                # print("(" + a1.name + "," + a2.name + ")")
            except Exception as e:
                # print(e)
                continue

    def match(self, num_of_types : int):
        for agent in random.permutation(self.agents):
            agent.match(num_of_types)

    def write_to_file(self, filename : string, dir : string):
        file_name = filename + ".scen"
        first_lines = "version 1 graph" + "\n"
        first_lines += self.graph.name + ".graph" + "\n"
        first_lines += "Num_of_Agents " + str(self.agents.__len__()) + "\n"
        body = "types" + "\n"
        for type in self.get_types():
            body += type
            for agent in self.agents:
                if agent.type == type:
                    body += " " + agent.to_string()
            body += "\n"
        body += "agents starts" + "\n"
        for agent in self.agents:
            body += agent.to_string() + " " + agent.start.to_string() + "\n"
        body += "goals"
        for agent in self.agents:
            body += "\n" + agent.type + " " + agent.goal.to_string()
        f = open(dir + "/" + file_name, 'w')
        f.write(first_lines + body)
        f.close()

        