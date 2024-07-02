#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author       : Edgar Carrillo
# Created      : 2022-02-02
# Last Modified: 2024-07-01
# Affiliation  : Fisk University, Vanderbilt University

'''
problem_2_plots, originally designed as courswork for a 
magmas and eruptions graduate course
harker diagram which compares multiple data
'''

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def load_data(sheet_name):
    """Load data from the specified sheet in the Excel file."""
    return pd.read_excel('lit_data.xlsx', sheet_name=sheet_name)

def extract_columns(df):
    """Extract relevant columns from the dataframe, handling missing columns."""
    columns = ['SiO2', 'TiO2', 'Al2O3', 'FeO', 'MgO', 'MnO', 'CaO', 'Na2O', 'K2O']
    extracted = {col: df[col] for col in columns}
    if 'FeO/MgO' in df.columns:
        extracted['FeO/MgO'] = df['FeO/MgO']
    else:
        extracted['FeO/MgO'] = pd.Series([np.nan] * len(df), index=df.index)
    return extracted

# Load data from all sheets
sheets = ['Sheet0', 'Sheet1', 'Sheet2', 'Sheet3', 'Sheet4', 'Sheet5']
data_frames = {sheet: extract_columns(load_data(sheet)) for sheet in sheets}

# Plot settings
labels = ['hat', 'seg', 'thing', 'new(TNC)', 'new(CA)', 'aug']
colors = ['b', 'g', 'r', 'c', 'm', 'y']
elements = ['TiO2', 'Al2O3', 'MnO', 'MgO', 'FeO', 'CaO', 'FeO/MgO', 'Na2O', 'K2O']

figure, axis = plt.subplots(4, 2, figsize=(10, 10))

# Plot data
for idx, (ax, element) in enumerate(zip(axis.flatten(), elements)):
    for label, color, (sheet, df) in zip(labels, colors, data_frames.items()):
        if not df[element].isnull().all():
            ax.scatter(df['SiO2'], df[element], label=label if idx == 0 else "", color=color, alpha=0.5)
            ax.set_ylabel(f"{element} %")
    if idx >= len(elements) - 2:
        ax.set_xlabel("SiO2 %")
    ax.grid()

# Add legend to the first subplot only
axis[0, 0].legend(loc='upper right')

plt.suptitle("Liquid lines of descent", fontsize=15)
figure.tight_layout()
plt.show()
