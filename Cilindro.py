import numpy as np
import matplotlib.pyplot as plt

#Constantes
N = 40
r = 30. #m
delta_p=np.array([1,-3])#kg/m**3
G = 0.00000000006674 #N*kg**2/m**2, Constante de gravitación universal

#Variación en z
z = np.array([1,1.2,1.4,20,1]) # m

#Función
def g1(px,pz,pd):
    return (4/3)*np.pi*G*(r**3)*(pd)*pz*(1/((px**2)+(pz**2))**(3/2))

# Valores del eje X que toma el gráfico.
x = np.linspace(-2.5,2.5,N) #m

# Valores del eje Y que toma el gráfico.
g11 = g1(x,z[0],delta_p[0])
g12 = g1(x,z[1],delta_p[0])
g13 = g1(x,z[2],delta_p[0])
g14 = g1(x,z[3],delta_p[0])
g15 = g1(x,z[4],delta_p[1])

# Graficar funcion.
plt.scatter(x,g11,label=f"z= {z[0]}, p_e > p_s")
plt.scatter(x,g12,label=f"z= {z[1]}, p_e > p_s")
plt.scatter(x,g13,label=f"z= {z[2]}, p_e > p_s")
plt.scatter(x,g14,label=f"z= {z[3]}, p_e > p_s")
plt.scatter(x,g15,label=f"z= {z[4]}, p_e < p_s")

# Nombrar los ejes
plt.xlabel('x')
plt.ylabel("$g(x)$")

#Ponerle nombre al grafico
plt.title("Esfera")

# Limitar los valores de los ejes.
#plt.xlim(-7, 7)
#plt.ylim(-10, 10)

#Guardar gráfico como imágen PNG.
plt.savefig("output.png")

#Iniciar leyenda
plt.legend()

#Grilla
plt.grid(True)

#Graficarlo
plt.show()