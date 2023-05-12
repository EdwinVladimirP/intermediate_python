"""
1. LIST                     8. LAMBDA FUNCTIONS                 15. THREADING VS MULTIPROCESSING
2 TUPLES                   9. EXPCEPTIONS AND ERRORS           16. MULTITHREADING
👉. DICTIONARY               10. LOGGING                         17. MULTIPROCESSING
4. SETS                     11. JSON                            18. FUNCTION ARGUMENTS
5. STRINGS                  12. RANDOM NUMBERS                  19. SHALLOW VS DEEP COPYING
6. COLLECTIONS              13. DECORATORS                      20. THE ASTERISK(*) OPERATOR
7. ITERTOOLS                14. GENERATORS                      21CONTEXT MANAGERS
"""

# -> Diccionario es una colección de tipos de datos
# que no tienen orde y son mutables. consiste en una colección
# de pares clave-valor.

mydict = {"name": "Max", "Age": 28, "City": "New York"}
print(type(mydict))

mydict_2 = dict(name="Mary", age=27, City="Boston")  # ----->OJO:
# print("diccionario # 2", type(mydict_2))
# Al usar el método dic(), y colocar los datos clave-valor:
# tener en cuenta que NO SE USA " : " ahora se usa --> " = ", el simbolo =
# tampoco se usan las comillas en la clave, solo en el valor si es un string.
# print(mydict_2["name"])
# print(mydict["name"])
mydict["email"] = "@gmail.com"  # --> Se agregó nuevos datos
# print(mydict)
mydict_2["email"] = "@hotmail.com"  # --> Se agregó nuevos datos
# print(mydict_2)

test = {"name": "Charl", "Age": 28, "City": "Miami"}
# print(test)
# del test["name"]  # -->método para eliminar elemento
# print(test)
# test.pop("name")  # -->método para eliminar elemento
# test.popitem()  # -->método popitem elimina el dato del final.
# print(test)

# if "name" in test:
#     print(test["name"])
# else:
#     print("Nej..")

# try:
#     print(test["name"])
# except:
#     print("Error")

""" OTRO EJEMPLO DE try, except, else, finally: 
try:
  x = int(input("Ingresa un número: "))
  y = 100 / x
except ValueError:
  print("Debe ingresar un número válido")
except ZeroDivisionError:
  print("No se puede dividir entre cero")
else:
  print(f"El resultado es: {y}")
finally:
  print("Fin del programa")

En este ejemplo, el bloque try intenta tomar un número ingresado por
el usuario y dividir 100 entre ese número. Si el usuario ingresa algo
que no es un número, se captura la excepción ValueError y se imprime un
mensaje de error. Si el usuario ingresa cero, se captura la excepción ZeroDivisionError y
se imprime un mensaje de error. Si no se captura ninguna excepción,
el resultado se imprime en la pantalla.

También hay un bloque else que se ejecuta si no se captura ninguna excepción,
y un bloque finally que siempre se ejecuta, sin importar si se captura una excepción o no.
"""

# --------OJO------------con el ciclo for, se puede solicitar la claves:
# for key in test:
#     print(key)

# --------OJO------------con el ciclo for tambien se puede conseguir los valores:
# for value in test.values():
#     print(value)

# --------OJO-------------también se puede solicitar las clave-valor completas, usando .items()
# for key, value in test.items():
#     print(key, value)

# test_copy = test.copy()
# print(test)
# print(test_copy)
# test_copy["email"] = "@outlook.com"  # ------>forma corrécta de copiar un diccionario, sin alterar el original.
# print(test)
# print(test_copy)

# calavera = {"hueso": "mano", "tipo": 21, "color": "Blanco"}
# calavera_2 = dict(calavera)
# calavera_2["país"] = "chile"
# print(calavera)
# print(calavera_2)

# ---> ACTUALIZAR UN DICCIONARIO,las clave-valor se agregarán del seleccionado a actualizar:

saludos = {"ingles": "hello", "español": "hola", "sueco": "hej"}
# value = saludos["sueco"]
# print(value)

# https://www.youtube.com/watch?v=HGOBQPFzWKo

mytuple = (8, 7)
tupla_mas_dict = {mytuple: saludos}
print(tupla_mas_dict)
print(type(tupla_mas_dict))
