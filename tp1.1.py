import numpy as np
import matplotlib.pyplot as plt

#TP 1.1 Simulación de Una Ruleta
#Datos

def frecuenciaR(nro, valores):
    frecuenciaA = 0
    for n in valores:
        if n == nro:
            frecuenciaA+= 1
    freqRel= frecuenciaA/len(valores)
    return freqRel

frecuencia= 1/37
esperanza= np.arange(0, 37).mean()
desvio= np.arange(0, 37).std()
varianza= np.arange(0, 37).var()

t = 500 #número de tiradas
c = 10 #número de corridas
nroEvaluar = 12

frecuencias= [[0 for x in range(t)] for y in range(c)]
medias= [[0 for x in range(t)] for y in range(c)]
desvios= [[0 for x in range(t)] for y in range(c)]
varianzas= [[0 for x in range(t)] for y in range(c)]



for i in range(0, c):
    numeros= np.random.randint(0, 37, t)
    print(numeros)
    for n in range(0, t):
        lista= numeros[:n+1]
        frecuencias[i][n]= frecuenciaR(nroEvaluar, lista)
        medias[i][n]= lista.mean()
        desvios[i][n]= lista.std()
        varianzas[i][n]= lista.var()


# Grafico de las corridas
fig, axs = plt.subplots(ncols=2, nrows=2, constrained_layout=True, figsize=[8, 6])

axs[0, 0].set_title('Frecuencia Relativa (fr)')
axs[0, 0].set(xlabel='Tiradas', ylabel='Frecuencia Relativa (fr)')
axs[0, 0].set_ylim(bottom=0, top=max(np.amax(frecuencias), frecuencia)+0.05)
for i in range(0, c):
    axs[0, 0].plot(range(1, t+1), frecuencias[i], label=str(i+1)+' corridas')
axs[0, 0].axhline(y=frecuencia, color='b', linestyle='-', label='fre')

plt.show()