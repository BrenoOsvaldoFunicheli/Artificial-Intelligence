from array import numpy as np
import skfuzzy as fuzz

t_dest = np.arange(0, 100, 1)  # espaço de discurso de cada valor
u_dest = np.arange(0, 50, 1)
pm_water = np.arange(0, 50, 1)
i_dest = np.arange(0, 100, 1)

# Conjuntos fuzzy
tdest_lo = fuzz.trimf(t_dest, [0, 0, 75])
tdest_hi = fuzz.trimf(t_dest, [25, 100, 100])

udest_lo = fuzz.trimf(u_dest, [0, 0, 100])
udest_hi = fuzz.trimf(u_dest, [0, 100, 100])

pm_water_near = fuzz.trapmf(u_dest, [0, 0, 10, 40])
pm_water_far = fuzz.trapmf(u_dest, [10, 40, 50, 50])

idest_lo = fuzz.trimf(u_dest, [0, 10, 20])
idest_hi = fuzz.trimf(u_dest, [20, 100, 100])


# qt_medicine = np.arange(0, 100, 1)

# q_med_low = fuzz.trimf(qt_medicine, [0, 0, 50])
# q_med_md = fuzz.trimf(qt_medicine, [0, 40, 10])
# q_med_hi = fuzz.trimf(qt_medicine, [40, 100, 10])

# regras fuzzy
#
#
tmp_level_lo = fuzz.interp_membership(t_dest, tdest_lo, 80)
tmp_level_hi = fuzz.interp_membership(t_dest, tdest_hi, 80)
#
# udest_level_lo = fuzz.interp_membership(u_dest, udest_lo, 10)
# udest_level_hi = fuzz.interp_membership(u_dest, udest_hi, 10)
#
# pm_water_level_near = fuzz.interp_membership(pm_water, pm_water_near, 15)
# pm_water_level_far = fuzz.interp_membership(pm_water, pm_water_far, 15)
#
# id_level_lo = fuzz.interp_membership(i_dest, idest_lo, 90)
# id_level_hi = fuzz.interp_membership(i_dest, idest_hi, 90)
#
# rule1 = np.fmin(tdest_hi, udest_hi, pm_water_near, idest_lo)
# rule2 = idest_hi
# rule3 = np.fmax(np.fmin(np.fmin(udest_hi, tdest_hi), idest_lo), pm_water_near)
# rule4 = np.fmax(tdest_lo, udest_lo)
#
# agregate = np.fmax(rule1, rule2, rule3, rule4)

# medicine =fuzz.defuzz(qt_medicine, agregate, 'centroid')

# print(medicine)
