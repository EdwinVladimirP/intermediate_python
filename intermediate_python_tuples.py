"""
1. LIST                     8. LAMBDA FUNCTIONS                 15. THREADING VS MULTIPROCESSING
👉 TUPLES                   9. EXPCEPTIONS AND ERRORS           16. MULTITHREADING
3. DICTIONARY               10. LOGGING                         17. MULTIPROCESSING
4. SETS                     11. JSON                            18. FUNCTION ARGUMENTS
5. STRINGS                  12. RANDOM NUMBERS                  19. SHALLOW VS DEEP COPYING
6. COLLECTIONS              13. DECORATORS                      20. THE ASTERISK(*) OPERATOR
7. ITERTOOLS                14. GENERATORS                      21CONTEXT MANAGERS
"""
import timeit

mytuple = tuple(["Max", 25, "Boston"])
mytuple_2 = ("a", "b", "b", "c", "d", "e", "f", "g")
# UNA TUPLA es una colección de tipos de datos
# que es ordenada é inmutable.

# mytuple = ("Max", 25, "Boston")  # ---> los parentesis son opcionales.
# print(type(mytuple))
# OJO --> al contener un solo dato, se convierte en <'str'>
# Pero si se le coloca una coma al final, se convierte en <'tuple'>

# mytuple = tuple(["max", 25, "Boston"])  # --->se recibe lista (tuple() recibe solo 1 argumento.
# print(mytuple)
# print(mytuple[0])
# print(mytuple[1])
# print(mytuple[2])

# mytuple = tuple(["max", 25, "Boston"])
# for i in mytuple:
#     print([i])

# if "Max" in mytuple:  # ---->se burca el dato en la lista que contiene la tupla.
#     print("yes")
# else:
#     print("NO")

# print(len(mytuple_2))

# print(mytuple_2.count("b"))

# print(mytuple_2.index("g"))

# print(type(mytuple_2))
# mytuple_2 = list(mytuple_2)
# print(type(mytuple_2))
# mytuple_2 = tuple(mytuple_2)
# print(type(mytuple_2))

# mytuple_3 = mytuple_2[2:5]
# print(mytuple_3)

# name, age, city = mytuple
# print(name)
# print(age)
# print(city)
# print(name, age, city)

# import sys

# my_list = [0, 1, 2, "hello", True]
# my_tuple = (0, 1, 2, "hello", True)
# print(sys.getsizeof(my_list), "bites")
# print(sys.getsizeof(my_tuple), "bites")

# import time

# print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
# print(timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
"""En el contexto de la función timeit de Python, stmt (statement) es
un argumento que se utiliza para especificar la instrucción o bloque de código
que se va a medir el tiempo de ejecución. Es decir, el valor del argumento stmt
es el código que se va a repetir varias veces para medir el tiempo de ejecución promedio.

Por ejemplo, si se quiere medir el tiempo que tarda en ejecutarse un bucle for
que crea una lista de números, se puede pasar el bucle for como
valor del argumento stmt.
"""



# https://www.youtube.com/watch?v=HGOBQPFzWKo
