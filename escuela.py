#!/bin/python

listaDeAlumnos={

    1:{
        "nombre": "JUAN SANTIAGO",
        "apellido": "ABREGU",
        "DNI": "123456789",
        "Nacimiento": "26/02/2006",
        "Grado": "5°",
        "Burbuja": "A",
        "Notas": [5, 6, 10, 8],
        "Tutor": "Mi mama",
        "Faltas": 0,
        "Amonestaciones": 0},

    2:{
        "nombre": "ANGEL NICOLAS",
        "apellido": "FLORES CASTRO",
        "DNI": "123456789",
        "Nacimiento": "26/02/2006",
        "Grado": "5°",
        "Burbuja": "A",
        "Notas": [5, 6, 10, 8],
        "Tutor": "Mi mama",
        "Faltas": 0,
        "Amonestaciones": 0}
    
    }

def ordenarDiccionario(dicc):
    listaOrden=[]
    for i in range(len(dicc)):
	    listaOrden.append(f"{dicc[i+1]['apellido']}, {dicc[i+1]['nombre']}")

    listaOrden.sort()

    Contador=0
    Contador2=0
    diccSegundo={}
    Comparar=""

    while Contador < len(dicc):
	
        Comparar2=listaOrden[Contador]
	
        Contador2+=1
        Comparar=f"{dicc[Contador2]["apellido"]}, {dicc[Contador2]['nombre']}"
        
        if Comparar == Comparar2:
            diccSegundo[Contador+1]=dicc[Contador2]
            Contador2=0
            Contador+=1
        elif Contador2 == len(dicc):
            Contador2=0
            Contador+=1
    

    return diccSegundo
    

def seleccionar(opcion,menu,cantidadDeOpciones):
    # Menu Principal
    if opcion in cantidadDeOpciones and menu == 0:
        if opcion == "b":
            return 1
        if opcion == "h":
            return exit()
    
    # Lista de Alumnos
    elif opcion in cantidadDeOpciones and menu == 1:
        if opcion == "a":
            return 0
        
    elif opcion in cantidadDeOpciones and menu == None:
        if opcion == "a":
            return 0

def menuActual(menu):
    # Interfaz del Menu Principal
    if menu == 0:
        print("¿Qué desea hacer ahora?")
        print("a. Abrir otra lista")
        print("b. Mostrar los datos de cada alumno")
        print("c. Modificar los datos de los alumnos")
        print("d. Ordenar la lista")
        print("e. Agregar alumnos")
        print("f. Expulsar alumnos")
        print("g. Configuración")
        print("h. Salir y guardar")
        return ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
    
    # Interfaz de la Lista de Alumnos
    elif menu == 1:
        print("- Lista de Alumnos -")
        print("¿Cual alumno desea ver?")
        opcionesAlumnos=[]
        for i in range(len(listaDeAlumnos)):
            print (f"{i+1}. {listaDeAlumnos[i+1]['apellido']}, {listaDeAlumnos[i+1]['nombre']}")
            opcionesAlumnos.append(str(i+1))
        
        opcionesAlumnos.append("a")
            
        print("a. Volver")
        return opcionesAlumnos

    # The Dark Realm (solo para depurar)
    if menu == None:
        print("Esta funcion por ahora no está implementada o intentaste ir a una pagina no existente.")
        print("Si ves este mensaje en software de produccion, por favor mandalo como un bug a nuestro GitHub")
        print("https://github.com/fluffeon/ManejoEscuela-Python")
        print("a. Volver al menú principal")
        return ("a")

print("Bienvenido a la Lista Escolar!")
pagina=0
opciones=menuActual(pagina)
while True:
    
    selecciondeMenu=input("> ")

    if len(selecciondeMenu) <= 0:
        pass
    elif selecciondeMenu == "currentPage":
        print(f"Pagina actual: {pagina}")
    elif len(selecciondeMenu) >= 2 or selecciondeMenu not in opciones:
        print("Opcion invalida.")
    else:
        pagina=seleccionar(selecciondeMenu,pagina,opciones)
        opciones=menuActual(pagina)