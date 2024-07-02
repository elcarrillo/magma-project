#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author       : Edgar Carrillo
# Created      : 2022-02-14
# Last Modified: 2024-07-01
# Affiliation  : Fisk University, Vanderbilt University

'''
Pressure vs Volume
'''

import numpy as np
import matplotlib.pyplot as plt

params = {
    'legend.title_fontsize': 'xx-small',
    'axes.labelsize': 16,
    'font.size': 16,
    'legend.fontsize': 8,
    'xtick.labelsize': 12,
    'ytick.labelsize': 12,
    'font.family': 'serif',
    'xtick.direction': 'in',
    'ytick.direction': 'in',
    'xtick.minor.visible': True,
    'ytick.minor.visible': True,
    'xtick.top': True,
    'ytick.right': True,
    'figure.autolayout': True
}
plt.rcParams.update(params)

# parameters
R_gas = 8.31445       # Ideal gas constant m^3*Pa*K
T_rhy = 1000          # Rhyolite temperature, K
m_a = 100             # Assumption for mass 
p_init = 200000000    # Initial pressure in pascals
p_lim = 100000        # Atmospheric pressure
p_factors = [1, 0.5, 0.1]  # Pressure reduction factors
at_wt = 18            # Atomic weight of H2O, grams 
n_val = m_a / at_wt

# volume as a function of pressure using the ideal gas law
def ideal_gas(p):
    return (n_val * R_gas * T_rhy) / p

## create list of pressure values for each factor
p_max = 100
pressure_ranges = [np.linspace(p_lim, p_init * factor, p_max) for factor in p_factors]

# Calculate volume changes for each pressure range
volume_changes = [[ideal_gas(p) for p in pressure_range] for pressure_range in pressure_ranges]

### plot p vs v
fig, ax = plt.subplots(figsize=[8, 6])

labels = ['Initial Pressure (200 MPa)', 'Half Initial Pressure (100 MPa)', 'One-Tenth Initial Pressure (20 MPa)']
colors = ['blue', 'green', 'red']

for i in range(3):
    ax.scatter(volume_changes[i], pressure_ranges[i], label=labels[i], color=colors[i])
    #ax.plot(volume_changes[i], pressure_ranges[i], color='black')

ax.set_xlabel(r"Volume [m$^3$]")
ax.set_ylabel("Pressure [Pa]")
ax.grid()
ax.legend()

fig.tight_layout()
plt.show()
