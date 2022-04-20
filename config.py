import configparser

cp = configparser.ConfigParser()
cp['DEFAULT'] = {
'nodes' : 30,
'branches' : 5,
'gate_length' : 10,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 10,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swap_fraction' : 0,
'start_swap_fraction' : 0
}

cp['RANDOM'] = {
'nodes' : 30,
'branches' : 5,
'gate_length' : 10,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 10,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swap_fraction' : 0,
'start_swap_fraction' : 0
}

cp['REVERSAL'] = {
'nodes' : 30,
'branches' : 5,
'gate_length' : 10,
'randomness_parameter' : 0,
'min_agents' : 2,
'max_agents' : 10,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'reversal', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swap_fraction' : 0,
'start_swap_fraction' : 0
}

cp['ARRIVAL'] = {
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swap_fraction' : 0,
'start_swap_fraction' : 0
}

cp['DEPARTURE'] = {
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'departure', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swap_fraction' : 0,
'start_swap_fraction' : 0
}

cp['INVERSE'] = {
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'random', # options : random, reversal, arrival, departure
'include_inverted_scen' : True,
'goal_swap_fraction' : 0,
'start_swap_fraction' : 0
}

cp['HARD ARRIVAL'] = {
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'arrival', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swap_fraction' : 0,
'start_swap_fraction' : 0.5
}

cp['HARD DEPARTURE'] = {
'nodes' : 50,
'branches' : 8,
'gate_length' : 15,
'randomness_parameter' : 0.5,
'min_agents' : 2,
'max_agents' : 15,
'num_of_instances_per_num_agents' : 10,
'instance_type' : 'departure', # options : random, reversal, arrival, departure
'include_inverted_scen' : False,
'goal_swap_fraction' : 0.5,
'start_swap_fraction' : 0
}


with open("settings.ini", 'w') as f:
    cp.write(f)