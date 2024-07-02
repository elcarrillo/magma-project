#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author       : Edgar Carrillo
# Created      : 2022-02-02
# Last Modified: 2024-07-01
# Affiliation  : Fisk University, Vanderbilt University

"""
Harker diagram for the Hat Creek data.

Data was compiled from work done by Brad Pitcher.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

## load data 
df_hat = pd.read_excel('lit_data.xlsx', sheet_name='Sheet0')

## extract columns
columns = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MgO', 'MnO', 'CaO', 'Na2O', 'K2O', 'P2O5']
x0 = df_hat['SiO2']
y_labels = ['TiO2 %', 'Al2O3 %', 'MnO %', 'MgO %', 'FeO %', 'CaO %', 'K2O %', 'Na2O %']

## create subplots
figure, axis = plt.subplots(4, 2, figsize=(5, 8))

# plot 
for i, ax in enumerate(axis.flatten()):
    ax.scatter(x0, df_hat[columns[i+1]])
    ax.set_ylabel(y_labels[i])
    if i >= 6:  # last row
        ax.set_xlabel("SiO2 %")

plt.tight_layout()
plt.show()
