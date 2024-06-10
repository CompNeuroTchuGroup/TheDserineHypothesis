import pickle
import multiprocessing
import sys

import numpy as np

sys.path.append('../model/')
from model import RBCM, compute_p_change

########## Parameters ##########

# Possible states
states = {'S1': np.array([1, 0]), 'S2': np.array([0, 1])}

# Valence signals
R_negative = -1.
R_positive = 1.5 
Rs = {'phase_1': {'R1': R_positive, 'R2': R_negative}, 'phase_2': {'R1': R_negative, 'R2': R_positive}}


# Number of steps
number_of_mice = 100
steps = {'phase_1': 10000, 'phase_2': 30000}

# Initial values
initial_weights = (0.2, 0.2)  
initial_state = 'S1'
initial_threshold = 0.018

# Simulation function
def change_state(current_state):

    if np.array_equal(current_state, states['S1']):
        return states['S2'].copy()
    else:
        return states['S1'].copy()

def get_valence_signal(current_state, R1, R2):
    
    if np.array_equal(current_state, states['S1']):
        return R1
    else:
        return R2

def simulate_single_mouse(mouse_id, mouse_type):

    print("Simulating mouse n. " + str(mouse_id) + "/ (" + mouse_type + ")...")

    rng = np.random.default_rng(seed=mouse_id)

    data = {'phase_1': {'states': [], 'rates': [], 'thetas': [], 'weights': []},
            'phase_2': {'states': [], 'rates': [], 'thetas': [], 'weights': []}}
    block_threshold = False if mouse_type == 'sham' else True

    x = states[initial_state].copy()
    w = np.array(initial_weights)

    mouse = RBCM(block_threshold=block_threshold, theta0=initial_threshold)

    for phase in ['phase_1', 'phase_2']:

        for _ in range(steps[phase]):

            x_old = x.copy()
            y = np.dot(w, x)

            p_change = compute_p_change(y)

            if rng.random() < p_change:
                x = change_state(x)

            R = get_valence_signal(x, Rs[phase]['R1'], Rs[phase]['R2'])
            w += mouse.get_weights_update(x_old, y, R)

            data[phase]['states'].append(x.copy())
            data[phase]['rates'].append(y)
            data[phase]['thetas'].append(mouse.theta)
            data[phase]['weights'].append(w.copy())

    
    return data

pool = multiprocessing.Pool()

mice = [(i, 'sham') for i in range(number_of_mice)] + [(number_of_mice+i, 'mutant') for i in range(number_of_mice)]
results = pool.starmap(simulate_single_mouse, mice)

with open('data.pickle', 'wb') as file:
    pickle.dump({'sham': results[0:number_of_mice], 'mutant': results[number_of_mice:]}, file)
