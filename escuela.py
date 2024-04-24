#!/bin/python

persistenteVariable=None

global listaDeAlumnos
listaDeAlumnos={
    1: {
        'apellido': 'ABREGU', 
        'nombre': 'JOSE CARLOS',
        "dni": "123456789",
        "fdn": "26/02/2006",
        "grado": "5°",
        "burbuja": "A",
        "notas": [5, 6, 10, 8],
        "tutor": "Mi mama",
        "faltas": 0,
        "amonestaciones": 0},

    2: {
        'apellido': 'TU MAMÁ', 
        'nombre': 'JUAN PEREZ', 
        "dni": "123456789",
        "fdn": "26/02/2006",
        "grado": "5°",
        "burbuja": "A",
        "notas": [5, 6, 10, 8],
        "tutor": "Mi mama",
        "faltas": 0,
        "amonestaciones": 0},

	3: {
        'apellido': 'ABENDAÑO',
        'nombre': 'ROSARIO', 
        "dni": "123456789",
        "fdn": "26/02/2006",
        "grado": "5°",
        "burbuja": "A",
        "notas": [5, 6, 10, 8],
        "tutor": "Mi mama",
        "faltas": 0,
        "amonestaciones": 0},

    4: {
        'apellido': 'AAAA', 
        'nombre': 'BBBBB', 
        "dni": "123456789",
        "fdn": "26/02/2006",
        "grado": "5°",
        "burbuja": "A",
        "notas": [5, 6, 10, 8],
        "tutor": "Mi mama",
        "faltas": 0,
        "amonestaciones": 0},

    5: {
        'apellido': 'BERMEJO', 
        'nombre': 'JOAQUIN', 
        "dni": "123456789",
        "fdn": "26/02/2006",
        "grado": "5°",
        "burbuja": "A",
        "notas": [5, 6, 10, 8],
        "tutor": "Mi mama",
        "faltas": 0,
        "amonestaciones": 0},

    6: {
        'apellido': 'ABENDAÑO', 
        'nombre': 'JOAQUIN',
        "dni": "123456789",
        "fdn": "26/02/2006",
        "grado": "5°",
        "burbuja": "A",
        "notas": [5, 6, 10, 8],
        "tutor": "Mi mama",
        "faltas": 0,
        "amonestaciones": 0}
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
    

def seleccionar(opcion,menu,cantidadDeOpciones,persistente):
    # Menu Principal 
    if type(menu) is list or type(menu) is tuple and len(menu) == 2:
        modo=menu[1]
        menu=menu[0]

    if opcion in cantidadDeOpciones and menu == 0:
        match opcion:
            case "b": # Mostrar los datos de cada alumno
                return 1
            case "c": # Modificar los datos de cada alumno
                return 3
            case "g": # Salir y guardar
                return exit()
    
    # Lista de Alumnos
    elif opcion in cantidadDeOpciones and menu == 1:
        match opcion:
            case "a":
                return 0
            case default:
                return [2, int(opcion)]


    # Visualizador de Información de Alumno
    elif opcion in cantidadDeOpciones and menu == 2:
        return 1

    elif opcion in cantidadDeOpciones and menu == 3:
        match opcion:
            case "a":
                return 0
            case default:
                return [4, int(opcion), int(opcion)]
    
    elif opcion in cantidadDeOpciones and menu == 4:
        match opcion:
            case "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j":
                return [5, opcion]
            case "k":
                return 3

    elif opcion in cantidadDeOpciones and menu == 5:
        return 0

    # Nada 
    elif opcion in cantidadDeOpciones and menu == None:
        return 0

def menuActual(menu, persistente=None):
    if type(menu) is list or type(menu) is tuple and len(menu) == 2:
        modo=menu[1]
        menu=menu[0]

    match menu:
        # Interfaz del Menu Principal
        case 0:
            print("¿Qué desea hacer ahora?")

            print("a. Abrir otra lista")
            print("b. Mostrar los datos de cada alumno")
            print("c. Modificar los datos de los alumnos")
            print("d. Agregar alumno")
            print("e. Expulsar alumno")
            print("f. Configuración")
            print("g. Salir y guardar")
            return ('a', 'b', 'c', 'd', 'e', 'f', 'g')
    
        # Interfaz de la Lista de Alumnos
        case 1:
            print("- Lista de Alumnos -")
            print("¿Cual alumno desea ver?")
            opcionesAlumnos=[]
            for i in range(len(listaDeAlumnos)):
                print (f"{i+1}. {listaDeAlumnos[i+1]['apellido']}, {listaDeAlumnos[i+1]['nombre']}")
                opcionesAlumnos.append(str(i+1))
        
            opcionesAlumnos.append("a")
            
            print("a. Volver")
            return opcionesAlumnos

        # Visualizador de Alumno
        case 2:
            print(f"Alumno {modo} - {listaDeAlumnos[modo]['apellido']}, {listaDeAlumnos[modo]['nombre']}")
            print()
            print("Información General")
            print(f"DNI: {listaDeAlumnos[modo]['dni']}")
            print(f"Fecha de Nacimiento: {listaDeAlumnos[modo]['fdn']}")
            print(f"Grado/Año: {listaDeAlumnos[modo]['grado']}")
            print(f"Burbuja: {listaDeAlumnos[modo]['burbuja']}")
            print()
            print("Información del Alumno")
            print(f"Notas: {listaDeAlumnos[modo]['notas']}")
            promedio=0
            for nota in listaDeAlumnos[modo]['notas']:
                promedio+=nota
        
            print(f"Promedio: {promedio/len(listaDeAlumnos[modo]['notas'])}")
            print(f"Tutor: {listaDeAlumnos[modo]['tutor']}")
            print(f"Faltas: {listaDeAlumnos[modo]['faltas']}")
            print(f"Amonestaciones: {listaDeAlumnos[modo]['amonestaciones']}")
            print()
        
            print("a. Volver")
            return ("a")
    
        case 3:
            print("¿Cual alumno desea modificar?")
            opcionesAlumnos=[]
            for i in range(len(listaDeAlumnos)):
                print (f"{i+1}. {listaDeAlumnos[i+1]['apellido']}, {listaDeAlumnos[i+1]['nombre']}")
                opcionesAlumnos.append(str(i+1))
        
            opcionesAlumnos.append("a")
            
            print("a. Volver")
            return opcionesAlumnos
        
        case 4:
            print(f"¿Que atributo de {listaDeAlumnos[modo]['apellido']}, {listaDeAlumnos[modo]['nombre']} quiere cambiar?")

            print("a. Apellido")
            print("b. Nombre")
            print("c. DNI")
            print("d. Fecha de nacimiento")
            print("e. Grado")
            print("f. Burbuja")
            print("g. Notas")
            print("h. Tutor")
            print("i. Faltas")
            print("j. Amonestaciones")
            print()
            print("k. Volver")
            return ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k")
        
        case 5:
            valorPersistente=persistente
            opcionesModif={
                'a': 'apellido', 
                'b': 'nombre', 
                'c': 'dni', 
                'd': 'fdn', 
                'e': 'grado', 
                'f': 'burbuja', 
                'g': 'notas',
                'h': 'tutor',
                'i': 'faltas',
                'j': 'amonestaciones'}

            modificar=opcionesModif[modo]
            
            nuevo=input("Nuevo: ")
            nuevo=nuevo.upper()
            print(nuevo)
    
            listaDeAlumnos[valorPersistente][modificar]=nuevo

            print("Atributo exitosamente cambiado.")
            print("a. Volver")
            return ("a")
            
            


        # The Dark Realm (solo para depurar, se llama si la pagina en concreto no existe)
        case default:
            print("Esta funcion por ahora no está implementada o intentaste ir a una pagina no existente.")
            print("Si ves este mensaje en software de produccion, por favor mandalo como un bug a nuestro GitHub")
            print("https://github.com/fluffeon/ManejoEscuela-Python")

            print("a. Volver al menú principal")
            return ("a")

def cmds(comando):
    match comando:
        case "currentPage":
            print(f"Pagina actual: {pagina}")

        case "exit" | "salir":
            exit()
    
        case default:
            print("Comando invalido.")

def persistir(variable):
    if len(variable) == 0:
        return
    else:
        return variable

listaDeAlumnos=ordenarDiccionario(listaDeAlumnos)

print("Bienvenido a la Lista Escolar!")
pagina=0
opciones=menuActual(pagina)
argumentoAdic=None
while True:

    if type(pagina) is list and len(pagina) == 3:
        persistenteVariable=pagina[2]

    if type(pagina) is list:
        pagina=pagina[0]

    selecciondeMenu=input("> ")

    if len(selecciondeMenu) <= 0:
        pass

    elif len(selecciondeMenu) >= 2:
        cmds(selecciondeMenu)

    elif selecciondeMenu not in opciones:
        print("Opcion invalida.")
    
    else:
        pagina=seleccionar(selecciondeMenu,pagina,opciones,persistenteVariable)
        opciones=menuActual(pagina,persistenteVariable)

    if pagina == 0:
        listaDeAlumnos=ordenarDiccionario(listaDeAlumnos)