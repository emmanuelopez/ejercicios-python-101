"""
Completar la funcion para que devuelva la "frase" pasada como parámetro
reemplazadas todas sus vocales con la "a" (o cualquier otra "vocal" que se
pase como parámetro)
"""


def cambia_vocales(frase, vocal="a"):
    for letra in frase:
        if letra in "aeiou" and letra != vocal.lower():
            frase = frase.replace(letra, vocal.lower())
        else:
            if letra in "AEIOU" and letra != vocal.upper():
                frase = frase.replace(letra, vocal.upper())
    return frase

# ------------------------------------------------------------------------
# NO BORRAR O MODIFICAR LAS LINEAS QUE SIGUEN
# ------------------------------------------------------------------------
# Una vez terminada la tarea ejecutar este archivo.
# Si se ve la leyenda 'Ejercicio terminado OK' el ejercicio se considera completado.
# La instruccion "assert" de Python lanzará un error si lo que se indica a
#   continuacion es falso.
# Si usas GitHub (o similares) podes hacer una nueva rama con esta solución,
#   crear un "pull request" y solicitar revision de un tercero.

assert cambia_vocales("hola") == "hala"
assert cambia_vocales("Juan Carlos") == "Jaan Carlas"
assert cambia_vocales("Pepito", "e") == "Pepete"
assert cambia_vocales(vocal="i", frase="me llamo juan") == "mi llimi jiin"
assert cambia_vocales("PEPEpe", "i") == "PIPIpi"
assert cambia_vocales("PEPEpe", "I") == "PIPIpi"

print('Ejercicio terminado OK')