## pressure vs volume

import math
import numpy as np
import matplotlib.pyplot as plt


### parameters
R_gas  = 8.31445    ## ideal gas constant m^3*Pa*k
T_rhy  = 1000       ## rhyolite temperature, K
m_a    = 100        ## assumption for mass 
p_init = 200000000  ## init pressures in pascals
p_lim  = 100000     ## atmospheric pressure
p_half = p_init/2
p_10   = p_init/10
at_wt  = 18         ## atomic weight of H20, grams 
n_val  = m_a/at_wt

#volume as a function of pressure using ideal gas law
def ideal_gas(p):
	vol =  (n_val*R_gas*T_rhy)/p  
	return vol

# create list of pressure values from 2e8 pa to 1e5 pa(1 atm)
p_max      = 100
p_mag_atm  = list(np.linspace(p_lim, p_init, p_max))
p_mag_half = list(np.linspace(p_half, p_init, p_max))
p_mag_10   = list(np.linspace(p_10, p_init, p_max))
#biggest range
vol_change_atm = []
for i in p_mag_atm:
	v_val = ideal_gas(i)
	vol_change_atm.append(v_val)
#pressure reduced by half, 100MPa
vol_change_half = []
for i in p_mag_half:
	v_val = ideal_gas(i)
	vol_change_half.append(v_val)
#pressure reduced 10 fold, 2e7
vol_change_10 = []
for i in p_mag_10:
	v_val = ideal_gas(i)
	vol_change_10.append(v_val)


#plot p vs v
fig, ax = plt.subplots(1,3)

ax[0].scatter(vol_change_atm, p_mag_atm)
ax[0].set_xlabel("volume(m^3)")
ax[0].set_ylabel("pressure(Pa)")
ax[1].scatter(vol_change_half, p_mag_half)
ax[1].set_xlabel("volume(m^3)")
ax[1].set_ylabel("pressure(Pa)")
ax[2].scatter(vol_change_10, p_mag_10)
ax[2].set_xlabel("volume(m^3)")
ax[2].set_ylabel("pressure(Pa)")


plt.suptitle("Volume as a function of pressure", fontsize= 9)
fig.tight_layout()
fig.set_figwidth(10)
plt.show()

#print(p_mag_var)
#print(vol_change)
