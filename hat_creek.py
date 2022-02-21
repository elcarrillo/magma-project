
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df_hat = pd.read_excel('lit_data.xlsx', sheet_name= 'Sheet0')

#hat creek data
x0 = df_hat.loc[:, 'SiO2']
x1 = df_hat.loc[:, 'TiO2']
x2 = df_hat.loc[:, 'Al2O3']
x3 = df_hat.loc[:, 'FeO']
x4 = df_hat.loc[:, 'MgO']
x5 = df_hat.loc[:, 'MnO']
x6 = df_hat.loc[:, 'CaO']
x7 = df_hat.loc[:, 'Na2O']
x8 = df_hat.loc[:, 'K2O']
x9 = df_hat.loc[:, 'P2O5']

figure, axis = plt.subplots(4,2,figsize = (5, 10))

axis[0,0].scatter(x0, x1)
axis[0,0].set_ylabel("TiO2 %")

axis[0,1].scatter(x0, x2)
axis[0,1].set_ylabel("Al2O3 %")

axis[1,0].scatter(x0, x5)
axis[1,0].set_ylabel("MgO %")

axis[1,1].scatter(x0, x4)
axis[1,1].set_ylabel("MnO %")

axis[2,0].scatter(x0, x3)
axis[2,0].set_ylabel("Fe02 %")

axis[2,1].scatter(x0, x6)
axis[2,1].set_ylabel("CaO %")

axis[3,0].scatter(x0, x8)
axis[3,0].set_ylabel("FeO2/MgO %")
axis[3,0].set_xlabel("SiO2 %")

axis[3,1].scatter(x0, x7)
axis[3,1].set_ylabel("K2O %")
axis[3,1].set_xlabel("SiO2 %")

plt.suptitle("liquid lines of descent for Hat Creek data", fontsize= 9)
figure.tight_layout()
plt.show()


