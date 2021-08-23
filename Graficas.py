import numpy as np
import matplot.pyplot as plt
import math

#Constantes
N = 40
r = 30. #m
p_e = 2 #kg/m**3
p_s = 1 #kg/m**3
G = 0.00000000006674 #N*kg**2/m**2, Constante de gravitación universal

#Variación en z
z = np.array([1,1.2,1.4,1.6,20]) # m

#Función
def g(px,pz):
    return (4/3)*math.pi*G*(r**3)*(p_e-p_s)*pz*(1/((px**2)+(pz**2))**(3/2))

fig, ax = plt.subplots()

e = 2
# Valores del eje X que toma el gráfico.
x = np.linspace(-2.5,2.5,N)#m

# Valores del eje Y que toma el gráfico.
g1 = g(x,z[0])
g2 = g(x,z[1])
g3 = g(x,z[2])
g4 = g(x,z[3])
g5 = g(x,z[4])

# Graficar funcion.
ax.scatter(x,g1,label=f"z= {z[0]}")
ax.scatter(x,g2,label=f"z= {z[1]}")
ax.scatter(x,g3,label=f"z= {z[2]}")
ax.scatter(x,g4,label=f"z= {z[3]}")
ax.scatter(x,g5,label=f"z= {z[4]}")

# Nombrar los ejes
plt.xlabel('x')
plt.ylabel("$g(x)$")

#Ponerle nombre al grafico
plt.title("Modelamiento de anomalías gravimétricas")

# Limitar los valores de los ejes.
#plt.xlim(-7, 7)
#plt.ylim(-10, 10)

#Guardar gráfico como imágen PNG.
plt.savefig("output.png")

#Iniciar leyenda
ax.legend()

#Grilla
ax.grid(True)

#Graficarlo
plt.show()

#Guardar imagen
plt.savefig("Plot generated using Matplotlib.jpg")