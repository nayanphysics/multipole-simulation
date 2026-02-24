import numpy as np
import matplotlib.pyplot as plt

# Define the multipole configurations
# Each is a dict with 'label', 'positions', 'charges'
multipoles = [

    {
        'label': 'Dipole (2 charges)',
        'positions': [-0.5, 0.5],
        'charges': [1.0, -1.0],
        'k':[2,2,2,2]
    },
    {
        'label': 'Tripole (3 charges)',
        'positions': [-0.5, 0.0, 0.5],
        'charges': [1.0, -2.0, 1.0],
        'k':[3,3,3,3]
    },
    {
        'label': 'Quadrupole (4 charges)',
        'positions': [-0.5, -0.5/3, 0.5/3, 0.5],
        'charges': [1.0, -3.0, 3.0, -1.0],
        'k':[4,4,4,4]
    },
    {
        'label': 'Pentapole (5 charges)',
        'positions': [-0.5, -0.25, 0.0, 0.25, 0.5],
        'charges': [1.0, -4.0, 6.0, -4.0, 1.0],
        'k':[5,5,5,5]
    }
]

# Define r values (large compared to separation ~1)
r_values = np.linspace(0.1, 20.0, 20000)

# Function to compute potential V at r (along z-axis, r > 0)
def compute_V(r, positions, charges,k):
    V = 0.0
    for pos, q,kv in zip(positions, charges,k):
        dist = np.abs(r - pos)
        V += q /(dist **kv)
    return V

# Function to compute electric field E_z at r
def compute_E(r, positions, charges,k):
    E = 0.0
    for pos, q, kv in zip(positions, charges,k):
        dist = r - pos
        abs_dist = np.abs(dist)
        E += q * dist / (abs_dist **(kv+1))
    return E

# Prepare plots
fig_V, ax_V = plt.subplots()
fig_E, ax_E = plt.subplots()

for multipole in multipoles:
    label = multipole['label']
    positions = multipole['positions']
    charges = multipole['charges']
    k= multipole['k']
    
    V = np.array([compute_V(r, positions, charges,k) for r in r_values])
    E = np.array([compute_E(r, positions, charges,k) for r in r_values])
    
    # Plot abs(V) and abs(E) on log-log scale to show dependence
    ax_V.loglog(r_values, np.abs(V), label=label)
    ax_E.loglog(r_values, np.abs(E), label=label)

# Set up potential plot
ax_V.set_xlabel('r (distance)')
ax_V.set_ylabel('|V| (potential)')
ax_V.set_title('Dependence of Electric Potential on r for Multipoles')
ax_V.legend()
ax_V.grid(True, which="both", ls="--")

# Set up field plot
ax_E.set_xlabel('r (distance)')
ax_E.set_ylabel('|E| (electric field)')
ax_E.set_title('Dependence of Electric Field on r for Multipoles')
ax_E.legend()
ax_E.grid(True, which="both", ls="--")

plt.show()