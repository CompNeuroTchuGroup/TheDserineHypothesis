import numpy as np
from tqdm import tqdm
import pickle
from TheDserineHypothesis.model_and_scripts.model import *

# Possible states
x1, x2 = np.array([1., 0.]), np.array([0., 1.])

# Rs
Rm = -1.5
Rp = 1.

# Number of steps
number_of_mice = 10
steps_phase1 = 10000
steps_phase2 = 30000

# Data Storage
data = {'sham': {'phase_1': [], 'phase_2': []}, 'aCB1KO': {'phase_1': [], 'phase_2': []}}

# Sham Mice
for mouse_id in range(number_of_mice):

    sham_mouse = BCM(block_threshold=False)

    temp_dict = {'states': [], 'rates': [], 'thetas': [], 'weights': []}

    # phase 1
    R1 = Rm
    R2 = Rp

    x = x1.copy()
    w = np.array([0.2,0.2])

    for i in tqdm(range(steps_phase1)):

        x_old = x.copy()

        y = np.dot(w, x)

        p_change = compute_p_change(y)

        if np.random.rand()< p_change:
            
            x = change_state(x, x1, x2)
        
        R = get_valence_signal(x, x1, x2, R1, R2)
        w += sham_mouse.get_weights_update(x_old, y, R)

        temp_dict['states'].append(x.copy())
        temp_dict['rates' ].append(y.copy())
        temp_dict['thetas'].append(sham_mouse.theta)
        temp_dict['weights'].append(w.copy())

    data['sham']['phase_1'].append(temp_dict.copy())

    temp_dict = {'states': [], 'rates': [], 'thetas': [], 'weights': []}

    # Phase 2
    R1 = Rp
    R2 = Rm

    for i in tqdm(range(steps_phase2)):

        x_old = x.copy()

        y = np.dot(w, x)

        p_change = compute_p_change(y)

        if np.random.rand()< p_change:
            
            x = change_state(x, x1, x2)
        
        R = get_valence_signal(x, x1, x2, R1, R2)
        w += sham_mouse.get_weights_update(x_old, y, R)

        temp_dict['states'].append(x.copy())
        temp_dict['rates' ].append(y.copy())
        temp_dict['thetas'].append(sham_mouse.theta)
        temp_dict['weights'].append(w.copy())

    data['sham']['phase_2'].append(temp_dict.copy())


# aCB1KO Mice
for mouse_id in range(number_of_mice):

    aCB1KO_mouse = BCM(block_threshold=True, theta0 = 0.018)

    # phase 1
    temp_dict = {'states': [], 'rates': [], 'thetas': [], 'weights': []}

    R1 = Rm
    R2 = Rp

    x = x1.copy()
    w = np.array([0.2,0.2])

    for i in tqdm(range(steps_phase1)):

        x_old = x.copy()

        y = np.dot(w, x)

        p_change = compute_p_change(y)

        if np.random.rand()< p_change:
            
            x = change_state(x, x1, x2)
        
        R = get_valence_signal(x, x1, x2, R1, R2)
        w += aCB1KO_mouse.get_weights_update(x_old, y, R)

        temp_dict['states'].append(x.copy())
        temp_dict['rates' ].append(y.copy())
        temp_dict['thetas'].append(aCB1KO_mouse.theta)
        temp_dict['weights'].append(w.copy())
    
    data['aCB1KO']['phase_1'].append(temp_dict.copy())

    # Phase 2
    temp_dict = {'states': [], 'rates': [], 'thetas': [], 'weights': []}
                    
    R1 = Rp
    R2 = Rm
    
    for i in tqdm(range(steps_phase2)):

        x_old = x.copy()

        y = np.dot(w, x)

        p_change = compute_p_change(y)

        if np.random.rand()< p_change:
            
            x = change_state(x, x1, x2)
        
        R = get_valence_signal(x, x1, x2, R1, R2)
        w += aCB1KO_mouse.get_weights_update(x_old, y, R)

        temp_dict['states'].append(x.copy())
        temp_dict['rates' ].append(y.copy())
        temp_dict['thetas'].append(aCB1KO_mouse.theta)
        temp_dict['weights'].append(w.copy())

    data['aCB1KO']['phase_2'].append(temp_dict.copy())


with open('data.pickle', 'wb') as file:
    pickle.dump(data, file)
