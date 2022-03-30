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
'include_inverted_scen' : False
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
'include_inverted_scen' : False
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
'include_inverted_scen' : False
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
'include_inverted_scen' : False
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
'include_inverted_scen' : False
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
'include_inverted_scen' : True
}





with open("settings.ini", 'w') as f:
    cp.write(f)