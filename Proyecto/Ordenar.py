# -*- coding: utf-8 -*-



class Ordenar:
    
    def __init__ (self, encArc, arcAnalizado, metodo, repetidas):
       if metodo == 0:
           self.encabezado(encArc,arcAnalizado)
       if metodo == 1:
           self.primeraLinea(encArc, arcAnalizado)
       if metodo == 2:
           self.oracionPrincipal(encArc, arcAnalizado)
       if metodo == 3:
           self.listaContarRepetidas(repetidas)
        
         
    
        
### *** POR ENCABEZADO *** ###        
    def encabezado(self, encArc, arcAnalizado):
        
        enc,indiceTitulo = self.hayEnc(encArc, arcAnalizado)
        titulo = ''
        
        if enc:

           encTitulo = encArc[indiceTitulo]
           encTitulo = self.stripLinea(encTitulo)
           
           arcTitulo = arcAnalizado[indiceTitulo]
           arcTitulo = self.stripLinea(arcTitulo)
           
           if encTitulo.replace('titulo', '') == "":
               titulo = arcTitulo
           
           else:
               titulo = self.stripTitulo(encTitulo, arcTitulo)
        print titulo
        return titulo

                
    ##Verifica que los elementos "obligatorios" que se encuentran entre <! y !>
    ## se encuentren en el archivo analizado, si es asì regresa True
    ## y ademas la posicion en que se encuentra el titulo
    def hayEnc(self, encArc,archAnalizado):
            indiceTitulo = -1
            hay = True
            
            for i in range(len(encArc)):
                abrir = encArc[i].find('<!')
                cerrar = encArc[i].find('!>')

                if abrir >= 0 and cerrar >= 0:
                    if encabezado1[i][(abrir +2): cerrar] not in archAnaliza[i]:
                        hay = False
                        break

                if "titulo" in encArc[i]:
                    indiceTitulo = i
                    
            return hay,indiceTitulo
            
    ##Regresa el titulo considerando lo que puede haber otras cosas ademas
    ##del titulo en una misma linea
    def stripTitulo(self, encTitulo, arcTitulo):
        titulo = ''
        
        x = encTitulo.find('titulo')  ## indice del titulo
        y =  encTitulo.count(" ",0,x) ## espacions antes
        fin = encTitulo.count(" ",x)  ## esapacios despues
     
        a = -1
        b = 0
       
        for i in range(0,y):
            a = arcTitulo.find(" ", a+1)
           
        for i in range(0,fin):
            b = arcTitulo[::-1].find(" ", b+1)
           
            
        if (len(arcTitulo)-b > a+1):
            titulo = arcTitulo[a+1:(len(arcTitulo) - b)]
        else:
            titulo = arcTitulo[a+1:]
        
        return titulo


### *** Primera linea *** ###
    def primeraLinea(encArch,archAnalizar):

        titulo = ""
        contEncontrado, archAnalizar, i = quitar_Formato(encArch, archAnalizar)
        if len(archAnalizar[i].strip('\t').split()) < 8  and contEncontrado == True:
            titulo = archAnalizar[i].strip()

        return titulo
    
    def quitarFormato(encArch, archAnalizar):
        
        listaConst = encabezadoConstantes(encArch)
        i = 0        
        contEncontrado = False
        meses = ['enero','febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio','agosto','septiembre','octubre','noviembre','diciembre']
        

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
                for x in listaConst:
                        if x in listaAnalizar:
                                archAnalizar[i] = archAnalizar[i].replace(x, "")
                                contEncontrado = False
                                

                listaAnalizar =  archAnalizar[i].split()
                b = 0;
                listaAnalizar1 = []
                
                for a in listaAnalizar:
                    listaAnalizar1.append(listaAnalizar[b].lower())
                    b = b +1

                for a in meses:   
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

        def encabezadoConstantes(encArc):
        
        for i in range(len(encArc)):
            abrir = encArc[i].find('<!')
            cerrar = encArc[i].find('!>')
            if abrir >= 0 and cerrar >= 0:
                listaConst = listaConst + [encArc[abrir+2:cerrar]]

                                           
        
###########################################


## se obtienen un titulo a partir de la oración principal


## quita strings de cada elemento de una lista
def quitarLista(string, lista):
        for x in lista:
                try:
                    string = string.replace(x, "")
                except UnicodeDecodeError:
                    pass
                
        return string


    ## Funcion que integra todo para obtener el titulo a partie de la oracion principal
    def oracionPrincipal(archAnalizar):
        puntuacion = ['.',',',':',';','!','¡','"',"'","¿",'?','-','..','...','(',')','\x08','\t']
        principios = ['el', 'la', 'los','las', 'un', 'unos', 'una', 'unas']
        finales = ['presenta', 'es','trata' , 'sirve', 'tiene', 'son', 'para','fue', 'analiza', 'que', 'depende']
        
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

        linea = quitarLista(linea, puntuacion).lower()
        listaLinea = linea.split()
        
        for x in principios:
                if x in listaLinea:
                        desde = linea.index(x)
                        listaLinea2 = listaLinea[listaLinea.index(x):]
                        break;
                    
        if (desde > -1):
                for x in finales:
                        if x in listaLinea2:
                                hasta = linea.index(x,desde)
                                return linea[desde:hasta].strip()
     

        if hasta == -1 and desde >= 0:
                titulo = linea[desde:].strip()
                return titulo
            
        return ""

    def listaRepetidasOrdenad(diccionarioPalabras):
        tupla = diccionarioPalabras.items()
        tupla.sort(key=lambda x:x[1])
        listaOrdenada = list(tupla)
        listaOrdenada = listaOrdenada[::-1] ##mayor a menor
        return listaOrdenada
    
###################
## crea un diccionario donde cuenta cuantas veces se repiten las palabras
    def listaContarRepetidas(repetidas):
        palabras = []
        diccionarioPalabras = repetidas
        listaOrdenada = listaRepetidasOrdenada(diccionarioPalabras)
        listaOrdenada = listaOrdenada[:5]
        for i in listaOrdenada:
            palabras.append(i[0])
        
        return palabras
    
    def listaRepetidasOrdenad(diccionarioPalabras):
        tupla = diccionarioPalabras.items()
        tupla.sort(key=lambda x:x[1])
        listaOrdenada = list(tupla)
        listaOrdenada = listaOrdenada[::-1] ##mayor a menor
        return listaOrdenada

#########
    
    def stripLinea(self, linea):
        linea = linea.rstrip()
        linea = linea.lstrip()
        return linea

