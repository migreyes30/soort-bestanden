# -*- coding: cp1252 -*-
import os.path
import os
import shutil
import win32com.client

## aqui se deben insertar los metodos que utilizaremos, en orden de efectividad
## obtenidas de algun archivo de configuracion

################################*********************************************************################################

#archEncabezado = "enca.txt"
## Variables que se configuran al incio por el usuario, a expecion de EN
## PALABRAS se obtiene del encabezado y son palabras que se podr�an encontrar en el encabezado aunque se cuente con encabezdo
## EN es un contador que se configura con el archivo que se encuentre en la variable reporteEn

carpetaInicio = ''
CARPETAS = {}
archEncabezado = ""
EN = 0
PALABRAS = []
REPORTE = 0
listaRepetidasOrdenada = []

reporteEn = "EN.txt"

################################*********************************************************################################

## Listas con palabras clave y puntuacion


MESES = ['enero','febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio','agosto','septiembre','octubre','noviembre','diciembre']


listaComunes = ['el', 'la', 'los','las', 'un', 'unos', 'una', 'unas', 'a', 'ante', 'con',
                'contra ', 'de', 'desde', 'en', 'entre', 'hasta', 'hacia', 'hasta', 'para','por',
                'seg�n','sobre', 'y', 'o', 'e', 'u', 'cuando', 'cu�ndo', 'que', 'qu�', 'cada',
                '�l' , 'ella', 'este', 'esta', '�ste', 'est�', 'si', 's�', 'no', 'se','me','lo', 'al', 'es', 'yo',
                'te','del','le','su','ya','me','algo','alguien','mi','tu']

puntuacion = ['.',',',':',';','!','�','"',"'","�",'?','-','..','...','(',')','\x08','\t']


finales = ['presenta', 'es','trata' , 'sirve', 'tiene', 'son', 'para','fue', 'analiza', 'que', 'depende', 'conocida', 'fue']
principios = ['el', 'la', 'los','las', 'un', 'unos', 'una', 'unas']




################################*********************************************************################################

#leerArchivo recibe el nombre del archivo que deseas leer
#lee el archivo
#regresa una lista, donde cada elemento de la lista es una linea del archivo leido
#lee documentos .txt
def leerArchivoTxt(archivo):
    if (os.path.exists(archivo) and  os.path.isfile(archivo)):
        arch = open(archivo, "r")
        archLista = arch.read()
        archLista = archLista.replace('\r\n', '\n').split('\n')
        arch.close()
        return archLista
    
#leerArchivoDoc recibe el nombre del archivo que deseas leer
#lee el archivo
#regresa una lista, donde cada elemento de la lista es una linea del archivo leido
#s�lo lee documentos .doc
def leerArchivoDoc(archivo):
    word= win32com.client.Dispatch('Word.Application')
    word.Documents.Open(archivo)
    text=word.ActiveDocument.Content.Text
    word.Visible = 0
    word.Documents.Close()
    return text.replace('\x0b', '\r').split('\r')
    
def leerArchivoExcel(archivo):
    lista = []
    excel = win32com.client.Dispatch("Excel.Application")
    texto = excel.Workbooks.Open(archivo)
    excel.Visible = 0
    for i in range(1,20):
        hola =""
        for j in range(1,20):
            if str(texto.ActiveSheet.Cells(i,j).Value) != 'None':
                lista.append(str(texto.ActiveSheet.Cells(i,j).Value))
    excel.Workbooks.Close()
    return lista

def leerArchivoPpt(archivo):
    ppt = win32com.client.DispatchEx("Powerpoint.Application")
    ppt.Visible=1
    text = ppt.Presentations.Open('G:\hola.ppt',False,False)
    
#*********************************************************#

#   Recibe el archivo para el cual se desea encontrar un titulo adecuado
#   manda leer el archivo que enviara a los distintos metodos
#   si el archivo no esta en blanco:
#        Con un for recorre la lista con los metodos para encontrar un titulo
#        recorre todos los metodos hasta que uno devuelve un titulo exitoso
#       regresa el nombre del titulo obtenido
#   si el archivo esta en blanco:
#       regresa un numero por default

def seleccionarTitulo(archivo, ext):
    global EN
    titulo = ""
    #print archivo, ext
    if ext == '.txt':
        archLeido = leerArchivoTxt(archivo)
    elif ext == '.doc':
        archLeido = leerArchivoDoc(archivo)
    elif ext == '.xls':
        archLeido = leerArchivoExcel(archivo)
    else:
        EN = EN + 1
        modificarArchivo(rerporteEn, 'EN = ' + str(EN))
        return str(EN)
        
 
    if archLeido !=['']:
        for i in metodos:
            #print archLeido, "dsffddfsd"
            titulo = i(archLeido)
            if (titulo != ""):
                #print titulo
                return titulo
    else:
        EN = EN + 1
        modificarArchivo(reporteEn, 'EN = ' + str(EN))
        return str(EN)


################################*********************************************************################################


##Recibe una lista donde esta guarado el archivo que se desea analizar y la lista que contiene el encabezado
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

## encabezado
## Recibe el archivo que se quiere analizar
## De haber encontrada un t�tulo regresa el t�tulo corresponidente, de lo contrario regresa ""
def encabezado(archAnalizar):

    titulo = ""

 
    if (archEncabezado != ""):
        encabezado1 = leerArchivoTxt(archEncabezado)
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

## Cuenta las palabras significativas que m�s se repiten
## La lista de comunes son palabras que no deben tomarse en cuenta, al igual que la lista PALABRAS
## Regresa una lista con 5 palabras que se repitieron constamenente en el documento
## La funci�n se dividio en tres metodos para poder rehusar el codigo en otras secciones

def contarRepetidas(archAnalizar):
    
    #archAnalizar = leerArchivoTxt(archAnaliza)
    global EN
    palabrasVeces = {}
    #print archAnalizar
    try: 
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
    except TypeError:
        EN = EN + 1
        modificarArchivo(reporteEn, 'EN = ' + str(EN))
        return str(EN)
         
    
    return palabrasVeces


## regresa la lista con las keys ordenadas de mayor a menor
def listaRepetidasOrdenad(diccionarioPalabras):
    tupla = diccionarioPalabras.items()
    tupla.sort(key=lambda x:x[1])
    listaOrdenada = list(tupla)
    listaOrdenada = listaOrdenada[::-1] ##mayor a menor
    return listaOrdenada

## crea un diccionario donde cuenta cuantas veces se repiten las palabras
def listaContarRepetidas(archAnalizar):
    palabras = []
    diccionarioPalabras = contarRepetidas(archAnalizar)
    listaOrdenada = listaRepetidasOrdenada(diccionarioPalabras)
    listaOrdenada = listaOrdenada[:5]
    for i in listaOrdenada:
        palabras.append(i[0])
    
    return palabras


################################*********************************************************################################

## se obtienen un titulo a partir de la oraci�n principal


## quita strings de cada elemento de una lista
def quitarLista(string, lista):
        for x in lista:
                try:
                    string = string.replace(x, "")
                except UnicodeDecodeError:
                    pass
                
        return string

## parecido a index de strings
## regresa un indice
def obtenerIndice(lista, hasta):
        indice = 0
        for x in range(hasta):
                indice = 1 + len(lista[x]) + indice

        return indice

## pasa todos los elementos a minuscula   
def pasarListaMin(lista):
        for x in range(len(lista)):
                lista[x] = lista[x].lower()
                
        return lista

## Funcion que integra todo para obtener el titulo a partie de la oracion principal
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

## Auxiliar de primeraLinea y oracion principal
## Quita elementos de la lista PALABRAS, asi como la fecha

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
                ## se volvera a analizar la misma linea porque puede que haya Claudia Bellido        D�a del Trabajo
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

## Caracteres que no pueden estar en el nombre de un archivo
caracters_prohibidos = ["\\", "*", "/", "?", '"', "'", "<", ">", "|",":",".", "\x01"]


## Ejecuta las funciones necesarias para obtener un titulo y renombra el archivo con el titulo obtenido

def ponerTitulo(archivo):
    global EN
    if (os.path.exists(archivo) and  os.path.isfile(archivo)):
        ext = archivo[archivo.rfind("."):]
        
        titulo = seleccionarTitulo(archivo, ext)
        
    
        if not  isinstance(titulo, list):
                for i in caracters_prohibidos:
                        titulo = titulo.replace(i,"")
        else:
                titulo = str(titulo)
        if ext >= 0:
                if(os.path.exists(titulo+ext)):
                        #print archivo[:archivo.rfind("\\") + 1] + titulo+ext, "RUTA"
                        os.rename(archivo,  archivo[:archivo.rfind("\\") + 1] + titulo+str(EN)+ext)
                       # print archivo, titulo +ext
                        
                        EN = EN + 1
                        modificarArchivo("reporteEn", 'EN = ' + str(EN))
                else:
                        #print archivo[:archivo.rfind("\\") + 1] + titulo+ext,"RUTA"
                        os.rename(archivo, archivo[:archivo.rfind("\\") + 1] + titulo+ext)
        
    else:
        print "Error, el archivo " + archivo + " no existe."


################################*********************************************************################################


## Mueve a la carpeta correcta
def moverACarpeta(archAnalizar):
        
        if archAnalizar != "":
            dst = seleccionarCarpeta(archAnalizar)
            if dst != "":
                shutil.move(archAnalizar, dst)
                escribirDatos(archAnalizar + "  ->  " + dst + "\n")

## selecciona la carpeta a partir de diccionarios
def leerComo (archAnalizar):
    ext = archAnalizar.split('.')[1]
    if ext == 'doc':
        return leerArchivoDoc(archAnalizar)
    elif ext == 'txt':
        return leerArchivoTxt(archAnalizar)
    elif ext == 'xls':
        #print "Leer archivo excel"
        return leerArchivoExcel(archAnalizar)
    else:
        return ""
def seleccionarCarpeta(archAnalizar):#(lista_palabras)
                #print archAnalizar, "este es el arch que analizara"
                global CARPETAS
                #print "seleccionar"
                if CARPETAS.has_key(''):
                    del CARPETAS['']
                lista = contarRepetidas(leerComo(archAnalizar))
                #print lista, "estas son las palabras que mas se repitieron"
                CONT_CARPETAS = {}
                #print "CARPETAS : ",CARPETAS
                for m in CARPETAS:
                        CONT_CARPETAS[m] = 0
                #print "cont_carpetas : ",CONT_CARPETAS
                for a in CARPETAS:
                        for y in CARPETAS[a]:
                            if isinstance(lista, str) == False:
                                if lista.has_key(y):
                                    CONT_CARPETAS[a]= CONT_CARPETAS[a] + lista[y]
                maxi = 0
                llave_max = ""
                for x in CONT_CARPETAS:
                    if CONT_CARPETAS[x] > maxi:
                        maxi = CONT_CARPETAS[x]
                        llave_max = x 
                #print "Cont_carpetas : ",cont_Carpetas         
                #print "CARPETAS : ",CARPETAS
                return llave_max



################################*********************************************************################################
                

## se mandan llamar las funciones necesarias para cambiar de nombre y carpeta a todos los archivos con extensi�n admitida por el software
## Genera el reportre
def hacer_la_magia():
    global REPORTE
    global carpetaInicio
    listaArchivos = obtenerArchivosCarpetaInicio()
    #print listaArchivos, 'listaarch'
    for x in listaArchivos:
        ##print x, 'archivo'
        if x != "" and x != None:
            # print x, "archivo en hacer la magia"
            ponerTitulo(x)
            moverACarpeta(x)
    REPORTE = REPORTE + 1
    modificarArchivo("reporteEn", "REPORTE = " + str(REPORTE))



################################*********************************************************################################

permitidas = ['.txt', '.doc','.xls']

## Obtiene los archivos con extension permitidos  los regresa en una lista
def obtenerArchivosCarpetaInicio():
    global carpetaInicio
    archivosEnDir = os.listdir(carpetaInicio)
    #print archivosEnDir
    listaArchivos = []
    for archivo in archivosEnDir:
        try:
            ext = archivo[archivo.rfind("."):].lower()
            if ext in permitidas:
                listaArchivos.append(carpetaInicio + "\\" +  archivo)
        except:
            pass    
                       
    return listaArchivos

def escribirDatos(escribir):
    f = open("Reporte" + str(REPORTE), "a")
    f.write(escribir + '\n')
    f.close()

def modificarArchivo(archivo, escribir):
        contenido = leerArchivoTxt(archivo)
        f = file(archivo, "w")
        f.write("")
        f.close()
        f = file(archivo, "a")
        if (escribir.startswith("EN")):
            f.write(escribir + '\n')
            f.write(contenido[1])
        if (escribir.startswith("REPORTE")):
            f.write(contenido[0] + '\n')
            f.write(escribir)
        f.close()
            
        

def palabrasClave():
    global PALABRAS
    x = []
    if archEncabezado != "":
         encabezado1 = leerArchivoTxt(archEncabezado)
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
        archivo = leerArchivoTxt(reporteEn)
        indice0 = archivo[0].find("=")
        indice1 = archivo[0].find("EN")
        if indice0 > 0 and indice1 >= 0:
                EN = int(archivo[0][indice0 + 1:].strip())
        indice0 = archivo[1].find("=")
        indice1 = archivo[1].find("REPORTE")
        if indice0 > 0 and indice1 >= 0:
                REPORTE = int(archivo[1][indice0 + 1:].strip())


def iniciarVariables():
    global carpetaInicio
    global CARPETAS
    global archEncabezado
    archivo = leerArchivoTxt("config.txt")

    carpetaInicio = archivo[0].strip()
    
     ### agregar if por si no hay configuracion..
    archivo[1] = archivo[1].split(',')

    #archivo
    archivo[2] = archivo[2].split('!!')
    
    for x in range(len(archivo[2])):
        archivo[2][x] = archivo[2][x].split(',')
        
    for x in range(len(archivo[2])):
          for y in range(len(archivo[2][x])):
               archivo[2][x][y] = archivo[2][x][y].strip()
    # len(archivo[2]), len(archivo[1])
    
    for x in range(len(archivo[1])):
        CARPETAS[archivo[1][x].strip()] = archivo[2][x]
    #print CARPETAS, "ESTA ES LA CARPETA"
    try:
        archEncabezado = archivo[3].strip()
    except: pass


def configurar():
        iniciarEN()
        iniciarVariables()
        palabrasClave()
                

metodos = [encabezado, primeraLinea, oracionPrincipal, listaContarRepetidas]

