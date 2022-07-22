"""
Tarea: escribir la función "devolver_mayor_par" para que
devuelva el mayor numero par de la "lista" pasada como parámetro
"""


def es_par(n):
    """
    Dado un numero "n", indicar si es par (mayor a cero) o no
    """
    return n > 0 and n % 2 == 0


def devolver_mayor_par(lista):
    lista_pares = []
    for numero in lista:
        if es_par(numero):
            lista_pares.append(numero)
    #Guardo los numeros pares en una nueva lista y ordeno de mayor a menor, luego retorno el mayor
    #Esto no es necesario para los actuales assert, pero la funcion cumple en el caso que la lista
    #tenga mas de un numero par
    lista_pares.sort(reverse= True)
    return lista_pares[0]


# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.


assert devolver_mayor_par([-1, 3, 6, 9]) == 6
assert devolver_mayor_par([24, 34, -6, 9]) == 34

print('Ejercicio terminado OK')
