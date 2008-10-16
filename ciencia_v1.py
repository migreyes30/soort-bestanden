import os.path
import os

##aqui se deben insertar los metodos que utilizaremos, en orden de efectividad


## obtenidas de algun archivo de configuracion
archEncabezado = "enca.txt"
NOMBRE = "Claudia"
NOMBRE2 =  "Alicia"
APELLIDO = "Bellido"
APELLIDO2 = "García"
MATRICULA = "466914"

MESES = ['enero','febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio','agosto','septiembre','octubre','noviembre','diciembre']
EN = 0

def leerArchivo(archivo):
    
        arch = open(archivo, "r")
        archLista = arch.read()
        archLista = archLista.replace('\r\n', '\n').split('\n')
        return archLista

    
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
        return str(EN)


## Si dentro de la configuracion se introdijo
## algun encabezado predeterminado y
## el archivo lo contiene este determinara
## el nombre del archivo analizado
## recibe:
##          archAnalizar -> archivo al que se desea colocar un titulo
        
def match(archAnaliza,encabezado):
    hay = True
    for i in range(len(encabezado)):
        indice_abrir = encabezado[i].find('<!')
        indice_cerrar = encabezado[i].find('!>')
        
        if indice_abrir >= 0 and  indice_cerrar >= 0:
            if encabezado[i][(indice_abrir +2): indice_cerrar] not in archAnaliza[i]:
                return 0, False
        
        if "titulo" in encabezado[i]:
                indiceTitulo = i

    return [indiceTitulo, hay]   
                

def encabezado(archAnalizar):
    titulo = ""
    #archAnalizar = leerArchivo(archAnaliza)

    if (archEncabezado != ""):
        encabezado = leerArchivo(archEncabezado)
        indiceTitulo, hayEncabezado = match(archAnalizar,encabezado)
        if (hayEncabezado):
                
            elementoTitulo = encabezado[indiceTitulo]
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


listaComunes = ['el', 'la', 'los','las', 'un', 'unos', 'una', 'unas', 'a', 'ante', 'con',
                'contra ', 'de', 'desde', 'en', 'entre', 'hasta', 'hacia', 'hasta', 'para','por',
                'según','sobre', 'y', 'o', 'e', 'u', 'cuando', 'cuándo', 'que', 'qué', 'cada',
                'él' , 'ella', 'este', 'esta', 'éste', 'está', 'si', 'sí', 'no', 'se','me','lo', 'al', 'es', 'yo',
                'te','del','le','su','ya','me','algo','alguien','mi']

puntuacion = ['.',',',':',';','!','¡','"',"'","¿",'?','-','..','...','(',')']

def contarRepetidas(archAnalizar):
    
    #archAnalizar = leerArchivo(archAnaliza)
    
    palabrasVeces = {}
    palabras = []
     
    for x in archAnalizar:
        linea = x.split()
        for a in linea:
            a = a.strip()

            if a != "":
                if a[0] in puntuacion:
                    a = a.strip(a[0])
                if a[-1] in puntuacion:
                    a = a.strip(a[-1])
                
                if a.lower() not in listaComunes:   
                    if palabrasVeces.has_key(a):
                        palabrasVeces [a]=  palabrasVeces [a]+1
                    else:
                        palabrasVeces [a] = 1

   
    tupla = palabrasVeces.items()
    tupla.sort(key=lambda x:x[1])
    listaOrdenada = list(tupla)
    listaOrdenada = listaOrdenada[::-1]
    listaOrdenada = listaOrdenada[:5]
   
    
    for i in listaOrdenada:
        palabras.append(i[0])
    
    return palabras
    
#clave = ['es','fue', 'este', 'esta','describe', 'escribe', 'clasifica', 'aplica']

finales = ['presenta', 'trata', 'sirve', 'tiene', 'son', 'para','fue']
principios = ['el', 'la', 'los','las', 'un', 'unos', 'una', 'unas']

def oracionPrincipal(archAnalizar):
    
    #archAnalizar = leerArchivo(archAnaliza)
    
    linea = ""
    for p in archAnalizar:
        linea = linea + " " + p
        if (p.find(".")) >= 0:
            break;
        
    linea = linea[:linea.find(".")]
    for x in principios:
        if x in linea:
            desde =  linea.find(x)
            for a in finales:
                if a in linea:
                    hasta = linea.find(a)
                    titulo = linea[desde:hasta].strip()
                    print titulo
                    return titulo

    return ""


## busca titulo en la primera linea

def primeraLinea(archAnalizar):

    #archAnalizar = leerArchivo(archAnaliza)
    
    titulo = ""
    i = 0
    lineaLibre = ['\t', '\n', " ", ""]
    contEncontrado = False

    while contEncontrado == False and i < 13:
        
        contEncontrado = True

        ## checa que no sea una linea vacia.
        if archAnalizar[i] in lineaLibre:
            i = i + 1
            contEncontrado = False
            
        ## convierte el str en una lista, ejemplo: las abejas son verdes -> ['las','abejas','son','verdes']
        listaAnalizar =  str(archAnalizar[i].split())
       

        ## listaAnalizar es una lista con 1 palabra cada elemento..
        ## se volvera a analizar la misma linea porque puede que haya Claudia Bellido        Día del Trabajo
        if (NOMBRE in listaAnalizar and APELLIDO in listaAnalizar) or (MATRICULA in listaAnalizar):

                archAnalizar[i] = archAnalizar[i].replace(NOMBRE, "")
                archAnalizar[i] = archAnalizar[i].replace(APELLIDO, "")
                archAnalizar[i] = archAnalizar[i].replace(NOMBRE2, "")
                archAnalizar[i] = archAnalizar[i].replace(APELLIDO2, "")
                archAnalizar[i] = archAnalizar[i].replace(MATRICULA, "")
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
            if m.replace(",", "").replace(".", "").replace("/", "").replace("-", "").isdigit():
                archAnalizar[i] = archAnalizar[i].replace(m, "")
                contEncontrado = False
    
    if len(archAnalizar[i].strip('\t').split()) < 8  and contEncontrado == True:
        titulo = archAnalizar[i].strip()

    return titulo

metodos = [encabezado, primeraLinea, oracionPrincipal, contarRepetidas]


###########################

caracters_prohibidos = ["\\", "*", "/", "?", '"', "'", "<", ">", "|",":","."]

def ponerTitulo(archivo):
    if (os.path.exists(archivo) and  os.path.isfile(archivo)):
        titulo = seleccionarTitulo(archivo)
        ext = archivo[archivo.find("."):]
    
        
         
        
        for i in caracters_prohibidos:
            titulo = titulo.replace(i,"")
        if ext >= 0:
            os.rename(archivo, titulo+ext)
    else:
        
        print "Error, el archoivo " + archivo + " no existe."

    
    
