#Boa:Frame:Frame2

import wx
import wx.lib.filebrowsebutton
import Frame1
import frCarpetaInicial
import frCarpetasDestino
import frPalabrasClave
import frEncabezado
import shutil
import completado
import borrado
import error_seleccionar_archivo
import error_escribir_nombre
import error
import error2
import error3
import error4
import errorYaHasConfigurado

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2ARCHIVOEXPO, wxID_FRAME2ARCHIVOIMPO, 
 wxID_FRAME2BOTONDESTINO, wxID_FRAME2BOTONENCABEZADO, 
 wxID_FRAME2BOTONEXPORTAR, wxID_FRAME2BOTONIMPORTAR, wxID_FRAME2BOTONINICIAL1, 
 wxID_FRAME2BOTONPALABRAS, wxID_FRAME2BOTONREGRESAR, 
 wxID_FRAME2BOTONREINICIAR, wxID_FRAME2CAJITA, wxID_FRAME2CONFIGURACION, 
 wxID_FRAME2ETIQUETAINFO, wxID_FRAME2ETIQUETAINFO2, wxID_FRAME2ETIQUETAINFO3, 
 wxID_FRAME2ETIQUETAINFO4, wxID_FRAME2ETIQUETAINFO5, wxID_FRAME2PANEL1, 
 wxID_FRAME2STATICBITMAP1, wxID_FRAME2STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(21)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(400, 150), size=wx.Size(600, 450),
              style=wx.DEFAULT_FRAME_STYLE, title='Configuraci\xf3n')
        self.SetClientSize(wx.Size(592, 416))
        self.SetBackgroundColour(wx.Colour(238, 238, 238))
        self.Bind(wx.EVT_CLOSE, self.OnFrame2Close)

        self.Configuracion = wx.StaticText(id=wxID_FRAME2CONFIGURACION,
              label='C o n f i g u r a c i \xf3 n', name='Configuracion',
              parent=self, pos=wx.Point(232, 24), size=wx.Size(205, 23),
              style=0)
        self.Configuracion.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'config.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(168, 8),
              size=wx.Size(51, 47), style=0)

        self.botonRegresar = wx.BitmapButton(bitmap=wx.Bitmap(u'regresar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONREGRESAR,
              name='botonRegresar', parent=self, pos=wx.Point(24, 344),
              size=wx.Size(165, 64), style=wx.BU_AUTODRAW)
        self.botonRegresar.Bind(wx.EVT_BUTTON, self.OnBotonRegresarButton,
              id=wxID_FRAME2BOTONREGRESAR)
        self.botonRegresar.Bind(wx.EVT_ENTER_WINDOW,
              self.OnBotonRegresarEnterWindow)

        self.cajita = wx.StaticBox(id=wxID_FRAME2CAJITA, label='Informaci\xf3n',
              name='cajita', parent=self, pos=wx.Point(272, 96),
              size=wx.Size(296, 128), style=0)
        self.cajita.SetBackgroundColour(wx.Colour(240, 240, 240))

        self.etiquetaInfo2 = wx.StaticText(id=wxID_FRAME2ETIQUETAINFO2,
              label='Para que veas la informacion de cada punto desplegada',
              name='etiquetaInfo2', parent=self, pos=wx.Point(288, 136),
              size=wx.Size(268, 13), style=0)

        self.etiquetaInfo = wx.StaticText(id=wxID_FRAME2ETIQUETAINFO,
              label='Pon el puntero sobre alguno de los botones',
              name='etiquetaInfo', parent=self, pos=wx.Point(288, 120),
              size=wx.Size(208, 13), style=0)

        self.etiquetaInfo3 = wx.StaticText(id=wxID_FRAME2ETIQUETAINFO3,
              label='dentro de esta caja de informacion.', name='etiquetaInfo3',
              parent=self, pos=wx.Point(288, 152), size=wx.Size(171, 13),
              style=0)

        self.etiquetaInfo4 = wx.StaticText(id=wxID_FRAME2ETIQUETAINFO4,
              label='Cualquier otra duda la podras consultar en el boton',
              name='etiquetaInfo4', parent=self, pos=wx.Point(288, 168),
              size=wx.Size(246, 13), style=0)

        self.etiquetaInfo5 = wx.StaticText(id=wxID_FRAME2ETIQUETAINFO5,
              label='de ayuda dentro del menu inicial.', name='etiquetaInfo5',
              parent=self, pos=wx.Point(288, 184), size=wx.Size(158, 13),
              style=0)

        self.archivoImpo = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Examinar',
              dialogTitle='Choose a file', fileMask='*.*',
              id=wxID_FRAME2ARCHIVOIMPO, initialValue='',
              labelText='File Entry:', parent=self, pos=wx.Point(232, 312),
              size=wx.Size(200, 48), startDirectory='configuraciones',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.archivoImpo.SetLabel('')
        self.archivoImpo.SetValue('')
        self.archivoImpo.SetHelpText('')
        self.archivoImpo.SetName('archivoImpo')

        self.botonImportar = wx.Button(id=wxID_FRAME2BOTONIMPORTAR,
              label='Leer configuraci\xf3n', name='botonImportar', parent=self,
              pos=wx.Point(448, 325), size=wx.Size(128, 29), style=0)
        self.botonImportar.SetBackgroundColour(wx.Colour(207, 207, 207))
        self.botonImportar.Bind(wx.EVT_BUTTON, self.OnBotonImportarButton,
              id=wxID_FRAME2BOTONIMPORTAR)
        self.botonImportar.Bind(wx.EVT_ENTER_WINDOW,
              self.OnBotonImportarEnterWindow)

        self.botonExportar = wx.Button(id=wxID_FRAME2BOTONEXPORTAR,
              label='Guardar configuraci\xf3n', name='botonExportar',
              parent=self, pos=wx.Point(448, 368), size=wx.Size(128, 28),
              style=0)
        self.botonExportar.SetBackgroundColour(wx.Colour(210, 210, 210))
        self.botonExportar.Bind(wx.EVT_ENTER_WINDOW,
              self.OnBotonExportarEnterWindow)
        self.botonExportar.Bind(wx.EVT_BUTTON, self.OnBotonExportarButton,
              id=wxID_FRAME2BOTONEXPORTAR)

        self.archivoExpo = wx.TextCtrl(id=wxID_FRAME2ARCHIVOEXPO,
              name='archivoExpo', parent=self, pos=wx.Point(272, 376),
              size=wx.Size(140, 21), style=0, value='')

        self.botonReiniciar = wx.Button(id=wxID_FRAME2BOTONREINICIAR,
              label='Borrar configuraci\xf3n', name='botonReiniciar',
              parent=self, pos=wx.Point(448, 280), size=wx.Size(128, 31),
              style=0)
        self.botonReiniciar.SetBackgroundColour(wx.Colour(212, 212, 212))
        self.botonReiniciar.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.botonReiniciar.Bind(wx.EVT_BUTTON, self.OnBotonReiniciarButton,
              id=wxID_FRAME2BOTONREINICIAR)
        self.botonReiniciar.Bind(wx.EVT_ENTER_WINDOW,
              self.OnBotonReiniciarEnterWindow)

        self.panel1 = wx.Panel(id=wxID_FRAME2PANEL1, name='panel1', parent=self,
              pos=wx.Point(232, 248), size=wx.Size(352, 160),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBackgroundColour(wx.Colour(229, 229, 229))

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='Opciones del archivo de configuraci\xf3n.',
              name='staticText1', parent=self.panel1, pos=wx.Point(56, 8),
              size=wx.Size(215, 13), style=0)
        self.staticText1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.BOLD, False,
              'Tahoma'))

        self.botonInicial1 = wx.BitmapButton(bitmap=wx.Bitmap(u'botonInicialpng.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONINICIAL1,
              name='botonInicial1', parent=self, pos=wx.Point(16, 72),
              size=wx.Size(208, 56), style=wx.BU_AUTODRAW)
        self.botonInicial1.Bind(wx.EVT_BUTTON, self.OnBotonInicial1Button,
              id=wxID_FRAME2BOTONINICIAL1)
        self.botonInicial1.Bind(wx.EVT_ENTER_WINDOW,
              self.OnBotonInicial1EnterWindow)

        self.botonDestino = wx.BitmapButton(bitmap=wx.Bitmap(u'botonDestino.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONDESTINO,
              name='botonDestino', parent=self, pos=wx.Point(16, 136),
              size=wx.Size(208, 56), style=wx.BU_AUTODRAW)
        self.botonDestino.Bind(wx.EVT_BUTTON, self.OnBotonDestinoButton,
              id=wxID_FRAME2BOTONDESTINO)
        self.botonDestino.Bind(wx.EVT_ENTER_WINDOW,
              self.OnBotonDestinoEnterWindow)

        self.botonPalabras = wx.BitmapButton(bitmap=wx.Bitmap(u'botonPalabras.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONPALABRAS,
              name='botonPalabras', parent=self, pos=wx.Point(16, 200),
              size=wx.Size(208, 56), style=wx.BU_AUTODRAW)
        self.botonPalabras.Bind(wx.EVT_BUTTON, self.OnBotonPalabrasButton,
              id=wxID_FRAME2BOTONPALABRAS)
        self.botonPalabras.Bind(wx.EVT_ENTER_WINDOW,
              self.OnBotonPalabrasEnterWindow)

        self.botonEncabezado = wx.BitmapButton(bitmap=wx.Bitmap(u'botonEncabezado.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONENCABEZADO,
              name='botonEncabezado', parent=self, pos=wx.Point(16, 264),
              size=wx.Size(208, 56), style=wx.BU_AUTODRAW)
        self.botonEncabezado.Bind(wx.EVT_BUTTON, self.OnBotonEncabezadoButton,
              id=wxID_FRAME2BOTONENCABEZADO)
        self.botonEncabezado.Bind(wx.EVT_ENTER_WINDOW,
              self.OnBotonEncabezadoEnterWindow)

    def __init__(self, parent): # Inicia el constructor
        self._init_ctrls(parent)


#           ----- BOTONES DE CONFIGURACION ---------- 

    # El archivo de configuracion se conforma de la siguiente manera :
    # config[0] = Carpeta inicial
    # config[1] = Carpetas destino
    # config[2] = Palabras clave
    # config[3] = Encabezado
    
    def OnBotonInicial1Button(self, event):
        cosa = open('config.txt','r')
        x = cosa.readlines()
        if len(x) > 0 : # Para el caso en el que ya se haya configurado la carpeta inicial
            ventanaErrorYaHasConfigurado = errorYaHasConfigurado.create(None)
            ventanaErrorYaHasConfigurado.Show()
        else:
            ventanaCarpetaInicial = frCarpetaInicial.create(None)
            self.Destroy()
            ventanaCarpetaInicial.Show()
        cosa.close()
        
    def OnBotonDestinoButton(self, event):
        cosa = open('config.txt','r')
        x = cosa.readlines()
        if len(x) > 1 : # Para el caso en el que ya se haya configurado las carpetas destino
            ventanaErrorYaHasConfigurado = errorYaHasConfigurado.create(None)
            ventanaErrorYaHasConfigurado.Show()
            
        elif len(x) == 0 : # Para el caso en el que aun no se haya configurado la opcion anterior
            ventanaError2 = error2.create(None)
            ventanaError2.Show()
            
        else:
            ventanaCarpetaDestino = frCarpetasDestino.create(None)
            self.Destroy()
            ventanaCarpetaDestino.Show()
        cosa.close()

    def OnBotonPalabrasButton(self, event):
        cosa = open('config.txt','r')
        x = cosa.readlines()
        if len(x) > 2 : # Para el caso en el que ya se haya configurado las palabras clave
            ventanaErrorYaHasConfigurado = errorYaHasConfigurado.create(None)
            ventanaErrorYaHasConfigurado.Show()
            
        elif len(x) < 2 : # Para el caso en el que aun no se haya configurado la opcion anterior
            ventanaError3 = error3.create(None)
            ventanaError3.Show()
            
        else:
            ventanaPalabrasClave = frPalabrasClave.create(None)
            self.Destroy()
            ventanaPalabrasClave.Show()
        cosa.close()
            
    def OnBotonEncabezadoButton(self, event):
        cosa = open('config.txt','r')
        x = cosa.readlines()
        if len(x) == 3 :
            ventanaEncabezado = frEncabezado.create(None)
            self.Destroy()
            ventanaEncabezado.Show()
        else:
            ventanaError4 = error4.create(None)
            ventanaError4.Show()
        cosa.close()

#      ------ TERMINAN BOTONES DE CONFIGURACION -----------

    def OnBotonDestinoEnterWindow(self, event):
        self.etiquetaInfo.SetLabel("")
        self.etiquetaInfo2.SetLabel("")
        self.etiquetaInfo3.SetLabel("")
        self.etiquetaInfo4.SetLabel("")
        self.etiquetaInfo5.SetLabel("")
        self.etiquetaInfo.SetLabel("Las carpetas destino son aquellas en donde se van a ")
        self.etiquetaInfo2.SetLabel("ordenar los archivos de acuerdo a palabras clave")
        self.etiquetaInfo3.SetLabel("que puedes insertar en la siguiente opcion.")
        self.etiquetaInfo4.SetLabel("ordenar los archivos de acuerdo a palabras clave")

    def OnBotonPalabrasEnterWindow(self, event):
        self.etiquetaInfo.SetLabel("")
        self.etiquetaInfo2.SetLabel("")
        self.etiquetaInfo3.SetLabel("")
        self.etiquetaInfo4.SetLabel("")
        self.etiquetaInfo5.SetLabel("")
        self.etiquetaInfo.SetLabel("Las palabras clave son aquellas que pueden encontrarse")
        self.etiquetaInfo2.SetLabel("frecuentemente en alguna carpeta. Sirven para colocar")
        self.etiquetaInfo3.SetLabel("los archivos en la carpeta correcta. Cada carpeta tiene")
        self.etiquetaInfo4.SetLabel("su grupo de palabras clave.Mas palabras significa mayor")
        self.etiquetaInfo5.SetLabel("probabilidad de exito.")
        

    def OnBotonEncabezadoEnterWindow(self, event):
        self.etiquetaInfo.SetLabel("")
        self.etiquetaInfo2.SetLabel("")
        self.etiquetaInfo3.SetLabel("")
        self.etiquetaInfo4.SetLabel("")
        self.etiquetaInfo5.SetLabel("")
        self.etiquetaInfo.SetLabel("Aqui va lo del encabezado")
        self.etiquetaInfo2.SetLabel("Blah bla")
        
    def OnBotonImportarEnterWindow(self, event):
        self.etiquetaInfo.SetLabel("")
        self.etiquetaInfo2.SetLabel("")
        self.etiquetaInfo3.SetLabel("")
        self.etiquetaInfo4.SetLabel("")
        self.etiquetaInfo5.SetLabel("")
        self.etiquetaInfo.SetLabel("Aqui puedes leer alguna otra configuracion")
        self.etiquetaInfo2.SetLabel("que hayas realizado anteriormente.")
        self.etiquetaInfo3.SetLabel("Por ejemplo : miconfiguracionAnterior.txt")

    def OnBotonExportarEnterWindow(self, event):
        self.etiquetaInfo.SetLabel("")
        self.etiquetaInfo2.SetLabel("")
        self.etiquetaInfo3.SetLabel("")
        self.etiquetaInfo4.SetLabel("")
        self.etiquetaInfo5.SetLabel("")
        self.etiquetaInfo.SetLabel("Aqui puedes guardar la configuracion que acabas de ")
        self.etiquetaInfo2.SetLabel("realizar para que despues puedas volver a utilizarla.")
        self.etiquetaInfo3.SetLabel("Escribe el nombre en la caja de texto que ves de lado")
        self.etiquetaInfo4.SetLabel("izquierdo. (Por ejemplo : miconfiguracion.txt)")
        self.etiquetaInfo5.SetLabel("NOTA: Tiene que ser un archivo .txt")
 


    def OnBotonRegresarButton(self, event):
        ventanaInicial = Frame1.create(None)
        self.Destroy()
        ventanaInicial.Show()


    def OnFrame2Close(self, event):
        self.Destroy()
        borrar = file("config.txt", "w")
        borrar.write("")
        borrar.close()


    def OnBotonImportarButton(self, event):
        nombre = self.archivoImpo.GetValue()
        if (nombre != ""):
        #nombre = "configuraciones\\" + nombre
            shutil.copyfile(nombre,"config.txt")
            ventanaAviso = completado.create(None)
            ventanaAviso.Show()
        else:
            ventanaError = error_seleccionar_archivo.create(None)
            ventanaError.Show()
        


    def OnBotonExportarButton(self, event):
        nombreArchivo= self.archivoExpo.GetValue()
        if nombreArchivo != "":
            rutaConfig = "configuraciones\\"
            nombre = rutaConfig +  nombreArchivo
            shutil.copyfile("config.txt", nombre)
            ventanaAviso = completado.create(None)
            ventanaAviso.Show()
        else:
            ventanaError1 = error_escribir_nombre.create(None)
            ventanaError1.Show()

    def OnBotonReiniciarButton(self, event):
        borrar = file("config.txt", "w")
        borrar.write("")
        borrar.close()
        ventanaBorrado = borrado.create(None)
        ventanaBorrado.Show()

    def OnBotonReiniciarEnterWindow(self, event):
        self.etiquetaInfo.SetLabel("")
        self.etiquetaInfo2.SetLabel("")
        self.etiquetaInfo3.SetLabel("")
        self.etiquetaInfo4.SetLabel("")
        self.etiquetaInfo5.SetLabel("")
        self.etiquetaInfo.SetLabel("Aqui puedes borrar la ultima configuracion")
        self.etiquetaInfo2.SetLabel("que hayas creado anteriormente para poder")
        self.etiquetaInfo3.SetLabel("hacer una nueva.")
        
    def OnBotonInicial1EnterWindow(self, event):
        self.etiquetaInfo.SetLabel("")
        self.etiquetaInfo2.SetLabel("")
        self.etiquetaInfo3.SetLabel("")
        self.etiquetaInfo4.SetLabel("")
        self.etiquetaInfo5.SetLabel("")
        self.etiquetaInfo.SetLabel("La carpeta inicial es aquella donde tienes ")
        self.etiquetaInfo2.SetLabel("tus archivos desordenados y que desees que")
        self.etiquetaInfo3.SetLabel("sean ordenados.(ej. C:\mis documentos)")

    def OnBotonRegresarEnterWindow(self, event):
        self.etiquetaInfo.SetLabel("")
        self.etiquetaInfo2.SetLabel("")
        self.etiquetaInfo3.SetLabel("")
        self.etiquetaInfo4.SetLabel("")
        self.etiquetaInfo5.SetLabel("")
        self.etiquetaInfo.SetLabel("Regresa al menu principal. ")
        self.etiquetaInfo2.SetLabel("")
        self.etiquetaInfo3.SetLabel("")

