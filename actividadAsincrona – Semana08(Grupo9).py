print("---------------------------")
print("------¡Identificador!------")
print("---------------------------")

print("Menú de opciones")             #Menu que se imprime al iniciar el progrma
print("Presione 1 para identificar gentilicios")     #Opcion 1
print("Presione 2 para identificar animales")         #Opcion 2

opción = int(input("¿Cuál es la opción que desea seleccionar? \n"))  #Esta linea del codigo da inicio al programa

if opción == 1:                               #Aqui empieza la opcion uno si la variable es igual a uno de los elif o if se ejecutara lo planteado en cada linea
    print("Identificador de gentilicios\n")
    
    opcionhumano = str(input("¿Cuál es el gentilicio que desea identificar? ")).lower()
    
    if opcionhumano == "el salvador":
        print("Su gentilicio es 'Salvadoreño' ")
    elif opcionhumano == "mexico":
        print("Su gentilicio es 'Mexicano/a' ")
    elif opcionhumano == "estados unidos":
        print("Su gentilicio es 'Estadounidense' ")
    elif opcionhumano == "canada":
        print("Su gentilicio es 'Canadiense' ")
    elif opcionhumano == "inglaterra":
        print("Su gentilico es 'Británico/a' ")
    elif opcionhumano == "argentina":
        print("Su gentilicio es 'Argentino/a' ")
    elif opcionhumano == "españa":
        print("Su gentilicio es 'Español/a' ")
    elif opcionhumano == "chile":
        print("SU gentilicio es 'Chileno/a' ")
    elif opcionhumano == "australia":
        print("Su gentilicio es 'Australiano/a' ")
    elif opcionhumano == "italia":
        print("Su gentilicio es 'Italiano/a' ")          #Aqui terminan los elif
    else:                                                 #La opcion else por si ningun dato introducido es igual
        print('Ese no esta en la base de datos \n')           
        
        
elif opción == 2:                                         #Aqui empieza la opcion identificador de Animales, si la variable introducida es igual a alguno de los if se desarrollara correctamente
    print("Identificador de tipo de animal")
    
    opcionanimal = str(input("¿Cuál es el tipo de animal que desea idetificar?")).lower()        #Aqui introduce el nombre de un animal
    
    if opcionanimal == "lobo":
        print("El tipo de animal es 'canino'")
    elif opcionanimal == "tigre":
        print("El tipo de animal es 'felino'")
    elif opcionanimal == "vaca":
        print("El tipo de animal es 'bobino'")
    elif opcionanimal == "caballo":
        print("El tipo de animal es 'equino'")
    elif opcionanimal == "oso":
        print("El tipo de animal es 'pantígrado'")
    elif opcionanimal == "colibrí":
        print("El tipo de animal es 'ave'")
    elif opcionanimal == "iguana":
        print("El tipo de animal es 'reptil'")
    elif opcionanimal == "perro":
        print("El tipo de animal es 'canino'")
    elif opcionanimal == "pingüino":
        print("El tipo de animal es 'ave'")
    elif opcionanimal == "leon":   #sin tilde
        print("El tipo de animal es 'felino'")      #Aqui terminan todas las opciones de if que habias
    else:                                          #Y el else por si la variable no cuadra con ningun if
        print("El animal ingresado no se puede identificar")
        
else:
    print("Opción no disponible")         #Este else es de el menu de inicio, si no introduce 1 o 2 que son las opciones, saltara este print para hacerle saber que no se puede desarrollar el programa
    
print("FIN\n")     #FIN
