#!/bin/python

persistenteVariable=None

"""
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
        'apellido': 'CARRAZCO', 
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
        'nombre': 'ROSA', 
        "dni": "123456789",
        "fdn": "26/02/2006",
        "grado": "5°",
        "burbuja": "A",
        "notas": [5, 6, 10, 8],
        "tutor": "Mi mama",
        "faltas": 0,
        "amonestaciones": 0},

    4: {
        'apellido': 'FERNÁNDEZ', 
        'nombre': 'BRANDON QUISPE', 
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
"""

class Alumno:

    def __init__(self,apellido,nombre,dni="",fdn="",grado="",division="",notas=[],tutor="",faltas=int(),amonestaciones=int()):
        self.apellido = apellido.upper().lstrip().rstrip()
        self.nombre = nombre.upper().lstrip().rstrip()
        self.dni = dni.lstrip().rstrip()
        self.fdn = fdn.lstrip().rstrip()
        self.grado = grado.lstrip().rstrip()
        self.division = division.lstrip().rstrip()
        self.notas = list(notas)
        for nota in self.notas:
            if nota not in range(1,11):
                raise ValueError('No se pueden poner valores mayores de 10 ni menores de 1 en una lista de notas.')
        self.tutor = tutor.lstrip().rstrip()
        self.faltas = int(faltas)
        self.amonestaciones = int(amonestaciones)

    def dato(self,datoASacar):
        match datoASacar:
            case "apellido":
                return self.apellido
            case "nombre":
                return self.nombre
            case "dni":
                return self.dni
            case "fdn":
                return self.fdn
            case "grado":
                return self.grado
            case "division":
                return self.division
            case "notas":
                return self.notas
            case "tutor":
                return self.tutor
            case "faltas":
                return self.faltas
            case "amonestaciones":
                return self.amonestaciones

    def reemplazar(self,datoAReemplazar,nuevo):
        match datoAReemplazar:
            case "apellido":
                self.apellido = nuevo.upper().lstrip().rstrip()
            case "nombre":
                self.nombre = nuevo.upper().lstrip().rstrip()
            case "dni":
                self.dni = nuevo.lstrip().rstrip()
            case "fdn":
                self.fdn = nuevo.lstrip().rstrip()
            case "grado":
                self.grado = nuevo.lstrip().rstrip()
            case "division":
                self.division = nuevo.lstrip().rstrip()
            case "notas":
                self.notas = list(nuevo)
                for nota in self.notas:
                    if nota not in range(1,11):
                        raise ValueError('No se pueden poner valores mayores de 10 ni menores de 1 en una lista de notas.')
            case "tutor":
                self.tutor = nuevo.lstrip().rstrip()
            case "faltas":
                self.faltas = int(nuevo)
            case "amonestaciones":
                self.amonestaciones = int(nuevo)
    
    def agregar(self,datoAAgregar,nuevo):
        match datoAAgregar:
            case "notas":
                if nuevo not in range(1,11):
                    raise ValueError('No se pueden poner valores mayores de 10 ni menores de 0 en una lista de notas.')
                else:
                    self.notas.append(nuevo)
            case "faltas":
                self.faltas += int(nuevo)
            case "amonestaciones":
                self.amonestaciones += int(nuevo)
            
    
listaDeAlumnos=[
    
    Alumno(
    apellido="abendaño",
    nombre="joaquin", 
    fdn="26/02/2006", 
    grado="5º", 
    division="A", 
    notas=[10, 2, 4, 10],
    tutor="Mi mamá",
    faltas=0,
    amonestaciones=0), 
    
    Alumno(
    apellido="caca",
    nombre="juan perez", 
    fdn="26/02/2006", 
    grado="5º", 
    division="A", 
    notas=[10, 2, 4, 10],
    tutor="Mi mamá",
    faltas=0,
    amonestaciones=0), 

    Alumno(
    apellido="balá",
    nombre="carlos", 
    fdn="26/02/2006", 
    grado="5º", 
    division="A", 
    notas=[10, 2, 4, 10],
    tutor="Mi mamá",
    faltas=0,
    amonestaciones=0),

    Alumno(
    apellido="Abregú",
    nombre="Juan Carlos", 
    fdn="26/02/2006", 
    grado="5º", 
    division="A", 
    notas=[10, 2, 4, 10],
    tutor="Mi mamá",
    faltas=0,
    amonestaciones=0)

    ]

print(listaDeAlumnos[0].dato("apellido"))
print(listaDeAlumnos[0].dato("notas"))
listaDeAlumnos[0].agregar("notas",5)
listaDeAlumnos[0].agregar("notas",10)

print(listaDeAlumnos[0].dato("notas"))
print(listaDeAlumnos[0].dato("apellido"))


for i in range(len(listaDeAlumnos)):
	print(f"{listaDeAlumnos[i].dato('apellido')}, {listaDeAlumnos[i].dato('nombre')}")

print(listaDeAlumnos)

def ordenarLista(lista):
    listaOrden=[]
    for i in range(len(lista)):
	    listaOrden.append(f"{lista[i].dato('apellido')}, {lista[i].dato('nombre')}")

    listaRespaldo = []
    listaOrden.sort()

    print(listaOrden)
    print(listaRespaldo)

    Contador=0
    Contador2=0

    while True:
        if Contador == len(listaOrden):
            break

        IteraciónActual=f"{lista[Contador].dato('apellido')}, {lista[Contador].dato('nombre')}"
        IteraciónActual2=lista[Contador]
        print(IteraciónActual)

        if IteraciónActual == listaOrden[i]:
            listaRespaldo.append(IteraciónActual2)
            Contador+=1
            Contador2=0

        if Contador2 == len(lista):
            Contador+=1
            Contador2=0
        else:
            Contador2+=1

    return listaRespaldo

    
print(ordenarLista(listaDeAlumnos))

exit()

def seleccionar(opcion,menu,cantidadDeOpciones,persistente):

    if type(menu) is list or type(menu) is tuple and len(menu) == 2:
        modo=menu[1]
        menu=menu[0]

    # Menu Principal (ID: 0)
    if opcion in cantidadDeOpciones and menu == 0:
        match opcion:
            case "a": # Mostrar los datos de cada alumno
                return 1
            case "b": # Modificar los datos de los alumnos
                return 3
            case "c": # Agregar alumno
                return 6
            case "d": # Expulsar alumno
                return 7
            case "e": # Salir y guardar
                return exit()
    
    # Lista de Alumnos (ID: 1)
    elif opcion in cantidadDeOpciones and menu == 1:
        match opcion:
            case "a":
                return 0
            case default:
                return [2, int(opcion)]


    # Visualizador de Información de Alumno (ID: 2)
    elif opcion in cantidadDeOpciones and menu == 2:
        return 1

    # Visualizador de Información de Alumno (para modificar) (ID: 3)
    elif opcion in cantidadDeOpciones and menu == 3:
        match opcion:
            case "a":
                return 0
            case default:
                return [4, int(opcion), int(opcion)]

    # Seleccionador para Modificar atributos de Alumno (ID: 4) 
    elif opcion in cantidadDeOpciones and menu == 4:
        match opcion:
            case "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j":
                return [5, opcion]
            case "k":
                return 3

    # Modificador de Atributos de Alumno / Herramienta para Agregar Alumnos (ID: 5, ID: 6)
    elif opcion in cantidadDeOpciones and menu == 5 or menu == 6 or menu == 8:
        return 0
    
    elif opcion in cantidadDeOpciones and menu == 7:
        match opcion:
            case "a":
                return 0
            case default:
                return [8, int(opcion), int(opcion)]

    # Pagina no existente (ID: None)
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

            print("a. Mostrar los datos de cada alumno")
            print("b. Modificar los datos de los alumnos")
            print("c. Agregar alumno")
            print("d. Expulsar alumno")
            print("e. Salir y guardar")
            return ('a', 'b', 'c', 'd', 'e')
    
        # Interfaz de la Lista de Alumnos
        case 1:
            print("- Lista de Alumnos -")
            opcionesAlumnos=[]
            if len(listaDeAlumnos) != 0:
                print("¿Cual alumno desea ver?")
                for i in range(len(listaDeAlumnos)):
                    print (f"{i+1}. {listaDeAlumnos[i+1]['apellido']}, {listaDeAlumnos[i+1]['nombre']}")
                    opcionesAlumnos.append(str(i+1))
            else:
                print("No hay alumnos inscriptos en esta lista.")
        
            opcionesAlumnos.append("a")
            
            print("a. Volver")
            return opcionesAlumnos

        # Interfaz del Visualizador de Alumno
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

            print(f"Tutor: {listaDeAlumnos[modo]['tutor']}")
            print(f"Faltas: {listaDeAlumnos[modo]['faltas']}")
            print(f"Amonestaciones: {listaDeAlumnos[modo]['amonestaciones']}")
            print()
        
            print("a. Volver")
            return ("a")

        # Seleccionar cual alumno modificar atributos
        case 3:
            opcionesAlumnos=[]
            if len(listaDeAlumnos) != 0:
                print("¿Cual alumno desea modificar?")
                for i in range(len(listaDeAlumnos)):
                    print (f"{i+1}. {listaDeAlumnos[i+1]['apellido']}, {listaDeAlumnos[i+1]['nombre']}")
                    opcionesAlumnos.append(str(i+1))
            else:
                print("No hay alumnos inscriptos en esta lista.")
        
            opcionesAlumnos.append("a")
            
            print("a. Volver")
            return opcionesAlumnos
        
        # Selector de Atributos a Modificar del Alumno
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
        
        # Herramienta para Modificar atributos del alumno
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

            vacio=None
            
            nuevo=input(f"Nuevo atributo '{modificar}': ")
            nuevo=nuevo.upper()
            nuevo=nuevo.lstrip()
            nuevo=nuevo.rstrip()

            if modificar == 'notas':
                    nuevo=list(nuevo)

            for caracter in nuevo:
                if caracter != " ":
                    listaDeAlumnos[valorPersistente][modificar]=nuevo
                    vacio=False
                    break
        
            if vacio == False:
                print("Atributo exitosamente cambiado.")
            else:
                print("Operación cancelada.")

            print("a. Volver")
            return ("a")
    
        # Agregar alumno
        case 6:
            Vacio=None
            print ("- Agregar alumno -")
            opcionesModif={
                0: 'apellido', 
                1: 'nombre', 
                2: 'dni', 
                3: 'fdn', 
                4: 'grado', 
                5: 'burbuja', 
                6: 'notas',
                7: 'tutor',
                8: 'faltas',
                9: 'amonestaciones'}
            
            listaParaPoner=[]
            
            for i in range(len(opcionesModif)):
                Valor=input(f"Inserte atributo '{opcionesModif[i]}': ")

                Valor=Valor.lstrip()
                Valor=Valor.rstrip()
                Valor=Valor.upper()

                if len(Valor) == 0:
                    Vacio=True
                    break
                else:
                    if opcionesModif[i] == 'notas':
                        Valor=list(Valor)
                    listaParaPoner.append(Valor)
            
            if Vacio == True:
                print("Operación cancelada.")
            else:
                listaDeAlumnos[len(listaDeAlumnos)+1]={
                    f"{opcionesModif[0]}": f"{listaParaPoner[0]}",
                    f"{opcionesModif[1]}": f"{listaParaPoner[1]}",
                    f"{opcionesModif[2]}": f"{listaParaPoner[2]}",
                    f"{opcionesModif[3]}": f"{listaParaPoner[3]}",
                    f"{opcionesModif[4]}": f"{listaParaPoner[4]}",
                    f"{opcionesModif[5]}": f"{listaParaPoner[5]}",
                    f"{opcionesModif[6]}": f"{listaParaPoner[6]}",
                    f"{opcionesModif[7]}": f"{listaParaPoner[7]}",
                    f"{opcionesModif[8]}": f"{listaParaPoner[8]}",
                    f"{opcionesModif[9]}": f"{listaParaPoner[9]}"
                    }
                
                print("Se ha agregado al alumno con exito.")
            print("a. Volver")
            return ("a")

        # Seleccionar cual alumno expulsar
        case 7:
            opcionesAlumnos=[]
            if len(listaDeAlumnos) != 0:
                print("¿A cual alumno quiere expulsar?")
                for i in range(len(listaDeAlumnos)):
                    print (f"{i+1}. {listaDeAlumnos[i+1]['apellido']}, {listaDeAlumnos[i+1]['nombre']}")
                    opcionesAlumnos.append(str(i+1))
            else:
                print("No hay alumnos inscriptos en esta lista.")
            
            opcionesAlumnos.append("a")
            
            print("a. Volver")
            return opcionesAlumnos

        # Expulsador de Alumnos 3000
        case 8:
            valorPersistente=modo
            Respaldo=listaDeAlumnos

            Confirmación=input(f"¿Está seguro que quiere expulsar al alumno/a {listaDeAlumnos[modo]['apellido']}, {listaDeAlumnos[modo]['nombre']}? (s/N) ")
            Confirmación=Confirmación.lstrip()
            Confirmación=Confirmación.rstrip()
            
            if Confirmación == "s":
                Confirmación="S"

            if Confirmación == "S" and len(Confirmación) == 1:

                for i in range(modo,len(listaDeAlumnos)):
                    listaDeAlumnos[i]=listaDeAlumnos[i+1]
            
                del listaDeAlumnos[len(listaDeAlumnos)]

                print("Se ha expulsado al alumno con exito.")

            else:
                print("Operación cancelada.")

            print("a. Volver")
            return ("a")


        # Pagina no existente
        case default:
            print("Esta funcion por ahora no está implementada o intentaste ir a una pagina no existente.")
            print("Si ves este mensaje en software de produccion, por favor mandalo como un bug a nuestro GitHub")
            print("https://github.com/fluffeon/ManejoEscuela-Python")

            print("a. Volver al menú principal")
            return ("a")

def cmds(comando):
    match comando:
        case "paginaActual":
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
try:
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
except KeyboardInterrupt:
    cmds("exit")