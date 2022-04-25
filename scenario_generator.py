from hashlib import new
from random import random
from re import split
from graph import Graph
from node import Node
from scenario import Scenario
from agent import Agent

import random
import string

class ScenarioGenerator():
    def __init__(self, graph : Graph):
        self.graph = graph

    def generate_random(self, name : string, num_of_agents : int) -> Scenario:
        S = Scenario(name, self.graph, [])
        starts = random.sample(self.graph.nodes,num_of_agents)
        goals = random.sample(self.graph.nodes, num_of_agents)
        for ii in range(num_of_agents):
            new_agent = Agent(str(ii), None, starts[ii], goals[ii])
            S.add_agent(new_agent)
        return S

    def generate_complete_reversal(self, name: string, num_of_agents : int) -> Scenario:
        S = Scenario(name, self.graph, [])
        gate_nodes = [node for node in self.graph.nodes if node.name[0] == 'g']
        starts = sorted(gate_nodes, key=lambda node: -int(node.name[1:]) )
        goals = sorted(gate_nodes, key=lambda node: int(node.name[1:]) )

        for ii in range(num_of_agents):
            # print(ii)

            new_agent = Agent(str(ii), None, starts[ii], goals[ii])
            S.add_agent(new_agent)
        return S

    def generate_arrival(self, name: string, num_of_agents : int) -> Scenario:
        S = Scenario(name, self.graph, [])
        gate_nodes = [node for node in self.graph.nodes if node.name[0] == 'g']
        starts = sorted(gate_nodes, key=lambda node: -int(node.name[2:]) )
        parking_nodes = [node for node in self.graph.nodes if node.name[0] == 'b']
        goals = sorted(parking_nodes, key=lambda node: -int(split("-",node.name)[-1]) )

        for ii in range(num_of_agents):
            # print(ii)

            new_agent = Agent(str(ii), None, starts[ii], goals[ii])
            S.add_agent(new_agent)
        return S

    def generate_departure(self, name: string, num_of_agents : int) -> Scenario:
        S = Scenario(name, self.graph, [])
        gate_nodes = [node for node in self.graph.nodes if node.name[0] == 'g']
        goals = sorted(gate_nodes, key=lambda node: -int(node.name[2:]) )
        parking_nodes = [node for node in self.graph.nodes if node.name[0] == 'b']
        starts = sorted(parking_nodes, key=lambda node: -int(split("-",node.name)[-1]) )

        for ii in range(num_of_agents):
            # print(ii)

            new_agent = Agent(str(ii), None, starts[ii], goals[ii])
            S.add_agent(new_agent)
        return S