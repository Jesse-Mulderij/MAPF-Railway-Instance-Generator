from numpy import number
from graph_generator import GraphGenerator
from graph import Graph
from node import Node
from scenario_generator import ScenarioGenerator
from scenario import Scenario
from agent import Agent
import os

def main(args):
    nodes = args[0]                             # total nodes in the graph
    branches = args[1]                          # number of branches of the sjoelbak
    gate_length = args[2]                       # length of the arrival/departure (gate) track
    randomness_parameter = args[3]              # 0 < x < 100 ; how much variety in length of the branches
    min_agents = args[4]                        # minimum number of agents
    max_agents = args[5]                        # maximum number of agents
    num_of_instances_per_num_agents = args[6]   # number of instances for each fixed number of agents between min & max agents
    generate_random = args[7]                   # bool that indicates whether random starts and goals scenarios are generated
    generate_reversal = args[8]                 # bool that indicates whether reversal scenarios are generated

    Graph_gen = GraphGenerator()
    path = "/home/jesse/Documents/GitProjects/InstanceGenerator/quasi_real_instances/"
    path_addon = "sjoelbak_" # carrousel not implemented as of yet
    path_addon += str(nodes) + "n_"
    path_addon += str(branches) + "b_"
    path_addon += str(gate_length) + "g_"
    path_addon += str(randomness_parameter) + "r"
    path+=path_addon + "/"
    try:
        os.mkdir(path)
    except FileExistsError:
        print()


    G = Graph_gen.generate_sjoelbak(path_addon, nodes, branches, gate_length, float(randomness_parameter)/100)
    G.write_to_file(path)
    Scen_gen = ScenarioGenerator(G)
    for aa in range(min_agents,max_agents+1):
        for ii in range(num_of_instances_per_num_agents):
            if generate_random:
                S = Scen_gen.generate_random("S", aa)
                S.write_to_file(path_addon + str(aa) + "a_" + str(ii), path)
            elif generate_reversal:
                S = Scen_gen.generate_complete_reversal("S", aa)
                S.write_to_file(path_addon + str(aa) + "a_" + str(ii), path)
            # for agent in S.agents:
            #     print(agent.name)
            #     print(agent.start.name)
            #     print(agent.goal.name)
            #     print("\n")

            S.write_to_file(path_addon + "_" + str(aa) + "a_" + str(ii), path)
    return 0



nodes = 20
branches = 1
gate_length = 10
randomness_parameter = 0
min_agents = 2
max_agents = 10
num_of_instances_per_num_agents = 1
generate_random = False
generate_reversal = True

args = [nodes, branches, gate_length, randomness_parameter, min_agents, max_agents, num_of_instances_per_num_agents, generate_random, generate_reversal]
main(args)