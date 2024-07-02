# Magma Project 


This repository contains scripts and data for plotting chemical compositions of various lava samples. The scripts load data from Excel files, process it, and generate scatter plots to visualize the liquid lines of descent for different samples.



![Lava Flow](images/stock_volcano.jpg)



## Table of Contents

- [Installation](#installation)
- [Project Structure](#project-structure)
- [Sample Usage](#scripts)
- [Sample Data](#data)
- [License](#license)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/elcarrillo/magma-project.git
    cd magma-project
    ```

## Project Structure

```
magma-project/
│
├── README.md                                # Project documentation
├── vol_mol_conv.py                          # Volume to mole conversion script
├── p2_plots.py                              # Main script for plotting chemical compositions
├── hat_creek.py                             # Auxiliary script for plotting Hat Creek data
├── lit_data.xlsx                            # Excel file containing compiled data
├── EES4891-Spr2022-M&E-Problem2-Literature_data.xlsx  # Compiled data from various sources
├── EES4891-Spr2022-M&E-Problem2-Hat_Creek.xlsx        # Compiled data for Hat Creek
├── EES4891-Spr2022-M&E-Problem2-problem1.xlsx         # Equations and parameters
├── crystal_dynamics_in_melts.pdf            # Crystal dynamics in melts report
├── p_v.py                                   # Script for pressure vs volume calculations
└── sample_plots/                            # Directory containing sample plots
    ├── sample1.png                            # Example plot 1
    ├── sample2.png                            # Example plot 2
    └── sample3.png                            # Example plot 3

```

## Sample Usage 


To generate the plots, simply run the `p2_plots.py` script:
```bash
python p2_plots.py
```

Make sure the `lit_data.xlsx` file is in the same directory as the script or update the file path accordingly.

### p2_plots.py

This script performs the following steps:
1. Loads data from multiple sheets in an Excel file.
2. Extracts relevant chemical composition data for each sample.
3. Generates scatter plots to visualize the liquid lines of descent.

#### Functions:

- `load_data(sheet_name)`: Loads data from the specified sheet in the Excel file.
- `extract_columns(df)`: Extracts relevant columns from the dataframe, handling missing columns.

#### Usage:

```python
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
```

## Sample Data

### lit_data.xlsx

This Excel file contains the chemical composition data for different lava samples. Each sheet in the file corresponds to a different sample set:
- `Sheet0`: Hat Creek data
- `Sheet1`: Seguam data
- `Sheet2`: Thing data
- `Sheet3`: New (TNC) data
- `Sheet4`: New (CA) data
- `Sheet5`: Aug data

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
