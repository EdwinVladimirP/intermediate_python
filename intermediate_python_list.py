"""from tkinter import *

root = Tk()
root.title("Learning tkinter")

# lbl1 = Label(root, text="<----1------->").grid(row=0, column=0)
# lbl2 = Label(root, text="<----2------->").grid(row=1, column=1)
# lbl3 = Label(root, text="<----3------->").grid(row=2, column=2)

e = Entry(root, width=25, bg="silver", borderwidth=3)
e.pack()
# e.insert(0, "Enter your name..") <---------texto por defaul en la caja de ingreso.
e.get()


def myClick():
    hello = f"Hello, " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()
    print("Barbaroo!! le estas encontrando a python!!")

myButton = Button(root, text="Enter your name", state=ACTIVE, padx=50, pady=50, command=myClick, bg="skyblue", fg="green")
# myButton.grid(row=0, column=0)
myButton.pack()
root.mainloop()"""

# OUTLINE:
"""
👉 LIST                     8. LAMBDA FUNCTIONS                 15. THREADING VS MULTIPROCESSING
2. TUPLES                   9. EXPCEPTIONS AND ERRORS           16. MULTITHREADING
3. DICTIONARY               10. LOGGING                         17. MULTIPROCESSING
4. SETS                     11. JSON                            18. FUNCTION ARGUMENTS
5. STRINGS                  12. RANDOM NUMBERS                  19. SHALLOW VS DEEP COPYING
6. COLLECTIONS              13. DECORATORS                      20. THE ASTERISK(*) OPERATOR
7. ITERTOOLS                14. GENERATORS                      21CONTEXT MANAGERS
"""

mylist = ["banana", "cherry", "apple"]
print(mylist)

# for i in mylist:
#    print(i)

# if "banana" in mylist:
#    print("yes")
# else:
#    print("No")

# print(len(mylist))

# mylist.append("lemon")
# print(mylist)

# mylist.insert(1, "blueberry")
# print(mylist)

# mylist.pop()
# print(mylist)

# item = mylist.pop()
# print(item)

# mylist.remove("cherry")
# print(mylist)

# item = mylist.remove("cherry")
# print(mylist)

# mylist.clear()
# print(mylist)

# mylist.reverse()
# print(mylist)

# mylist.sort()
# print(mylist)

# new_list = sorted(mylist)
# print(new_list)

# nueva = mylist = [12] * 5
# print(nueva)

# new_list = [1, 2, 3]
# new_list_2 = mylist = [4, 5, 6]
# new_list_3 = new_list + new_list_2
# print(new_list_3)

# new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = new_list[1:6]
# print(a)

# new_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = new_list[::2]
# ->[::2] indica que se deben tomar todos los elementos de la lista new_list, pero saltando de a dos elementos.
# print(a)

# list_copy = mylist
# print(mylist)
# print(list_copy)
# list_copy.append("lemon")
# OJO --> al alterar la lista sacada de la original, tambien se altera la original. la manera correcta es con metodo copy
# print(list_copy)
# print(mylist)

# manera correcta:
# list_copy = mylist.copy()
# list_copy.append("lemon")
# print(list_copy)
# print(mylist)

# a = [1, 2, 3, 4, 5, 6]
# b = [i * i for i in a]
# print(a)
# print(b)
# En este caso, la lista por comprensión itera sobre los elementos de la lista "a"
# utilizando la sintaxis "for i in a", donde "i" es una variable temporal que toma
# el valor de cada elemento de "a" en cada iteración. Dentro del bucle, se aplica la
# expresión "i * i" para calcular el cuadrado de cada elemento "i". Finalmente, los
# resultados se almacenan en la lista "b". Por lo tanto, "b" es una lista que contiene
# LOS CUADRADOS DE LOS ELEMENTOS DE "a".


