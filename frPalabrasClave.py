#Boa:Frame:Frame2

import wx
import configuracion
import guardaste
import error
import error5
from types import *

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BOTONGUARDAR, wxID_FRAME2BOTONREGRESAR, 
 wxID_FRAME2DIR1, wxID_FRAME2DIR2, wxID_FRAME2DIR3, wxID_FRAME2DIR4, 
 wxID_FRAME2DIR5, wxID_FRAME2DIR6, wxID_FRAME2ETIQUETADIR1, 
 wxID_FRAME2ETIQUETADIR2, wxID_FRAME2ETIQUETADIR3, wxID_FRAME2ETIQUETADIR4, 
 wxID_FRAME2ETIQUETADIR5, wxID_FRAME2ETIQUETADIR6, wxID_FRAME2STATICBITMAP1, 
 wxID_FRAME2STATICBOX1, wxID_FRAME2STATICTEXT1, wxID_FRAME2STATICTEXT2, 
 wxID_FRAME2STATICTEXT3, wxID_FRAME2STATICTEXT4, 
] = [wx.NewId() for _init_ctrls in range(21)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(400, 150), size=wx.Size(600, 450),
              style=wx.DEFAULT_FRAME_STYLE, title='Palabras clave')
        self.SetClientSize(wx.Size(592, 416))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.SetIcon(wx.Icon(u'icon.ico',wx.BITMAP_TYPE_ICO))
        self.Bind(wx.EVT_ACTIVATE, self.OnFrame2Activate)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'config.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(112, 16),
              size=wx.Size(51, 47), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='Configuraci\xf3n :', name='staticText1', parent=self,
              pos=wx.Point(176, 24), size=wx.Size(181, 33), style=0)
        self.staticText1.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME2STATICTEXT2,
              label='Palabras clave', name='staticText2', parent=self,
              pos=wx.Point(368, 32), size=wx.Size(133, 25), style=0)
        self.staticText2.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME2STATICBOX1,
              label='Palabras Clave :', name='staticBox1', parent=self,
              pos=wx.Point(28, 112), size=wx.Size(536, 240), style=0)
        self.staticBox1.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.staticBox1.Center(wx.HORIZONTAL)

        self.etiquetaDir1 = wx.StaticText(id=wxID_FRAME2ETIQUETADIR1, label='',
              name='etiquetaDir1', parent=self, pos=wx.Point(50, 144),
              size=wx.Size(0, 13), style=0)
        self.etiquetaDir1.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.etiquetaDir2 = wx.StaticText(id=wxID_FRAME2ETIQUETADIR2, label='',
              name='etiquetaDir2', parent=self, pos=wx.Point(50, 176),
              size=wx.Size(0, 13), style=0)
        self.etiquetaDir2.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.etiquetaDir3 = wx.StaticText(id=wxID_FRAME2ETIQUETADIR3, label='',
              name='etiquetaDir3', parent=self, pos=wx.Point(50, 208),
              size=wx.Size(0, 13), style=0)
        self.etiquetaDir3.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.etiquetaDir4 = wx.StaticText(id=wxID_FRAME2ETIQUETADIR4, label='',
              name='etiquetaDir4', parent=self, pos=wx.Point(50, 240),
              size=wx.Size(0, 13), style=0)
        self.etiquetaDir4.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.etiquetaDir5 = wx.StaticText(id=wxID_FRAME2ETIQUETADIR5, label='',
              name='etiquetaDir5', parent=self, pos=wx.Point(50, 272),
              size=wx.Size(0, 13), style=0)
        self.etiquetaDir5.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.etiquetaDir6 = wx.StaticText(id=wxID_FRAME2ETIQUETADIR6, label='',
              name='etiquetaDir6', parent=self, pos=wx.Point(50, 304),
              size=wx.Size(0, 13), style=0)
        self.etiquetaDir6.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.dir1 = wx.TextCtrl(id=wxID_FRAME2DIR1, name='dir1', parent=self,
              pos=wx.Point(392, 144), size=wx.Size(160, 21), style=0, value='')
        self.dir1.Show(True)
        self.dir1.Show(False)
        self.dir1.SetValue('$')

        self.dir2 = wx.TextCtrl(id=wxID_FRAME2DIR2, name='dir2', parent=self,
              pos=wx.Point(392, 176), size=wx.Size(160, 21), style=0, value='')
        self.dir2.Show(True)
        self.dir2.Show(False)
        self.dir2.SetValue('$')

        self.dir3 = wx.TextCtrl(id=wxID_FRAME2DIR3, name='dir3', parent=self,
              pos=wx.Point(392, 208), size=wx.Size(160, 21), style=0, value='')
        self.dir3.Show(True)
        self.dir3.Show(False)
        self.dir3.SetValue('$')

        self.dir4 = wx.TextCtrl(id=wxID_FRAME2DIR4, name='dir4', parent=self,
              pos=wx.Point(392, 240), size=wx.Size(160, 21), style=0, value='')
        self.dir4.Show(True)
        self.dir4.Show(False)
        self.dir4.SetValue('$')

        self.dir5 = wx.TextCtrl(id=wxID_FRAME2DIR5, name='dir5', parent=self,
              pos=wx.Point(392, 272), size=wx.Size(160, 21), style=0, value='')
        self.dir5.Show(True)
        self.dir5.Show(False)
        self.dir5.SetValue('$')

        self.dir6 = wx.TextCtrl(id=wxID_FRAME2DIR6, name='dir6', parent=self,
              pos=wx.Point(392, 304), size=wx.Size(160, 21), style=0, value='')
        self.dir6.Show(True)
        self.dir6.Show(False)
        self.dir6.SetValue('$')

        self.staticText3 = wx.StaticText(id=wxID_FRAME2STATICTEXT3,
              label='para cada uno de los directorios que escogiste.',
              name='staticText3', parent=self, pos=wx.Point(136, 88),
              size=wx.Size(331, 19), style=0)
        self.staticText3.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.botonGuardar = wx.BitmapButton(bitmap=wx.Bitmap(u'guardar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONGUARDAR,
              name='botonGuardar', parent=self, pos=wx.Point(400, 360),
              size=wx.Size(160, 48), style=wx.BU_AUTODRAW)
        self.botonGuardar.Bind(wx.EVT_BUTTON, self.OnBotonGuardarButton,
              id=wxID_FRAME2BOTONGUARDAR)

        self.botonRegresar = wx.BitmapButton(bitmap=wx.Bitmap(u'regresarMenuConfig.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONREGRESAR,
              name='botonRegresar', parent=self, pos=wx.Point(8, 352),
              size=wx.Size(160, 64), style=wx.BU_AUTODRAW)
        self.botonRegresar.Bind(wx.EVT_BUTTON, self.OnBotonRegresarButton,
              id=wxID_FRAME2BOTONREGRESAR)

        self.staticText4 = wx.StaticText(id=wxID_FRAME2STATICTEXT4,
              label='Inserta las palabras clave, separadas por coma ,',
              name='staticText4', parent=self, pos=wx.Point(136, 64),
              size=wx.Size(339, 19), style=0)
        self.staticText4.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonRegresarButton(self, event):
        ventanaInicial = configuracion.create(None)
        self.Destroy()
        ventanaInicial.Show()

    def OnFrame2Activate(self, event):
        file=open('config.txt','r')
        listaEtiquetas = [] 
        listaEtiquetas.append(self.etiquetaDir1)
        listaEtiquetas.append(self.etiquetaDir2)
        listaEtiquetas.append(self.etiquetaDir3)
        listaEtiquetas.append(self.etiquetaDir4)
        listaEtiquetas.append(self.etiquetaDir5)
        listaEtiquetas.append(self.etiquetaDir6)
        temp = ''
        listaDirectorios =[]
        x =file.readlines()
        temp = x[1]
        # Obtiene el nombre de los directorios destino para ponerlos en las etiquetas.
        listaDirectorios = temp.split(',')
        for i in range(len(listaDirectorios)):
            listaEtiquetas[i].SetLabel(listaDirectorios[i])
        file.close()
        
        
    def OnBotonGuardarButton(self, event):
        cosa = open('config.txt','r')
        x = cosa.readlines()
        # Para comprobar si ya se han guardado palabras antes.
        if len(x) < 3:
    #-------- Creamos una lista para cada grupo de palabras clave. -------
            listaDir1 = []
            listaDir2 = []
            listaDir3 = []
            listaDir4 = []
            listaDir5 = []
            listaDir6 = []
    #--------- Aqui obtenemos las palabras clave que el usuario ingresa. ---------
            palabras1 = self.dir1.GetValue().encode('utf8')
            palabras2 = self.dir2.GetValue().encode('utf8')
            palabras3 = self.dir3.GetValue().encode('utf8')
            palabras4 = self.dir4.GetValue().encode('utf8')
            palabras5 = self.dir5.GetValue().encode('utf8')
            palabras6 = self.dir6.GetValue().encode('utf8')
	    
            listaDir1 = palabras1[0:len(palabras1)].split(',')
            listaDir2 = palabras2[0:len(palabras2)].split(',')
            listaDir3 = palabras3[0:len(palabras3)].split(',')
            listaDir4 = palabras4[0:len(palabras4)].split(',')
            listaDir5 = palabras5[0:len(palabras5)].split(',')
            listaDir6 = palabras6[0:len(palabras6)].split(',')
            

            
#----------- Las palabras de cada carpeta son separadas por !! ---------
            
            if listaDir1[0] == '' or listaDir2[0] == '' or listaDir3[0] == '' or listaDir4[0] == '' or listaDir5[0] == '' or listaDir6[0] == '':
                ventanaErrorW = error5.create(None)
                ventanaErrorW.Show()
            
            else:
                if listaDir1[0] == '$':
                    listaDir1[0] = ''
                if listaDir2[0] == '$':
                    listaDir2[0] = ''
                if listaDir3[0] == '$':
                    listaDir3[0] = ''
                if listaDir4[0] == '$':
                    listaDir4[0] = ''
                if listaDir5[0] == '$':
                    listaDir5[0] = ''
                if listaDir6[0] == '$':
                    listaDir6[0] = ''
                palabras = ','.join(listaDir1) + "!!" + ','.join(listaDir2) + "!!" + ','.join(listaDir3) + "!!" + ','.join(listaDir4) + "!!" +','.join(listaDir5) + "!!" + ','.join(listaDir6) + "\n"
                output = file("config.txt", "a")
                output.write("")
                output.write(palabras)
                output.close()
                ventanaX = guardaste.create(None)
                ventanaX.Show()
                self.dir1.Enable(False)
                self.dir2.Enable(False)
                self.dir3.Enable(False)
                self.dir4.Enable(False)
                self.dir5.Enable(False)
                self.dir6.Enable(False)

        else:
            ventanaError = error.create(None)
            ventanaError.Show()
