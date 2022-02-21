#vol_mol_conv
import math 
print("use 5.5  for rhyolite at 200 Mpa")
m_i    = float(input('enter wt% of water: '))           ## wt% of h20
m_j    = [5.5,73.49,.18,13.55,0.36,.976,.5,1.43,3.36]   ## wt% of individual compunds in misture
M_j    = [18, 46, 113, 74,100,42,28,36,38]              ## molar mass of each compund in g/cm^3
rho_i  = [.40,2.65,4.23,3.95,5.24,5.74,3.58,3.34,2.27] ## density of each compund
#density of water is for when its bubble form at 200MPa

mixture =['h20', 'sio2','tio2','al2o3','fe2o3','feo','mgo','cao','na2o']
 
# volume % calc
### get v total first then use to get individual vol%

v_i = []
for i in range(len(rho_i)):
	val = m_j[i]/rho_i[i]
	v_i.append(val)

v_total = sum(v_i)
vol_perc = (m_i/v_total)*100
print("vol% = ", vol_perc)

#molar fraction = wt%/molar mass/ (sum m_j/M_j)

frac_val = []
for i in range(len(m_j)):
	val = m_j[i]/M_j[i]
	frac_val.append(val)


mol_fract_water = (m_i/M_j[0])/sum(frac_val)

print("mol% = ", mol_fract_water*100)

