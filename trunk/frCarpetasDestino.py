#Boa:Frame:Frame2

import wx
import wx.lib.stattext
import wx.lib.filebrowsebutton
import configuracion
import string
import guardaste
import error
import error5
import errorBrowse1
import errorBrowse2
import errorBrowse3
import errorBrowse4
import errorBrowse5
import errorBrowse6
import errorNombreCorrecto
import os.path

global contador
contador = 2



def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BOTONGUARDAR, wxID_FRAME2BOTONREGRESAR, 
 wxID_FRAME2BUTTON1, wxID_FRAME2DIRBROWSEBUTTON1, wxID_FRAME2DIRBROWSEBUTTON2, 
 wxID_FRAME2DIRBROWSEBUTTON3, wxID_FRAME2DIRBROWSEBUTTON4, 
 wxID_FRAME2DIRBROWSEBUTTON5, wxID_FRAME2DIRBROWSEBUTTON6, 
 wxID_FRAME2GENSTATICTEXT1, wxID_FRAME2GENSTATICTEXT2, 
 wxID_FRAME2STATICBITMAP1, wxID_FRAME2STATICTEXT1, wxID_FRAME2STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(15)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(430, 240), size=wx.Size(600, 450),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Selecciona las carpetas destino')
        self.SetClientSize(wx.Size(592, 416))
        self.SetBackgroundColour(wx.Colour(234, 234, 234))
        self.Enable(True)
        self.SetHelpText(u'')
        self.Bind(wx.EVT_CLOSE, self.OnFrame2Close)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'config.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(104, 16),
              size=wx.Size(51, 47), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='Configuraci\xf3n :', name='staticText1', parent=self,
              pos=wx.Point(168, 24), size=wx.Size(159, 29), style=0)
        self.staticText1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME2STATICTEXT2,
              label='Carpetas destino', name='staticText2', parent=self,
              pos=wx.Point(344, 27), size=wx.Size(156, 25), style=0)
        self.staticText2.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.dirBrowseButton1 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle=u'OK', id=wxID_FRAME2DIRBROWSEBUTTON1,
              labelText=u'Directorio 1 :', newDirectory=False, parent=self,
              pos=wx.Point(16, 120), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton1.SetBackgroundColour(wx.Colour(235, 235, 235))
        self.dirBrowseButton1.SetValue(u'')
        self.dirBrowseButton1.SetLabel(u'Directorio 1 :')
        self.dirBrowseButton1.SetToolTipString(u'dirBrowseButton1')

        self.dirBrowseButton2 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle='', id=wxID_FRAME2DIRBROWSEBUTTON2,
              labelText='Directorio 2 :', newDirectory=False, parent=self,
              pos=wx.Point(16, 176), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton2.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.dirBrowseButton2.SetValue(u'')
        self.dirBrowseButton2.Show(False)

        self.dirBrowseButton3 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle='', id=wxID_FRAME2DIRBROWSEBUTTON3,
              labelText='Directorio 3 :', newDirectory=False, parent=self,
              pos=wx.Point(16, 232), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton3.SetBackgroundColour(wx.Colour(234, 234, 234))
        self.dirBrowseButton3.SetValue(u'')
        self.dirBrowseButton3.Show(False)

        self.dirBrowseButton4 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle='', id=wxID_FRAME2DIRBROWSEBUTTON4,
              labelText='Directorio 4 :', newDirectory=False, parent=self,
              pos=wx.Point(304, 120), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton4.SetBackgroundColour(wx.Colour(230, 230, 230))
        self.dirBrowseButton4.SetValue(u'')
        self.dirBrowseButton4.Show(False)

        self.dirBrowseButton5 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle='', id=wxID_FRAME2DIRBROWSEBUTTON5,
              labelText='Directorio 5:', newDirectory=False, parent=self,
              pos=wx.Point(304, 176), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton5.SetBackgroundColour(wx.Colour(234, 234, 234))
        self.dirBrowseButton5.Show(False)

        self.dirBrowseButton6 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle='', id=wxID_FRAME2DIRBROWSEBUTTON6,
              labelText='Directorio 6 :', newDirectory=False, parent=self,
              pos=wx.Point(304, 232), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton6.SetBackgroundColour(wx.Colour(233, 233, 233))
        self.dirBrowseButton6.SetValue(u'')
        self.dirBrowseButton6.Show(False)

        self.genStaticText1 = wx.lib.stattext.GenStaticText(ID=wxID_FRAME2GENSTATICTEXT1,
              label='desees que se ordenen los archivos. Puedes escoger hasta 6 directorios diferentes.',
              name='genStaticText1', parent=self, pos=wx.Point(24, 96),
              size=wx.Size(544, 18), style=0)
        self.genStaticText1.Center(wx.HORIZONTAL)
        self.genStaticText1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.genStaticText1.SetBackgroundColour(wx.Colour(239, 239, 239))

        self.botonRegresar = wx.BitmapButton(bitmap=wx.Bitmap(u'regresarMenuConfig.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONREGRESAR,
              name='botonRegresar', parent=self, pos=wx.Point(16, 336),
              size=wx.Size(160, 64), style=wx.BU_AUTODRAW)
        self.botonRegresar.Bind(wx.EVT_BUTTON, self.OnBotonRegresarButton,
              id=wxID_FRAME2BOTONREGRESAR)

        self.botonGuardar = wx.BitmapButton(bitmap=wx.Bitmap(u'guardar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONGUARDAR,
              name='botonGuardar', parent=self, pos=wx.Point(400, 350),
              size=wx.Size(160, 48), style=wx.BU_AUTODRAW)
        self.botonGuardar.Enable(True)
        self.botonGuardar.Bind(wx.EVT_BUTTON, self.OnBotonGuardarButton,
              id=wxID_FRAME2BOTONGUARDAR)

        self.genStaticText2 = wx.lib.stattext.GenStaticText(ID=wxID_FRAME2GENSTATICTEXT1,
              label='Escriba la ruta o haz clic en examninar para seleccionar los directorios donde',
              name='genStaticText2', parent=self, pos=wx.Point(48, 72),
              size=wx.Size(495, 18), style=0)
        self.genStaticText2.Center(wx.HORIZONTAL)
        self.genStaticText2.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.genStaticText2.SetBackgroundColour(wx.Colour(238, 238, 238))

        self.button1 = wx.Button(id=wxID_FRAME2BUTTON1,
              label=u'Carpetas Extras', name='button1', parent=self,
              pos=wx.Point(248, 360), size=wx.Size(88, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME2BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonRegresarButton(self, event):
        global contador
        contador = 2
        ventanaInicial = configuracion.create(None)
        self.Destroy()
        ventanaInicial.Show()

    def OnBotonGuardarButton(self, event):
        global contador
        cosa = open('config.txt','r')
        x = cosa.readlines()
        if len(x) < 2:
            
            if contador == 7 and (self.dirBrowseButton6.GetValue()  == "" or self.dirBrowseButton1.GetValue() == "" or self.dirBrowseButton2.GetValue()  == "" or self.dirBrowseButton3.GetValue()  == "" or self.dirBrowseButton4.GetValue()  == "" or self.dirBrowseButton5.GetValue()  == ""):
                ventanaError1 = error5.create(None)
                ventanaError1.Show()
            else:
                dictBrowse = {"errorBrowse1": errorBrowse1.create(None),
                              "errorBrowse2": errorBrowse2.create(None),
                              "errorBrowse3": errorBrowse3.create(None),
                              "errorBrowse4": errorBrowse4.create(None),
                              "errorBrowse5": errorBrowse5.create(None),
                              "errorBrowse6": errorBrowse6.create(None)}
                ventanaBadPath = None
                listaDestino = []
                listaDestino.append(self.dirBrowseButton1.GetValue())
                listaDestino.append(self.dirBrowseButton2.GetValue())
                listaDestino.append(self.dirBrowseButton3.GetValue())
                listaDestino.append(self.dirBrowseButton4.GetValue())
                listaDestino.append(self.dirBrowseButton5.GetValue())
                listaDestino.append(self.dirBrowseButton6.GetValue())
                listaDestino = ','.join(listaDestino)
                listaDestino = listaDestino.encode('utf8')
                listaDest = listaDestino.split(",")
                listErrorBrowse = []
                temp = contador-1
                
                for i in xrange(temp):
                    if os.path.exists(listaDest[i]) == False and os.path.isdir(listaDest[i]) == False:
                        listErrorBrowse.append("errorBrowse"+str(i+1))

                if len(listErrorBrowse) == 0:
                    output = file("config.txt", "a")
                    output.write(listaDestino)
                    output.write("\n")
                    output.close()
                    ventanaX = guardaste.create(None)
                    ventanaX.Show()
                    self.button1.Show(False)
                    self.dirBrowseButton1.Enable(False)
                    self.dirBrowseButton2.Enable(False)
                    self.dirBrowseButton3.Enable(False)
                    self.dirBrowseButton4.Enable(False)
                    self.dirBrowseButton5.Enable(False)
                    self.dirBrowseButton6.Enable(False)
                    
                else:
                    for i in listErrorBrowse:
                        mensajeError = dictBrowse[i]
                        mensajeError.Show()
                    

        else:
            ventanaError = error.create(None)
            ventanaError.Show()

    def OnFrame2Close(self, event):
        self.Destroy()
        borrar = file("config.txt", "w")
        borrar.write("")
        borrar.close()
        
    def OnButton1Button(self, event):
	    global contador
	    ventanaError0 = error5.create(None)
	    alreadyShow = True
   
	    if contador == 2 and self.dirBrowseButton1.GetValue() != "":
		    self.dirBrowseButton2.Show(True)
		    contador = contador +1
		    alreadyShow = False
	    elif alreadyShow == True and self.dirBrowseButton1.GetValue()  == "":
	        ventanaError0.Show()
	        alreadyShow = False
		    
	    if contador == 3 and self.dirBrowseButton1.GetValue() != "" and self.dirBrowseButton2.GetValue()  != "":
		    self.dirBrowseButton3.Show(True)
		    contador = contador +1
		    alreadyShow = False
	    elif alreadyShow == True and self.dirBrowseButton2.GetValue()  == "" :
	        ventanaError0.Show()
	        alreadyShow = False
		    
	    if contador == 4 and self.dirBrowseButton1.GetValue() != "" and self.dirBrowseButton2.GetValue()  != "" and self.dirBrowseButton3.GetValue()  != "":
		    self.dirBrowseButton4.Show(True)
		    contador = contador +1
		    alreadyShow = False
	    elif alreadyShow == True and self.dirBrowseButton3.GetValue()  == "":
	        ventanaError0.Show()
	        alreadyShow = False
		    
	    if contador == 5 and self.dirBrowseButton1.GetValue() != "" and self.dirBrowseButton2.GetValue()  != "" and self.dirBrowseButton3.GetValue()  != "" and self.dirBrowseButton4.GetValue()  != "":
		    self.dirBrowseButton5.Show(True)
		    contador = contador +1
		    alreadyShow = False
	    elif alreadyShow == True and self.dirBrowseButton4.GetValue()  == "":
	        ventanaError0.Show()
	        alreadyShow = False  
		    
	    if contador == 6 and self.dirBrowseButton1.GetValue() != "" and self.dirBrowseButton2.GetValue()  != "" and self.dirBrowseButton3.GetValue()  != "" and self.dirBrowseButton4.GetValue()  != "" and self.dirBrowseButton5.GetValue()  != "":
		    self.dirBrowseButton6.Show(True)
		    self.button1.Show(False)
		    contador = contador +1
		    alreadyShow = False
	    elif alreadyShow == True and self.dirBrowseButton5.GetValue()  == "":
	        ventanaError0.Show()
	        alreadyShow = False
