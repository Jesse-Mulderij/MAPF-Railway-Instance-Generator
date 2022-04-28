from graph_generator import GraphGenerator
from scenario import Scenario
from scenario_generator import ScenarioGenerator
from itertools import permutations
from utils import kendall_tau
import os
import configparser


def main(args):
    # Parse arguments
    try:
        experiment_number = args[0]                     # if 2 do reversals, if 3 do 
        nodes = int(args[1])                            # total nodes in the graph
        branches = int(args[2])                         # number of branches of the sjoelbak or the width of the grid
        gate_length = int(args[3])                      # length of the arrival/departure (gate) track
        randomness_parameter = float(args[4])           # 0 < x < 100 ; how much variety in length of the branches
        min_agents = int(args[5])                       # minimum number of agents
        max_agents = int(args[6])                       # maximum number of agents
        num_of_instances_per_num_agents = int(args[7])  # number of instances for each fixed number of agents between min & max agents
        instance_type = args[8]                         # string that indicates which type of instances should be generated, options : random, reversal, arrival, departure
        include_inverted_scen = args[9] == "True"       # bool that indicates whether inverted instances should also be generated
        goal_swaps = int(args[10])             
        start_swaps = int(args[11])
        graph_type = args[12]                           # string that sets the type of graph that is generated, options : shuffleboard, carrousel, grid (not implemented) 
        num_of_types = int(args[13])                    # number of types of agents
    
    except Exception as e:
        print("Reading arguments failed due to" + e)
    
    # Set path
    path = "/home/jesse/Documents/GitProjects/InstanceGenerator/quasi_real_instances/" + "exp" + experiment_number + "/"
    path_addon = graph_type + "_"
    path_addon += instance_type + "_"
    if goal_swaps + start_swaps < 0:
        path_addon += 'hard_'
    path_addon += str(num_of_types) + "t_"
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
    
    Graph_gen = GraphGenerator()

    if experiment_number[0] == "1":
        # Generate the graph and write to file
        if graph_type == "shuffleboard":
            G = Graph_gen.generate_sjoelbak(path_addon, nodes, branches, gate_length, float(randomness_parameter)/100)
        elif graph_type == "carrousel":
            G = Graph_gen.generate_carrousel(path_addon, nodes, branches, gate_length, float(randomness_parameter)/100)
        else:
            raise Exception("Invalid graph type specified")
        G.write_to_file(path)

        # Generate scenarios and write them to files
        Scen_gen = ScenarioGenerator(G)
        for aa in range(min_agents,max_agents+1):
            for ii in range(num_of_instances_per_num_agents):
                if instance_type == "random": # random start and goal locations are assigned to agents
                    S = Scen_gen.generate_random("S", aa)
                elif instance_type == "complete reversal": # agents are placed on gate track in an order which has to be reversed
                    S = Scen_gen.generate_complete_reversal("S", aa)
                elif instance_type == "reversal": # agents are placed on gate track in an order which has to be reversed
                    S = Scen_gen.generate_complete_reversal("S", aa)
                elif instance_type == "standstill":
                    S = Scen_gen.generate_standstill("S", aa)
                elif instance_type == "arrival": # agents start on gate tracks and are assigned goal locations on the parking tracks
                    S = Scen_gen.generate_arrival("S", aa)
                elif instance_type == "departure": # agents start on parking tracks and are assigned goal locations on the gate tracks
                    S = Scen_gen.generate_departure("S", aa)
                
                # Sometimes we simply swap half of the agents' starts or goals with another agent instead of a specific number of them
                if(start_swaps == -1):
                    start_swaps = round( aa / 2 )
                S.swap_starts(start_swaps)

                if(goal_swaps == -1):
                    goal_swaps = round( aa / 2 )
                S.swap_goals(goal_swaps)

                # Assign each to a type if number of types is specified
                if num_of_types != 0:
                    S.match(num_of_types)
                S.write_to_file(path_addon + "_" + str(aa) + "a_" + str(goal_swaps) + "gs_" + str(start_swaps) + "ss_" + str(num_of_types) + "types_" + str(ii), path)

        return 0

    if experiment_number[0] == "2":
        if graph_type == "shuffleboard":
            G = Graph_gen.generate_sjoelbak(path_addon, nodes, branches, gate_length, float(randomness_parameter)/100)
        else:
            raise Exception("Invalid graph type specified")
        G.write_to_file(path)
        Scen_gen = ScenarioGenerator(G)
        assert(min_agents == max_agents) # this experiment assumes a fixed number of agents.
        instance_counter = 0
        # loop over all permutations to generate all possible reversal scenarios
        for permutation in permutations(range(max_agents), max_agents):
            if instance_type == "reversal":
                S = Scen_gen.generate_sequence("S", permutation)
            S.write_to_file(path_addon + "_" + str(max_agents) + "a_" + str(goal_swaps) + "gs_" + str(start_swaps) + "ss_" + str(kendall_tau(permutation)) + "tau_" + str(instance_counter), path)
            instance_counter += 1
        return 0

    elif experiment_number[0] == "3":
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
                S.write_to_file(path_addon + "_" + str(aa) + "a_" + str(goal_swaps) + "gs_" + str(start_swaps) + "ss_" + str(ii), path)
        return 0


    else:
        # Generate the graph and write to file
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
                elif instance_type == "complete reversal": # agents are placed on gate track in an order which has to be reversed
                    S = Scen_gen.generate_complete_reversal("S", aa)
                elif instance_type == "reversal": # agents are placed on gate track in an order which has to be reversed
                    S = Scen_gen.generate_complete_reversal("S", aa)
                elif instance_type == "standstill":
                    S = Scen_gen.generate_standstill("S", aa)
                elif instance_type == "arrival": # agents start on gate tracks and are assigned goal locations on the parking tracks
                    S = Scen_gen.generate_arrival("S", aa)
                elif instance_type == "departure": # agents start on parking tracks and are assigned goal locations on the gate tracks
                    S = Scen_gen.generate_departure("S", aa)
                S.swap_starts(start_swaps)
                S.swap_goals(goal_swaps)
                S.write_to_file(path_addon + "_" + str(aa) + "a_" + str(goal_swaps) + "gs_" + str(start_swaps) + "ss_" + str(ii), path)
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

# Experiment 1: Performance test

# # Experiment 1a: Performance on Shuffleboard, no matching
# main(list(cp['ARRIVAL SHUFFLEBOARD'].values())) # few instances, easy to solve
# main(list(cp['DEPARTURE SHUFFLEBOARD'].values())) # few instances, easy to solve
# main(list(cp['ARRIVAL HARD SHUFFLEBOARD'].values())) # (50 % random start swaps)
# main(list(cp['DEPARTURE HARD SHUFFLEBOARD'].values())) # (50 % random goal swaps)

# # Experiment 1b: Performance on Carrousel, no matching
# main(list(cp['ARRIVAL HARD CARROUSEL'].values())) # (50 % random start swaps)
# main(list(cp['DEPARTURE HARD CARROUSEL'].values())) # (50 % random goal swaps)

# # Experiment 1c: Performance on shuffleboard / carrousel with 1 , 3 , 5 teams
# main(list(cp['ARRIVAL HARD SHUFFLEBOARD 1 TEAM'].values())) # (50 % random start swaps)
# main(list(cp['ARRIVAL HARD SHUFFLEBOARD 3 TEAMS'].values())) # (50 % random start swaps)
# main(list(cp['ARRIVAL HARD SHUFFLEBOARD 5 TEAMS'].values())) # (50 % random start swaps)

# main(list(cp['ARRIVAL HARD CARROUSEL 1 TEAM'].values())) # (50 % random start swaps)
# main(list(cp['ARRIVAL HARD CARROUSEL 3 TEAMS'].values())) # (50 % random start swaps)
# main(list(cp['ARRIVAL HARD CARROUSEL 5 TEAMS'].values())) # (50 % random start swaps)



# # Experiment 2: reversals
# main(list(cp['REVERSAL'].values()))

# # Experiment 3: GRID vs SHUFFLEBOARD vs CARROUSEL
main(list(cp['RANDOM SHUFFLEBOARD 25'].values()))
main(list(cp['RANDOM GRID 25'].values()))
main(list(cp['RANDOM CARROUSEL 25'].values()))

main(list(cp['RANDOM SHUFFLEBOARD 36'].values()))
main(list(cp['RANDOM GRID 36'].values()))
main(list(cp['RANDOM CARROUSEL 36'].values()))

main(list(cp['RANDOM SHUFFLEBOARD 49'].values()))
main(list(cp['RANDOM GRID 49'].values()))
main(list(cp['RANDOM CARROUSEL 49'].values()))


