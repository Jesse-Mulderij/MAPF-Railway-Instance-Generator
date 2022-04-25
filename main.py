from graph_generator import GraphGenerator
from scenario import Scenario
from scenario_generator import ScenarioGenerator

import os
import configparser


def main(args):
    # Parse arguments
    try:
        nodes = int(args[0])                            # total nodes in the graph
        branches = int(args[1])                         # number of branches of the sjoelbak or the width of the grid
        gate_length = int(args[2])                      # length of the arrival/departure (gate) track
        randomness_parameter = float(args[3])           # 0 < x < 100 ; how much variety in length of the branches
        min_agents = int(args[4])                       # minimum number of agents
        max_agents = int(args[5])                       # maximum number of agents
        num_of_instances_per_num_agents = int(args[6])  # number of instances for each fixed number of agents between min & max agents
        instance_type = args[7]                         # string that indicates which type of instances should be generated, options : random, reversal, arrival, departure
        include_inverted_scen = args[8] == "True"       # bool that indicates whether inverted instances should also be generated
        goal_swap_fraction = float(args[9])             
        start_swap_fraction = float(args[10])
        graph_type = args[11]                           # string that sets the type of graph that is generated, options : shuffleboard, carrousel, grid (not implemented) 
    except Exception as e:
        print("Reading arguments failed due to" + e)
    
    # Set path
    path = "/home/jesse/Documents/GitProjects/InstanceGenerator/quasi_real_instances/"
    path_addon = graph_type + "_" # carrousel not implemented as of yet
    path_addon += instance_type + "_"
    path_addon += str(nodes) + "n_"
    path_addon += str(branches) + "b_"
    path_addon += str(gate_length) + "g_"
    path_addon += str(randomness_parameter) + "r"
    path+=path_addon + "/"
    
    # Generate storage dir
    try:
        os.mkdir(path)
    except FileExistsError:
        print()

    # Generate the graph and write to file
    Graph_gen = GraphGenerator()
    if graph_type == "shuffleboard":
        G = Graph_gen.generate_sjoelbak(path_addon, nodes, branches, gate_length, float(randomness_parameter)/100)
    elif graph_type == "carrousel":
        G = Graph_gen.generate_carrousel(path_addon, nodes, branches, gate_length, float(randomness_parameter)/100)
    elif graph_type == "grid":
        G = Graph_gen.generate_grid(path_addon, nodes, branches)
    else:
        raise Exception("Invalid graph type specified")
    G.write_to_file(path)

    # Generate scenarios and write them to files
    Scen_gen = ScenarioGenerator(G)
    for aa in range(min_agents,max_agents+1):
        for ii in range(num_of_instances_per_num_agents):
            if instance_type == "random": # random start and goal locations are assigned to agents
                S = Scen_gen.generate_random("S", aa)
            elif instance_type == "reversal": # agents are placed on gate track in an order which has to be reversed
                S = Scen_gen.generate_complete_reversal("S", aa)
            elif instance_type == "arrival": # agents start on gate tracks and are assigned goal locations on the parking tracks
                S = Scen_gen.generate_arrival("S", aa)
            elif instance_type == "departure": # agents start on parking tracks and are assigned goal locations on the gate tracks
                S = Scen_gen.generate_departure("S", aa)
            S.swap_starts(start_swap_fraction)
            S.swap_goals(goal_swap_fraction)
            S.write_to_file(path_addon + "_" + str(aa) + "a_" + str(goal_swap_fraction) + "gsf_" + str(start_swap_fraction) + "ssf_" + str(ii), path)
            # Inverted scenario is produced if required
            if include_inverted_scen:
                S.invert()
                S.write_to_file(path_addon + "_" + str(aa) + "a_" + str(ii) + "_inv", path)

            # for agent in S.agents:
            #     print(agent.name)
            #     print(agent.start.name)
            #     print(agent.goal.name)
            #     print("\n")
    return 0


# Read config file and run main with specified settings
cp = configparser.ConfigParser()
cp.read("settings.ini")
main(list(cp['RANDOM SHUFFLEBOARD'].values()))