import matplotlib.pyplot as plt
import statistics as stats
import scipy.stats as stats


# Datos
So = [6,7,8,9,10]
Si = [-25,-17.5,-13.2,-11,-10]



# Figura 1
plt.figure(1)
plt.plot(So, Si, 'ok', markersize=10, linewidth=2, color=[1, 0, 0])
plt.xlabel('So (cm)')
plt.ylabel('Si (cm)')
plt.xlim([25, 80])

# Cálculo de la pendiente y la desviación estándar
m, b, r_value, p_value, std_err = stats.linregress(So, Si)

# Adición de la pendiente y la desviación estándar al gráfico
plt.text(8, -25, 'Pendiente: {:.2f}'.format(m), fontsize=10)
plt.text(8, -23, 'Desviación estándar: {:.2f}'.format(std_err), fontsize=10)

plt.plot([min(So), max(So)], [m * min(So) + b, m * max(So) + b], 'k', linewidth=2)
plt.plot([min(So), max(So)], [m * min(So) + b + std_err, m * max(So) + b + std_err], 'k', linewidth=1)
plt.plot([min(So), max(So)], [m * min(So) + b - std_err, m * max(So) + b - std_err], 'k', linewidth=1)

# Figura 2
plt.figure(2)
inv_So = []
inv_Si = []
for i in range(len(So)):
    inv_So.append(1.0 / So[i])
    inv_Si.append(1.0 / Si[i])

plt.plot(inv_So, inv_Si, 'ok', markersize=10, linewidth=2, color=[1, 0, 0])
plt.xlabel('1/So (cm^-1)')
plt.ylabel('1/Si (cm^-1)')
plt.xlim([0.02, 0.04])

# Cálculo de la pendiente y la desviación estándar
m, b, r_value, p_value, std_err = stats.linregress(inv_So, inv_Si)

# Adición de la pendiente y la desviación estándar al gráfico
plt.text(0.14, -0.15, 'Pendiente: {:.2f}'.format(m), fontsize=10)
plt.text(0.14, -0.12, 'Desviación estándar: {:.2f}'.format(std_err), fontsize=10)

plt.plot([min(inv_So), max(inv_So)], [m * min(inv_So) + b, m * max(inv_So) + b], 'k', linewidth=2)
plt.plot([min(inv_So), max(inv_So)], [m * min(inv_So) + b + std_err, m * max(inv_So) + b + std_err], 'k', linewidth=1)
plt.plot([min(inv_So), max(inv_So)], [m * min(inv_So) + b - std_err, m * max(inv_So) + b - std_err], 'k', linewidth=1)


# Figura 3
plt.figure(3)
aumento = []
for i in range(len(So)):
    aumento.append(Si[i] / So[i])

plt.plot(So, aumento, 'ok', markersize=10, linewidth=2, color=[1, 0, 0])
plt.xlabel('So (cm)')
plt.ylabel('Aumento')
plt.xlim([25, 80])


# Cálculo de la pendiente y la desviación estándar
m, b, r_value, p_value, std_err = stats.linregress(So, aumento)

# Adición de la pendiente y la desviación estándar al gráfico
plt.text(8, -3.7, 'Pendiente: {:.2f}'.format(m), fontsize=10)
plt.text(8, -3.5, 'Desviación estándar: {:.2f}'.format(std_err), fontsize=10)

plt.plot([min(So), max(So)], [m * min(So) + b, m * max(So) + b], 'k', linewidth=2)
plt.plot([min(So), max(So)], [m * min(So) + b + std_err, m * max(So) + b + std_err], 'k', linewidth=1)
plt.plot([min(So), max(So)], [m * min(So) + b - std_err, m * max(So) + b - std_err], 'k', linewidth=1)


plt.show()