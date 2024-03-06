import numpy as np
import pickle
import matplotlib.pyplot as plt

# Get data to plot
with open('data.pickle', 'rb') as file:
    data = pickle.load(file)

number_of_mice = len(data['sham']['phase_1'])
steps_phase1 = len(data['sham']['phase_1'][0]['states'])
steps_phase2 = len(data['sham']['phase_2'][0]['states'])

## Plots of PHASE 1
fig, ax = plt.subplots(figsize=(5,4))

window = 300

all_visits_x1_sham = []
all_visits_x1_aCB1KO = []

for agent_id in range(number_of_mice):

    one_hot_vec_x1_sham = np.array([x[0] for x in data['sham']['phase_1'][agent_id]['states']])
    one_hot_vec_x1_aCB1KO = np.array([x[0] for x in data['aCB1KO']['phase_1'][agent_id]['states']])

    visits_x1_sham = []
    visits_x1_aCB1KO = []

    for i in range(steps_phase1-window):
        visits_x1_sham.append(one_hot_vec_x1_sham[i:i+window].mean())
        visits_x1_aCB1KO.append(one_hot_vec_x1_aCB1KO[i:i+window].mean())
    
    all_visits_x1_sham.append(visits_x1_sham)
    all_visits_x1_aCB1KO.append(visits_x1_aCB1KO)

average_visits_x1_sham = np.mean(all_visits_x1_sham, axis=0)
average_visits_x1_aCB1KO = np.mean(all_visits_x1_aCB1KO, axis=0)
    
ax.plot(average_visits_x1_sham, label='sham')
ax.plot(average_visits_x1_aCB1KO, label='aCB1KO')

ax.set_title("Relative Number of Visits to $x_1$ in the last 300 steps")
ax.set_xlabel('step')
ax.set_ylabel('$n_1$/300')
ax.legend()

fig.savefig('phase_1_visits.pdf')

## Plots of PHASE 2
fig, ax = plt.subplots(figsize=(5,4))

window = 300

all_visits_x1_sham = []
all_visits_x1_aCB1KO = []

for agent_id in range(number_of_mice):

    one_hot_vec_x1_sham = np.array([x[0] for x in data['sham']['phase_2'][agent_id]['states']])
    one_hot_vec_x1_aCB1KO = np.array([x[0] for x in data['aCB1KO']['phase_2'][agent_id]['states']])

    visits_x1_sham = []
    visits_x1_aCB1KO = []

    for i in range(steps_phase2-window):
        visits_x1_sham.append(one_hot_vec_x1_sham[i:i+window].mean())
        visits_x1_aCB1KO.append(one_hot_vec_x1_aCB1KO[i:i+window].mean())
    
    all_visits_x1_sham.append(visits_x1_sham)
    all_visits_x1_aCB1KO.append(visits_x1_aCB1KO)

average_visits_x1_sham = np.mean(all_visits_x1_sham, axis=0)
average_visits_x1_aCB1KO = np.mean(all_visits_x1_aCB1KO, axis=0)
    
ax.plot(average_visits_x1_sham, label='sham')
ax.plot(average_visits_x1_aCB1KO, label='aCB1KO')

ax.set_title("Relative Number of Visits to $x_1$ in the last 300 steps")
ax.set_xlabel('step')
ax.set_ylabel('$n_1$/300')
ax.legend()

fig.savefig('phase_2_visits.pdf')


# Weights plot - PHASE 1
fig, ax = plt.subplots(1,2, figsize=(10,4))

all_weights_sham = []
all_weights_aCB1KO = []

for agent_id in range(number_of_mice):

    all_weights_sham.append(data['sham']['phase_1'][agent_id]['weights'])
    all_weights_aCB1KO.append(data['aCB1KO']['phase_1'][agent_id]['weights'])

average_weights_sham =   np.mean(all_weights_sham, axis=0)
average_weights_aCB1KO = np.mean(all_weights_aCB1KO, axis=0)

ax[0].plot([w[0] for w in average_weights_sham] , label='$w_1$', color='#ff7f0e', linestyle='--')
ax[0].plot([w[1] for w in average_weights_sham] , label='$w_2$', color='#ff7f0e')

ax[1].plot([w[0] for w in average_weights_aCB1KO] , label='$w_1$', c='#1f77b4', linestyle='--')
ax[1].plot([w[1] for w in average_weights_aCB1KO] , label='$w_2$', c='#1f77b4')

ax[0].set_title('Sham mouse')
ax[1].set_title('aCBK1O mouse')
ax[0].set_xlabel('step')
ax[1].set_xlabel('step')
ax[0].set_ylabel('Weight value')
ax[1].set_ylabel('Weight value')

ax[0].legend()
ax[1].legend()

fig.savefig('phase_1_weights.pdf')


##### Weights plot -- PHASE 2
fig, ax = plt.subplots(1,2, figsize=(10,4))

all_weights_sham = []
all_weights_aCB1KO = []

for agent_id in range(number_of_mice):

    all_weights_sham.append(data['sham']['phase_2'][agent_id]['weights'])
    all_weights_aCB1KO.append(data['aCB1KO']['phase_2'][agent_id]['weights'])

average_weights_sham =   np.mean(all_weights_sham, axis=0)
average_weights_aCB1KO = np.mean(all_weights_aCB1KO, axis=0)

ax[0].plot([w[0] for w in average_weights_sham] , label='$w_1$', color='#ff7f0e', linestyle='--')
ax[0].plot([w[1] for w in average_weights_sham] , label='$w_2$', color='#ff7f0e')

ax[1].plot([w[0] for w in average_weights_aCB1KO] , label='$w_1$', c='#1f77b4', linestyle='--')
ax[1].plot([w[1] for w in average_weights_aCB1KO] , label='$w_2$', c='#1f77b4')

ax[0].set_title('Sham mouse')
ax[1].set_title('aCBK1O mouse')
ax[0].set_xlabel('step')
ax[1].set_xlabel('step')
ax[0].set_ylabel('Weight value')
ax[1].set_ylabel('Weight value')

ax[0].legend()
ax[1].legend()

fig.savefig('phase_2_weights.pdf')


## Zoomed Plot
fig, ax = plt.subplots(1,2, figsize=(10,4))

all_weights_sham = []
all_weights_aCB1KO = []

all_theta_sham = []
all_theta_aCB1KO = []

for agent_id in range(number_of_mice):

    all_weights_sham.append(data['sham']['phase_2'][agent_id]['weights'])
    all_theta_sham.append(data['sham']['phase_2'][agent_id]['thetas'])

    all_weights_aCB1KO.append(data['aCB1KO']['phase_2'][agent_id]['weights'])
    all_theta_aCB1KO.append(data['aCB1KO']['phase_2'][agent_id]['thetas'])

average_weights_sham =   np.mean(all_weights_sham, axis=0)
average_weights_aCB1KO = np.mean(all_weights_aCB1KO, axis=0)

average_theta_sham = np.mean(all_theta_sham, axis=0)
average_theta_aCB1KO = np.mean(all_theta_aCB1KO, axis=0)

ax[0].plot([w[0] for w in average_weights_sham] , label='$w_1$', color='#ff7f0e', linestyle='--')
ax[0].plot([w[1] for w in average_weights_sham] , label='$w_2$', color='#ff7f0e')

ax[1].plot([w[0] for w in average_weights_aCB1KO] , label='$w_1$', c='#1f77b4', linestyle='--')
ax[1].plot([w[1] for w in average_weights_aCB1KO] , label='$w_2$', c='#1f77b4')

ax[0].plot(average_theta_sham, color='red', label='threshold', alpha=0.7)
ax[1].plot(average_theta_aCB1KO, color='red', label='threshold', alpha=0.7)

ax[0].set_title('Sham mouse')
ax[1].set_title('aCBK1O mouse')
ax[0].set_xlabel('step')
ax[1].set_xlabel('step')
ax[0].set_ylabel('Weight value')
ax[1].set_ylabel('Weight value')

ax[0].legend()
ax[1].legend()

ax[0].set_ylim(-0.001, 0.1)
ax[1].set_ylim(-0.001, 0.1)

fig.savefig('phase_2_weightszoom.pdf')