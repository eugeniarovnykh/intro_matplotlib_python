# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos "multi_line_plot" de clase

    # Se desea graficar varias funciones en un mismmo gráfico (axe)

    # Las funciones que se desean implementar y graficar son:
    # y1 = x**2
    # y2 = x**3

    # Su implementación ya está disponible, es la siguiente:
    x = list(np.linspace(-4, 4, 20))

    y1 = []
    for i in x:
        y1.append(i**2)

    y2 = []
    for i in x:
        y2.append(i**3)

    # Alumno: Realizar un gráfico que representen las dos funciones
    # Para ello se debe llamar dos veces a "plot" con el mismo "ax"
    fig = plt.figure()
    ax = fig.add_subplot()

    
    # Se debe colocar en la leyenda la función que representa
    # cada función
    ax.plot(x, y1, color='b', marker='^', label='linea 1')
    ax.plot(x, y2, color='g', marker='+', label='linea 2')
    # Cada función dibujarla con un color distinto
    # a su elección
    ax.set_facecolor('white')
    ax.set_title("Grafico 2")
    ax.set_ylabel("y")
    ax.set_xlabel("x")
    plt.show()     
    # Crear acá su gráfico

    print("terminamos")
