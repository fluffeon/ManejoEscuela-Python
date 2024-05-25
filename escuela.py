#!/bin/python

persistenteVariable=None
class Alumno:

    def __init__(self,apellido,nombre,dni="Desconocido",fdn="Desconocido",grado="Desconocido",division="",notas=[],tutor="Desconocido",domicilio="Desconocido",faltas=int(0),amonestaciones=int(0)):
        self.apellido = apellido.upper().lstrip().rstrip()
        self.nombre = nombre.upper().lstrip().rstrip()
        self.dni = dni.lstrip().rstrip()
        self.fdn = fdn.lstrip().rstrip()
        self.grado = grado.lstrip().rstrip()
        self.division = division.lstrip().rstrip()
        self.domicilio = domicilio.lstrip().rstrip()
        self.notas = list(notas)
        for nota in self.notas:
            if nota not in range(1,11):
                raise ValueError('No se pueden poner valores mayores de 10 ni menores de 1 en una lista de notas.')
        self.tutor = tutor.lstrip().rstrip()
        if faltas >= 0:
            self.faltas = int(faltas)
        else:
            self.amonestaciones = 0

        if amonestaciones >= 0:
            self.amonestaciones = int(amonestaciones)
        else:
            self.amonestaciones = 0

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
            case "domicilio":
                return self.domicilio
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
            case "domicilio":
                self.domicilio = nuevo.lstrip().rstrip()
            case "notas":
                self.notas = list(nuevo)
                for nota in self.notas:
                    if nota not in range(1,11):
                        raise ValueError('No se pueden poner valores mayores de 10 ni menores de 1 en una lista de notas.')
            case "tutor":
                self.tutor = nuevo.lstrip().rstrip()
            case "faltas":
                if int(nuevo) >= 0:
                    self.faltas = int(faltas)
                else:
                    self.amonestaciones = 0
            case "amonestaciones":
                if int(nuevo) >= 0:
                    self.amonestaciones = int(nuevo)
                else:
                    self.amonestaciones = 0
    
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

    def remover(self,datoARemover,nuevo):
        match datoARemover:
            case "notas":
                del self.notas[nuevo]
            case "faltas":
                self.faltas -= int(nuevo)
                if self.faltas < 0:
                    self.faltas = 0
            case "amonestaciones":
                self.amonestaciones -= int(nuevo)
                if self.amonestaciones < 0:
                    self.amonestaciones = 0
            
    
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

for i in range(len(listaDeAlumnos)):
	print(f"{listaDeAlumnos[i].dato('apellido')}, {listaDeAlumnos[i].dato('nombre')}")

def ordenarLista(lista):
    listaOrden = sorted(lista, key=lambda x: x.apellido, reverse=False)
    return listaOrden

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
            case "a" | "b" | "c" | "d" | "e" | "f" | "g" | "h" | "i" | "j" | "k" | "l" | "m" | "n":
                return [5, opcion]
            case "o":
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
                    print (f"{i+1}. {listaDeAlumnos[i].dato('apellido')}, {listaDeAlumnos[i].dato('nombre')}")
                    opcionesAlumnos.append(str(i+1))
            else:
                print("No hay alumnos inscriptos en esta lista.")
        
            opcionesAlumnos.append("a")
            
            print("a. Volver")
            return opcionesAlumnos

        # Interfaz del Visualizador de Alumno
        case 2:
            print(f"Alumno {modo} - {listaDeAlumnos[modo-1].dato('apellido')}, {listaDeAlumnos[modo-1].dato('nombre')}")
            print()
            print("Información General")
            print(f"Domicilio: {listaDeAlumnos[modo-1].dato('domicilio')}")
            print(f"DNI: {listaDeAlumnos[modo-1].dato('dni')}")
            print(f"Fecha de Nacimiento: {listaDeAlumnos[modo-1].dato('fdn')}")
            print(f"Grado/Año: {listaDeAlumnos[modo-1].dato('grado')}")
            if len(listaDeAlumnos[modo-1].dato('division')) != 0 :
                print(f"División: {listaDeAlumnos[modo-1].dato('division')}")
            print()
            print("Información del Alumno")
            if len(listaDeAlumnos[modo-1].dato('notas')) == 0:
                print("Este alumno no tiene notas por el momento.")
            else:
                print(f"Notas: {listaDeAlumnos[modo-1].dato('notas')}")
                Acumulador=0
                for i in listaDeAlumnos[modo-1].dato('notas'):
                    Acumulador+=i
                print(f"Promedio: {Acumulador / len(listaDeAlumnos[modo-1].dato('notas'))}")

            print(f"Tutor: {listaDeAlumnos[modo-1].dato('tutor')}")
            print(f"Faltas: {listaDeAlumnos[modo-1].dato('faltas')}")
            print(f"Amonestaciones: {listaDeAlumnos[modo-1].dato('amonestaciones')}")
            print()
        
            print("a. Volver")
            return ("a")

        # Seleccionar cual alumno modificar atributos
        case 3:
            opcionesAlumnos=[]
            if len(listaDeAlumnos) != 0:
                print("¿Cual alumno desea modificar?")
                for i in range(len(listaDeAlumnos)):
                    print (f"{i+1}. {listaDeAlumnos[i].dato('apellido')}, {listaDeAlumnos[i].dato('nombre')}")
                    opcionesAlumnos.append(str(i+1))
            else:
                print("No hay alumnos inscriptos en esta lista.")
        
            opcionesAlumnos.append("a")
            
            print("a. Volver")
            return opcionesAlumnos
        
        # Selector de Atributos a Modificar del Alumno
        case 4:
            print(f"¿Que atributo de {listaDeAlumnos[modo-1].dato('apellido')}, {listaDeAlumnos[modo-1].dato('nombre')} quiere cambiar?")

            print("a. Apellido")
            print("b. Nombre")
            print("c. DNI")
            print("d. Fecha de nacimiento")
            print("e. Grado")
            print("f. División")
            print("g. Tutor")
            print("h. Domicilio")
            print("i. Agregar nota")
            print("j. Remover nota")
            print("k. Agregar faltas")
            print("l. Remover faltas")
            print("m. Agregar amonestaciones")
            print("n. Remover amonestaciones")
            print()
            print("o. Volver")
            return ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o")
        
        # Herramienta para Modificar atributos del alumno
        case 5:
            valorPersistente=persistente
            opcionesModif={
                'a': 'apellido', 
                'b': 'nombre', 
                'c': 'dni', 
                'd': 'fdn', 
                'e': 'grado', 
                'f': 'division', 
                'g': 'tutor',
                'h': 'domicilio',
                'i': 'agregarNota',
                'j': 'removerNota',
                'k': 'agregarFalta',
                'l': 'removerFalta',
                "m": 'agregarAmonestacion',
                'n': 'removerAmonestacion'}

            modificar=opcionesModif[modo]

            Vacio=False
            
            match modificar:
                case "agregarFalta" | "agregarAmonestacion":
                    nuevo=input(f"Agregar numero de '{modificar}': ")
                case "removerFalta" | "removerAmonestacion":
                    nuevo=input(f"Remover numero de '{modificar}': ")
                case "agregarNota":
                    nuevo=input(f"Agregar '{modificar}' (1-10): ")
                case "removerNota":
                    Notas=listaDeAlumnos[valorPersistente-1].dato("notas")
                    if len(Notas) == 0:
                        print("Este alumno no tiene notas aún.")
                        nuevo=""
                    else:
                        print(f"¿Cual nota quieres remover de {listaDeAlumnos[valorPersistente-1].dato('apellido')}, {listaDeAlumnos[valorPersistente-1].dato('nombre')}?")
                        for i in range(0, len(Notas)):
                            print(f"{i+1}. {Notas[i]}")
                        nuevo=input(f"Remover '{modificar}': ")
                        if nuevo == 0:
                            nuevo=""
                case default:
                    nuevo=input(f"Nuevo atributo '{modificar}': ")

            
            nuevo=nuevo.lstrip().rstrip()
            
            if len(nuevo) != 0:
                match modificar:
                    case "agregarNota" | "removerNota":
                        try:
                            nuevo=int(nuevo.lstrip().rstrip())
                            if modificar == "agregarNota":
                                listaDeAlumnos[valorPersistente-1].agregar("notas",nuevo)
                            elif modificar == "removerNota":
                                if nuevo >= 1:
                                    listaDeAlumnos[valorPersistente-1].remover("notas",nuevo-1)
                                else:
                                    Vacio=True
                        except ValueError:
                            Vacio=True
                    case "agregarFalta":
                        try:
                            nuevo=int(nuevo.lstrip().rstrip())
                            listaDeAlumnos[valorPersistente-1].agregar("faltas",nuevo)
                        except ValueError:
                            Vacio=True
                    case "removerFalta":
                        try:
                            nuevo=int(nuevo.lstrip().rstrip())
                            listaDeAlumnos[valorPersistente-1].remover("faltas",nuevo)
                        except ValueError:
                            Vacio=True
                    case "agregarAmonestacion":
                        try:
                            nuevo=int(nuevo.lstrip().rstrip())
                            listaDeAlumnos[valorPersistente-1].agregar("amonestaciones",nuevo)
                        except ValueError:
                            Vacio=True
                    case "removerAmonestacion":
                        try:
                            nuevo=int(nuevo.lstrip().rstrip())
                            listaDeAlumnos[valorPersistente-1].remover("amonestaciones",nuevo)
                        except ValueError:
                            Vacio=True
                    case default:
                        nuevo=nuevo.lstrip().rstrip().upper()
                        listaDeAlumnos[valorPersistente-1].reemplazar(modificar,nuevo)
            else:
                Vacio=True
        
            if Vacio == False:
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
                5: 'division',
                6: 'tutor',
                7: 'domicilio'
                }
            
            listaParaPoner=[]
            
            for i in range(len(opcionesModif)):
                if opcionesModif[i] == "apellido" or opcionesModif[i] == "nombre":
                    Valor=input(f"Inserte atributo '{opcionesModif[i]}' (obligatorio): ")
                else:
                    Valor=input(f"Inserte atributo '{opcionesModif[i]}' (opcional): ")

                Valor=Valor.lstrip().rstrip().upper()

                if len(Valor) == 0 and opcionesModif[i] != "division" and opcionesModif[i] != "grado" and opcionesModif[i] != "dni" and opcionesModif[i] != "fdn" and opcionesModif[i] != "tutor":
                    Vacio=True
                    break
                else:
                    listaParaPoner.append(Valor)
            
            if Vacio == True:
                print("Operación cancelada.")
            else:
                listaDeAlumnos.append(
                    Alumno(
                        apellido=listaParaPoner[0],
                        nombre=listaParaPoner[1],
                        dni=listaParaPoner[2],
                        fdn=listaParaPoner[3],
                        grado=listaParaPoner[4],
                        division=listaParaPoner[5],
                        tutor=listaParaPoner[6],
                        domicilio=listaParaPoner[7]                    
                    )
                )
                
                print("Se ha agregado al alumno con exito.")
            print("a. Volver")
            return ("a")

        # Seleccionar cual alumno expulsar
        case 7:
            opcionesAlumnos=[]
            if len(listaDeAlumnos) != 0:
                print("¿A cual alumno quiere expulsar?")
                for i in range(len(listaDeAlumnos)):
                    print (f"{i+1}. {listaDeAlumnos[i].dato('apellido')}, {listaDeAlumnos[i].dato('nombre')}")
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

            Confirmación=input(f"¿Está seguro que quiere expulsar al alumno/a {listaDeAlumnos[modo-1].dato('apellido')}, {listaDeAlumnos[modo-1].dato('nombre')}? (s/N) ")
            Confirmación=Confirmación.lstrip().rstrip()
            
            if Confirmación == "s":
                Confirmación="S"

            if Confirmación == "S" and len(Confirmación) == 1:
                listaDeAlumnos.remove(listaDeAlumnos[modo-1])
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

listaDeAlumnos=ordenarLista(listaDeAlumnos)

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
            listaDeAlumnos=ordenarLista(listaDeAlumnos)
except KeyboardInterrupt:
    cmds("exit")