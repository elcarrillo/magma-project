
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

axis[0,0].scatter(x1, x2)
axis[0,0].set_xlabel("TiO2 %")
axis[0,0].set_ylabel("Al2O3 %")

axis[0,1].scatter(x2, x3)
axis[0,1].set_xlabel("Al2O3 %")
axis[0,1].set_ylabel("FeO2 %")

axis[1,0].scatter(x3, x4)
axis[1,0].set_xlabel("FeO2 %")
axis[1,0].set_ylabel("MgO %")

axis[1,1].scatter(x4, x5)
axis[1,1].set_xlabel("MgO %")
axis[1,1].set_ylabel("MnO %")

axis[2,0].scatter(x6, x7)
axis[2,0].set_xlabel("CaO %")
axis[2,0].set_ylabel("K2O %")

axis[2,1].scatter(x7, x8)
axis[2,1].set_xlabel("Na2O %")
axis[2,1].set_ylabel("K2O%")

axis[3,0].scatter(x9, x5)
axis[3,0].set_xlabel("P2O5 %")
axis[3,0].set_ylabel("MnO %")

axis[3,1].scatter(x1, x3)
axis[3,1].set_ylabel("FeO2 %")
axis[3,1].set_xlabel("TiO2 %")

plt.suptitle("liquid lines of descent for Hat Creek data", fontsize= 9)
figure.tight_layout()
plt.show()


