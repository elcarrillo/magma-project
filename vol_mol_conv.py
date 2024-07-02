#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author       : Edgar Carrillo
# Created      : 2022-02-16
# Last Modified: 2024-07-01
# Affiliation  : Fisk University, Vanderbilt University

"""
Calculate the volume percentage and molar percentage of water in a mixture of rhyolite at 200 MPa.
"""

import math

# constants
mixture = ['H2O', 'SiO2', 'TiO2', 'Al2O3', 'Fe2O3', 'FeO', 'MgO', 'CaO', 'Na2O']
m_j = [5.5, 73.49, 0.18, 13.55, 0.36, 0.976, 0.5, 1.43, 3.36]  # wt% of individual compounds in mixture
M_j = [18, 46, 113, 74, 100, 42, 28, 36, 38]                   # molar mass of each compound in g/mol
rho_i = [0.40, 2.65, 4.23, 3.95, 5.24, 5.74, 3.58, 3.34, 2.27] # density of each compound in g/cm^3

# input
print("Use 5.5 for rhyolite at 200 MPa")
m_i = float(input('Enter wt% of water: '))  # wt% of H2O

# volume % Calculation
v_i = [m_j[i] / rho_i[i] for i in range(len(rho_i))]
v_total = sum(v_i)
vol_perc = (m_i / v_total) * 100
print(f"Volume % = {vol_perc:.2f}")

# molar Fraction Calculation
frac_val = [m_j[i] / M_j[i] for i in range(len(m_j))]
mol_fract_water = (m_i / M_j[0]) / sum(frac_val)
print(f"Molar % = {mol_fract_water * 100:.2f}")
