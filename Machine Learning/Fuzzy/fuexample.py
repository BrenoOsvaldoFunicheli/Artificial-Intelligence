import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

########################################################################
# DEFININDO VARIAVEIS LINGUÍSTICAS
########################################################################

x_qual = np.arange(0, 255, 1)
x_serv = np.arange(0, 100, 1)
x_tip = np.arange(0, 20, 1)

########################################################################
# DEFININDO CONJUNTOS NEBULOS PARA AS VARIÁVEIS LINGUISTCA
########################################################################

"""
Os valores colocados representam a notação em triangulo
Cabe ressaltar que não é necessário definir uma função de pertença, visto que 
a partir do triangulo formado a lib irá calcular uma função linear que encaixe os valores 
nítidos que serão inputados e os transformará em nebulosos
"""

# Definindo conjuntos nebulosos para variável linguistica qualidade
qual_lo = fuzz.trimf(x_qual, [0, 0, 5])
qual_md = fuzz.trimf(x_qual, [0, 5, 10])
qual_hi = fuzz.trimf(x_qual, [5, 10, 10])


# Definindo conjuntos nebulosos para variável linguistica serviço
serv_lo = fuzz.trimf(x_serv, [0, 0, 5])
serv_md = fuzz.trimf(x_serv, [0, 5, 10])
serv_hi = fuzz.trimf(x_serv, [5, 10, 10])

# Definindo conjuntos nebulosos para variável linguistica gorjeta
tip_lo = fuzz.trimf(x_tip, [0, 0, 13])
tip_md = fuzz.trimf(x_tip, [0, 13, 25])
tip_hi = fuzz.trimf(x_tip, [13, 25, 25])

########################################################################
# MAPEANDO VALORES CRISP PARA VALORES FUZZY
########################################################################
"""
Nesse momento é importante colocar o valor crisp para todos os conjuntos
pois em fuzzy um valor está incluido(pertence) a todos os conjuntos ao mesmo
tempo, porém em graus diferentes
"""
qual_level_lo = fuzz.interp_membership(x_qual, qual_lo, 6.5)
# e.g o valor 6.5 baseado na função triangular, pertence 0  ao conjunto qualidade baixo = 0/qual_baixa
qual_level_md = fuzz.interp_membership(x_qual, qual_md, 6.5)
qual_level_hi = fuzz.interp_membership(x_qual, qual_hi, 6.5)

#   O mesmo vale para o valor 9.8 para serviço
serv_level_lo = fuzz.interp_membership(x_serv, serv_lo, 9.8)
serv_level_md = fuzz.interp_membership(x_serv, serv_md, 9.8)
serv_level_hi = fuzz.interp_membership(x_serv, serv_hi, 9.8)

###############################################################
# DEFININDO REGRAS FUZZY
###############################################################

active_rule1 = np.fmax(qual_level_lo, serv_level_lo)
tip_activation_lo = np.fmin(active_rule1, tip_lo)  # removed entirely to 0

tip_activation_md = np.fmin(serv_level_md, tip_md)

active_rule3 = np.fmax(qual_level_hi, serv_level_hi)
tip_activation_hi = np.fmin(active_rule3, tip_hi)
tip0 = np.zeros_like(x_tip)

###############################################################
# DEFUZIFICAÇÃO
###############################################################

aggregated = np.fmax(tip_activation_lo,
                     np.fmax(tip_activation_md, tip_activation_hi))

tip = fuzz.defuzz(x_tip, aggregated, 'centroid')
tip_activation = fuzz.interp_membership(x_tip, aggregated, tip)  # for plot

print(tip, tip_activation)

fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_tip, tip_lo, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(x_tip, tip_md, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_tip, tip_hi, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_tip, tip0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([tip, tip], [0, tip_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()