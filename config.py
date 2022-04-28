import configparser

cp = configparser.ConfigParser()
cp['DEFAULT'] = {
'experiment number' : 3,
'nodes' : 30,
'branches' : 5,
'gate_length' : 10,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 10,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['RANDOM SHUFFLEBOARD 25'] = {
'experiment number' : 3,
'nodes' : 25,
'branches' : 5,
'gate_length' : 5,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 50,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['RANDOM CARROUSEL 25'] = {
'experiment number' : 3,
'nodes' : 25,
'branches' : 5,
'gate_length' : 5,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 50,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'carrousel', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['RANDOM GRID 25'] = {
'experiment number' : 3,
'nodes' : 25,
'branches' : 5,
'gate_length' : 5,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 50,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'grid', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['RANDOM SHUFFLEBOARD 36'] = {
'experiment number' : 3,
'nodes' : 36,
'branches' : 6,
'gate_length' : 6,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 50,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['RANDOM CARROUSEL 36'] = {
'experiment number' : 3,
'nodes' : 36,
'branches' : 6,
'gate_length' : 6,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 50,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'carrousel', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['RANDOM GRID 36'] = {
'experiment number' : 3,
'nodes' : 36,
'branches' : 6,
'gate_length' : 6,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 50,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'grid', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['RANDOM SHUFFLEBOARD 49'] = {
'experiment number' : 3,
'nodes' : 49,
'branches' : 7,
'gate_length' : 7,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 50,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['RANDOM CARROUSEL 49'] = {
'experiment number' : 3,
'nodes' : 49,
'branches' : 7,
'gate_length' : 7,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 50,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'carrousel', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['RANDOM GRID 49'] = {
'experiment number' : 3,
'nodes' : 49,
'branches' : 7,
'gate_length' : 7,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 50,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'grid', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['REVERSAL'] = {
'experiment number' : 2,
'nodes' : 11,
'branches' : 3,
'gate_length' : 5,
'randomness_parameter' : 0,
'min_agents' : 5,
'max_agents' : 5,
'num_of_instances_per_num_agents' : 1,
'instance_type' : 'reversal', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['ARRIVAL'] = {
'experiment number' : 3,
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['DEPARTURE'] = {
'experiment number' : 3,
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'departure', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['INVERSE'] = {
'experiment number' : 3,
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : True,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['HARD ARRIVAL'] = {
'experiment number' : 3,
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0.5,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['HARD DEPARTURE'] = {
'experiment number' : 3,
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'departure', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0.5,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['ARRIVAL SHUFFLEBOARD'] = {
'experiment number' : '1a',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['DEPARTURE SHUFFLEBOARD'] = {
'experiment number' : '1a',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'departure', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['ARRIVAL HARD SHUFFLEBOARD'] = {
'experiment number' : '1a',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : -1,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['DEPARTURE HARD SHUFFLEBOARD'] = {
'experiment number' : '1a',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'departure', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : -1,
'start_swaps' : 0,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['ARRIVAL HARD CARROUSEL'] = {
'experiment number' : '1b',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : -1,
'graph_type' : 'carrousel', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['DEPARTURE HARD CARROUSEL'] = {
'experiment number' : '1b',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'departure', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : -1,
'start_swaps' : 0,
'graph_type' : 'carrousel', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 0
}

cp['ARRIVAL HARD SHUFFLEBOARD 1 TEAM'] = {
'experiment number' : '1c',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : -1,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 1
}

cp['ARRIVAL HARD SHUFFLEBOARD 3 TEAMS'] = {
'experiment number' : '1c',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : -1,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 3
}

cp['ARRIVAL HARD SHUFFLEBOARD 5 TEAMS'] = {
'experiment number' : '1c',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : -1,
'graph_type' : 'shuffleboard', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 5
}

cp['ARRIVAL HARD CARROUSEL 1 TEAM'] = {
'experiment number' : '1c',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : -1,
'graph_type' : 'carrousel', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 1
}

cp['ARRIVAL HARD CARROUSEL 3 TEAMS'] = {
'experiment number' : '1c',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : -1,
'graph_type' : 'carrousel', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 3
}

cp['ARRIVAL HARD CARROUSEL 5 TEAMS'] = {
'experiment number' : '1c',
'nodes' : 50,
'branches' : 3,
'gate_length' : 20,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 20,
'num_of_instances_per_num_agents' : 20,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swaps' : 0,
'start_swaps' : -1,
'graph_type' : 'carrousel', #options : shuffleboard, carrousel, grid (not implemented)
'num_of_types' : 5
}



with open("settings.ini", 'w') as f:
    cp.write(f)