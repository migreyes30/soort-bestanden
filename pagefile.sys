# -*- coding: cp1252 -*-
import os.path
import os
import shutil

##aqui se deben insertar los metodos que utilizaremos, en orden de efectividad
## obtenidas de algun archivo de configuracion

################################*********************************************************################################

##archEncabezado = "enca.txt" ##****

carpetaInicio = ''
CARPETAS = {}
archEncabezado = ""
EN = 0
PALABRAS = []

################################*********************************************************################################

## Lista con los meses del año
MESES = ['enero','febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio','agosto','septiembre','octubre','noviembre','diciembre']

##**



##***


listaComunes = ['el', 'la', 'los','las', 'un', 'unos', 'una', 'unas', 'a', 'ante', 'con',
                'contra ', 'de', 'desde', 'en', 'entre', 'hasta', 'hacia', 'hasta', 'para','por',
                'según','sobre', 'y', 'o', 'e', 'u', 'cuando', 'cuándo', 'que', 'qué', 'cada',
                'él' , 'ella', 'este', 'esta', 'éste', 'está', 'si', 'sí', 'no', 'se','me','lo', 'al', 'es', 'yo',
                'te','del','le','su','ya','me','algo','alguien','mi']

puntuacion = ['.',',',':',';','!','¡','"',"'","¿",'?','-','..','...','(',')','\x08']


finales = ['presenta', 'es','trata' , 'sirve', 'tiene', 'son', 'para','fue', 'analiza', 'que', 'depende']
principios = ['el', 'la', 'los','las', 'un', 'unos', 'una', 'unas']




################################*********************************************************################################

#leerArchivo recibe el nombre del archivo que deseas leer
#lee el archivo
#regresa una lista, donde cada elemento de la lista es una linea del archivo leido
def leerArchivo(archivo):
    if (os.path.exists(archivo) and  os.path.isfile(archivo)):
        arch = open(archivo, "r")
        archLista = arch.read()
        archLista = archLista.replace('\r\n', '\n').split('\n')
        return archLista


################################*********************************************************################################

##Recibe el archivo para el cual se desea encontrar un titulo adecuado
##manda leer el archivo que enviara a los distintos metodos
##si el archivo no esta en blanco:
##        Con un for recorre la lista con los metodos para encontrar un titulo
##        recorre todos los metodos hasta que uno devuelve un titulo exitoso
##        regresa el nombre del titulo obtenido
##si el archivo esta en blanco:
##        regresa un numero por default

def seleccionarTitulo(archivo):
    global EN
    titulo = ""
    archLeido = leerArchivo(archivo)
    if archLeido !=['']:
        for i in metodos:
            titulo = i(archLeido)
            if (titulo != ""):
                return titulo
    else:
        EN = EN + 1
        modificarArchivo("EN.txt", 'EN = ' + str(EN))
        return str(EN)


################################*********************************************************################################


##Recibe una lista donde esta guarado el archivo que se desea analizar y el archivo que contiene el encabezado
##Verifica si el archivo leido contiene un formato igual
##al introducido dentro del encabezado
##regresa una lista: donde si indica en que lugar en que indice debe encontrarse el titulo,
##                   y una variable booleana que indica si el archivo analizado contiene un encabezado.

def match(archAnaliza,encabezado1):
    hay = True ## variable que indicara si el archivo contiene un encabezado

    for i in range(len(encabezado1)):
        indice_abrir = encabezado1[i].find('<!')
        indice_cerrar = encabezado1[i].find('!>')
        
        if indice_abrir >= 0 and  indice_cerrar >= 0:
            if encabezado1[i][(indice_abrir +2): indice_cerrar] not in archAnaliza[i]:
                return 0, False
        
        if "titulo" in encabezado1[i]:
                indiceTitulo = i

    return [indiceTitulo, hay]   
                

def encabezado(archAnalizar):

    titulo = ""

 
    if (archEncabezado != ""):
        encabezado1 = leerArchivo(archEncabezado)
        indiceTitulo, hayEncabezado = match(archAnalizar,encabezado1)

        if (hayEncabezado):
            elementoTitulo = encabezado[indiceTitulo] ##elementoTitulo ->  todo lo que existe en la linea desdde que se encontro la palabra titulo dentro de encabezado 
            elementoTitulo = elementoTitulo.rstrip()  
            elementoTitulo = elementoTitulo.lstrip()
            archTitulo = archAnalizar[indiceTitulo]
            
            archTitulo = archTitulo.rstrip()
            archTitulo = archTitulo.lstrip()

            if elementoTitulo.replace('titulo', "") != "":
                tituloEn = elementoTitulo.find('titulo')
                espacios_antes = elementoTitulo.count(" ",0,tituloEn)
                espacios_despues = elementoTitulo.count(" ",tituloEn)
                
                
                x = elementoTitulo.find('titulo')
                
                y =  elementoTitulo.count(" ",0,x)
                a = -1
                z =  elementoTitulo.find(" ", x)
                fin = elementoTitulo.count(" ",x)
                
                for i in range(0,y):
                    a = archTitulo.find(" ", a+1)
                    b = 0
                for i in range(0,fin):
                    b = archTitulo[::-1].find(" ", b+1)
                    
                if (len(archTitulo)-b > a+1):
                    titulo = archTitulo[a+1:(len(archTitulo) - b)]   
                else:
                    titulo = archTitulo[a+1:]

                    
            else:
                    titulo = archTitulo


    return titulo

################################*********************************************************################################


def contarRepetidas(archAnalizar):
    
    #archAnalizar = leerArchivo(archAnaliza)
    
    palabrasVeces = {}
     
    for x in archAnalizar:
        linea = x.split()
        for a in linea:
            a = a.strip()

            if a != "":
                if a[0] in puntuacion:
                    a = a.strip(a[0])
                    
                #if a[-1] in puntuacion:
                 #   a = a.strip(a[-1])
                
                if a.lower() not in listaComunes:   
                    if palabrasVeces.has_key(a):
                        palabrasVeces[a]=  palabrasVeces [a]+1
                    else:
                        palabrasVeces[a] = 1
    return palabrasVeces

def listaRepetidasOrdenad(diccionarioPalabras):
    tupla = diccionarioPalabras.items()
    tupla.sort(key=lambda x:x[1])
    listaOrdenada = list(tupla)
    listaOrdenada = listaOrdenada[::-1] ##mayor a menor
    return listaOrdenada

def listaContarRepetidas(archAnalizar):
    palabras = []
    diccionarioPalabras = contarRepetidas(archAnalizar)
    listaOrdenada = listaRepetidasOrdenada(diccionarioPalabras)
    listaOrdenada = listaOrdenada[:5]
    for i in listaOrdenada:
        palabras.append(i[0])
    
    return palabras


################################*********************************************************################################



def quitarLista(string, lista):
        for x in lista:
                string = string.replace(x, "")
        return string
                
def obtenerIndice(lista, hasta):
        indice = 0
        for x in range(hasta):
                indice = 1 + len(lista[x]) + indice

        return indice
                
def pasarListaMin(lista):
        for x in range(len(lista)):
                lista[x] = lista[x].lower()
                
        return lista
        
def oracionPrincipal(archAnalizar):
    
    contEncontrado, archAnalizar, i = quitar_Formato(archAnalizar)
    
    linea = ""
    for p in archAnalizar:
        linea = linea + " " + p
        if (p.find(".")) >= 0:
            break;

    desde = -1;
    hasta = -1;
    linea = linea[:linea.find(".")]
    linea = linea.strip().lower()

    listaLinea = quitarLista(linea, puntuacion).split()
    listaLinea = pasarListaMin(listaLinea)


    for x in principios:
            if x in listaLinea:
                    desde = obtenerIndice(listaLinea, listaLinea.index(x))
                    listaLinea2 = listaLinea[listaLinea.index(x):]
                    break;
                
    if (desde > -1):
            for x in finales:
                    if x in listaLinea2:
                            hasta = obtenerIndice(listaLinea, listaLinea.index(x))
                            return linea[desde:hasta].strip()
 

    if hasta == -1 and desde >= 0:
            hasta = len(linea)-1
            titulo = linea[desde:].strip()
            return titulo
        
    return ""


################################*********************************************************################################


## busca titulo en la primera linea

def primeraLinea(archAnalizar):

    titulo = ""
    contEncontrado, archAnalizar, i = quitar_Formato(archAnalizar)
    if len(archAnalizar[i].strip('\t').split()) < 8  and contEncontrado == True:
        titulo = archAnalizar[i].strip()

    return titulo



################################*********************************************************################################


def quitar_Formato (archAnalizar):
        i = 0
        
        contEncontrado = False
        while contEncontrado == False and i < 13:
                contEncontrado = True
        
                ## checa que no sea una linea vacia.
                if archAnalizar[i] == "":
                
                        i = i + 1
                        contEncontrado = False

                ## convierte el str en una lista, ejemplo: las abejas son verdes -> ['las','abejas','son','verdes']
                listaAnalizar =  str(archAnalizar[i].split())
       

                ## listaAnalizar es una lista con 1 palabra cada elemento..
                ## se volvera a analizar la misma linea porque puede que haya Claudia Bellido        Día del Trabajo
                for x in PALABRAS:
                        if x in listaAnalizar:
                                archAnalizar[i] = archAnalizar[i].replace(x, "")
                                contEncontrado = False
                                

                listaAnalizar =  archAnalizar[i].split()

                b = 0;
                listaAnalizar1 = []
                
                for a in listaAnalizar:
                    listaAnalizar1.append(listaAnalizar[b].lower())
                    b = b +1

                for a in MESES:   
                    if (a in listaAnalizar1):
                            

                        archAnalizar[i] = archAnalizar[i].replace(listaAnalizar[listaAnalizar1.index(a)], "")
                        contEncontrado = False
                        break
                    
                listaAnalizar =  archAnalizar[i].split()
               
                for m in listaAnalizar:
                    if m.replace(",", "").replace(".", "").replace("/", "").replace("-", "").replace("de", "").replace("del","").isdigit():
                        archAnalizar[i] = archAnalizar[i].replace(m, "")
                        contEncontrado = False
                        
        return contEncontrado, archAnalizar, i


################################*********************************************************################################


caracters_prohibidos = ["\\", "*", "/", "?", '"', "'", "<", ">", "|",":","."]


def ponerTitulo(archivo):
    global EN
    if (os.path.exists(archivo) and  os.path.isfile(archivo)):
        titulo = seleccionarTitulo(archivo)
        ext = archivo[archivo.rfind("."):]
    
        
        if not  isinstance(titulo, list):
                for i in caracters_prohibidos:
                        titulo = titulo.replace(i,"")
        else:
                titulo = str(titulo)
        print titulo
        if ext >= 0:
                if(os.path.exists(titulo+ext)):
                        os.rename(archivo, titulo+str(EN)+ext)
                        
                        EN = EN + 1
                        modificarArchivo("EN.txt", 'EN = ' + str(EN))
                else:
                        os.rename(archivo, titulo+ext)
        
    else:
        
        print "Error, el archivo " + archivo + " no existe."


################################*********************************************************################################


##CARPETAS = {}

##SRC = #.. carpeta de inicio configurada

def moverACarpeta(archAnalizar):
        dst = seleccionarCarpeta(archAnalizar)
        move(SRC, dst)

def seleccionarCarpeta(archAnalizar):#(lista_palabras)
      
        lista = contarRepetidas(leerArchivo(archAnalizar)).keys()
        CONT_CARPETAS = {}

        for m in CARPETAS:
                CONT_CARPETAS[m] = 0
                
        for a in CARPETAS:
                for y in CARPETAS[a]:
                        CONT_CARPETAS[a]= CONT_CARPETAS[a] + lista.count(y)

                        
        return max(CONT_CARPETAS)


################################*********************************************************################################

##def hacerLaMagia():
##        listaArchivos =  obtenerArchivosCaretaInicio()
##        for x in  listaArchivos:
##                leer
##                ponertitulo
##                seleccionarcarpeta
                

def hacer_la_magia():
        listaArchivos = obtenerArchivosCarpetaInicio()
        for x in listaArchivos:
                ponerTitulo(x)
                seleccionarCarpeta(x)
        




################################*********************************************************################################

permitidas = ['.txt']


def obtenerArchivosCarpetaInicio():
        archivosEnDir = os.listdir(carpetaInicio)
        listaArchivos = []
        for archivo in archivosEnDir:
                ext = archivo[archivo.rfind("."):].lower()
                if ext in permitidas:
                        listaArchivos.append(archivo)
                        
        return listaArchivos

def modificarArchivo(archivo, escribir):
        f = open(archivo, "w")
        f.write(escribir)
        

def palabrasClave():
    global PALABRAS
    x = []
    encabezado1 = leerArchivo(archEncabezado)
    for i in range(len(encabezado1)):
        indice_abrir = encabezado1[i].find('<!')
        indice_cerrar = encabezado1[i].find('!>')
        if indice_abrir >= 0 and  indice_cerrar >= 0:
                x.append(encabezado1[i][(indice_abrir +2): indice_cerrar])

    for i in x:
            for h in i.split():
                    PALABRAS.append(h)

def iniciarEN():
        global EN
        archivo = leerArchivo("EN.txt")
        indice0 = archivo[0].find("=")
        indice1 = archivo[0].find("EN")
        if indice0 > 0 and indice1 >= 0:

                EN = int(archivo[0][indice0 + 1:].strip())


def iniciarVariables():
    archivo = leerArchivo("config.txt")
    carpetaInicio = archivo[0].strip()
    archivo[1] = archivo[1].split(',')
    archivo[2] = archiv0[2].split('!!')
    for x in range(len(archivo[1])):
        CARPETAS[archivo[1][x].strip()] = archivo[2][x].strip()
    archEncabezado = archivo[3].strip()


def configurar():
        palabrasClave()
        iniciarEN()
        #iniciarVariables()
                

metodos = [encabezado, primeraLinea, oracionPrincipal, listaContarRepetidas]

configurar()
