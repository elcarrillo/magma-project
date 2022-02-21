#problem_2_plots
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df_hat = pd.read_excel('lit_data.xlsx', sheet_name= 'Sheet0')
df_seg = pd.read_excel('lit_data.xlsx', sheet_name= 'Sheet1')
df_thi = pd.read_excel('lit_data.xlsx', sheet_name= 'Sheet2')
df_new1 = pd.read_excel('lit_data.xlsx', sheet_name= 'Sheet3')
df_new2 = pd.read_excel('lit_data.xlsx', sheet_name= 'Sheet4')
df_aug = pd.read_excel('lit_data.xlsx', sheet_name= 'Sheet5')


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
#ssequam data
y0 = df_seg.loc[:, 'SiO2']
y1 = df_seg.loc[:, 'TiO2']
y2 = df_seg.loc[:, 'Al2O3']
y3 = df_seg.loc[:, 'FeO']
y4 = df_seg.loc[:, 'MgO']
y5 = df_seg.loc[:, 'MnO']
y6 = df_seg.loc[:, 'CaO']
y7 = df_seg.loc[:, 'Na2O']
y8 = df_seg.loc[:, 'K2O']
y9 = df_seg.loc[:, 'FeO/MgO']

z0 = df_thi.loc[:, 'SiO2']
z1 = df_thi.loc[:, 'TiO2']
z2 = df_thi.loc[:, 'Al2O3']
z3 = df_thi.loc[:, 'FeO']
z4 = df_thi.loc[:, 'MgO']
z5 = df_thi.loc[:, 'MnO']
z6 = df_thi.loc[:, 'CaO']
z7 = df_thi.loc[:, 'Na2O']
z8 = df_thi.loc[:, 'K2O']
z9 = df_thi.loc[:, 'FeO/MgO']

a0 = df_new1.loc[:, 'SiO2']
a1 = df_new1.loc[:, 'TiO2']
a2 = df_new1.loc[:, 'Al2O3']
a3 = df_new1.loc[:, 'FeO']
a4 = df_new1.loc[:, 'MgO']
a5 = df_new1.loc[:, 'MnO']
a6 = df_new1.loc[:, 'CaO']
a7 = df_new1.loc[:, 'Na2O']
a8 = df_new1.loc[:, 'K2O']
a9 = df_new1.loc[:, 'FeO/MgO']

b0 = df_new2.loc[:, 'SiO2']
b1 = df_new2.loc[:, 'TiO2']
b2 = df_new2.loc[:, 'Al2O3']
b3 = df_new2.loc[:, 'FeO']
b4 = df_new2.loc[:, 'MgO']
b5 = df_new2.loc[:, 'MnO']
b6 = df_new2.loc[:, 'CaO']
b7 = df_new2.loc[:, 'Na2O']
b8 = df_new2.loc[:, 'K2O']
b9 = df_new2.loc[:, 'FeO/MgO']

c0 = df_aug.loc[:, 'SiO2']
c1 = df_aug.loc[:, 'TiO2']
c2 = df_aug.loc[:, 'Al2O3']
c3 = df_aug.loc[:, 'FeO']
c4 = df_aug.loc[:, 'MgO']
c5 = df_aug.loc[:, 'MnO']
c6 = df_aug.loc[:, 'CaO']
c7 = df_aug.loc[:, 'Na2O']
c8 = df_aug.loc[:, 'K2O']
c9 = df_aug.loc[:, 'FeO/MgO']

#plt.scatter(x, x4, alpha=0.5)
#plt.scatter(y, y4, alpha=0.5)
#plt.scatter(x, x3, alpha=0.5)
#plt.scatter(x, x4, alpha=0.5)
#plt.scatter(x, x5, alpha=0.5)
#plt.scatter(x, x6, alpha=0.5)
#plt.scatter(x, x7, alpha=0.5)
#plt.scatter(x, x8, alpha=0.5)
#plt.scatter(x, x9, alpha=0.5)
#plt.show()

figure, axis = plt.subplots(4,2,figsize = (10, 10))

axis[0,0].scatter(x0, x1, label = "hat")
axis[0,0].scatter(y0, y1, label = "seg")
axis[0,0].scatter(z0, z1, label = "thing")
axis[0,0].scatter(a0, a1, label = 'new(TNC)')
axis[0,0].scatter(b0, b1, label = 'new(CA)')
axis[0,0].scatter(c0, c1, label = 'aug')
axis[0,0].set_ylabel("TiO2 %")
axis[0,0].legend(loc = 'upper right')

axis[0,1].scatter(x0, x2)
axis[0,1].scatter(y0, y2)
axis[0,1].scatter(z0, z2)
axis[0,1].scatter(a0, a2)
axis[0,1].scatter(b0, b2)
axis[0,1].scatter(c0, c2)
axis[0,1].set_ylabel("Al2O3 %")

axis[1,0].scatter(x0, x5)
axis[1,0].scatter(y0, y5)
axis[1,0].scatter(z0, z5)
axis[1,0].scatter(a0, a5)
axis[1,0].scatter(b0, b5)
axis[1,0].scatter(c0, c5)
axis[1,0].set_ylabel("MgO %")

axis[1,1].scatter(x0, x4)
axis[1,1].scatter(y0, y4)
axis[1,1].scatter(z0, z4)
axis[1,1].scatter(a0, a4)
axis[1,1].scatter(b0, b4)
axis[1,1].scatter(c0, c4)
axis[1,1].set_ylabel("MnO %")

axis[2,0].scatter(x0, x3)
axis[2,0].scatter(y0, y3)
axis[2,0].scatter(z0, z3)
axis[2,0].scatter(a0, a3)
axis[2,0].scatter(b0, b3)
axis[2,0].scatter(c0, c3)
axis[2,0].set_ylabel("Fe02 %")

axis[2,1].scatter(x0, x6)
axis[2,1].scatter(y0, y6)
axis[2,1].scatter(z0, z6)
axis[2,1].scatter(a0, a6)
axis[2,1].scatter(b0, b6)
axis[2,1].scatter(c0, c6)
axis[2,1].set_ylabel("CaO %")

axis[3,0].scatter(x0, x8)
axis[3,0].scatter(y0, y8)
axis[3,0].scatter(z0, z8)
axis[3,0].scatter(a0, a8)
axis[3,0].scatter(b0, b8)
axis[3,0].scatter(c0, c8)
axis[3,0].set_ylabel("FeO2/MgO %")
axis[3,0].set_xlabel("SiO2 %")

axis[3,1].scatter(x0, x7)
axis[3,1].scatter(y0, y7)
axis[3,1].scatter(z0, z7)
axis[3,1].scatter(a0, a7)
axis[3,1].scatter(b0, b7)
axis[3,1].scatter(c0, c7)
axis[3,1].set_ylabel("K2O %")
axis[3,1].set_xlabel("SiO2 %")

plt.suptitle("liquid lines of descent", fontsize= 15)
figure.tight_layout()
plt.show()
