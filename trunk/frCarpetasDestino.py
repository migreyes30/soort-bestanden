#Boa:Frame:Frame2

import wx
import wx.lib.stattext
import wx.lib.filebrowsebutton
import configuracion
import string
import guardaste
import error
global contador
contador = 1



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
              pos=wx.Point(400, 150), size=wx.Size(600, 450),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Selecciona las carpetas destino')
        self.SetClientSize(wx.Size(592, 416))
        self.SetBackgroundColour(wx.Colour(234, 234, 234))
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
              dialogTitle='', id=wxID_FRAME2DIRBROWSEBUTTON1,
              labelText='Directorio 1 :', newDirectory=False, parent=self,
              pos=wx.Point(16, 120), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton1.SetBackgroundColour(wx.Colour(235, 235, 235))

        self.dirBrowseButton2 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle='', id=wxID_FRAME2DIRBROWSEBUTTON2,
              labelText='Directorio 2 :', newDirectory=False, parent=self,
              pos=wx.Point(16, 176), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton2.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.dirBrowseButton2.Show(False)

        self.dirBrowseButton3 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle='', id=wxID_FRAME2DIRBROWSEBUTTON3,
              labelText='Directorio 3 :', newDirectory=False, parent=self,
              pos=wx.Point(16, 232), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton3.SetBackgroundColour(wx.Colour(234, 234, 234))
        self.dirBrowseButton3.Show(False)

        self.dirBrowseButton4 = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle='', id=wxID_FRAME2DIRBROWSEBUTTON4,
              labelText='Directorio 4 :', newDirectory=False, parent=self,
              pos=wx.Point(304, 120), size=wx.Size(264, 48), startDirectory='.',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.dirBrowseButton4.SetBackgroundColour(wx.Colour(230, 230, 230))
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

        self.button1 = wx.Button(id=wxID_FRAME2BUTTON1, label='button1',
              name='button1', parent=self, pos=wx.Point(256, 368),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME2BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonRegresarButton(self, event):
        ventanaInicial = configuracion.create(None)
        self.Destroy()
        ventanaInicial.Show()

    def OnBotonGuardarButton(self, event):
        cosa = open('config.txt','r')
        x = cosa.readlines()
        if len(x) < 2:
            listaDestino = []
            listaDestino.append(self.dirBrowseButton1.GetValue())
            listaDestino.append(self.dirBrowseButton2.GetValue())
            listaDestino.append(self.dirBrowseButton3.GetValue())
            listaDestino.append(self.dirBrowseButton4.GetValue())
            listaDestino.append(self.dirBrowseButton5.GetValue())
            listaDestino.append(self.dirBrowseButton6.GetValue())
            listaDestino = ','.join(listaDestino)
            listaDestino = "" + listaDestino + "\n"
            output = file("config.txt", "a")
            output.write(listaDestino)
            output.close()
            ventanaX = guardaste.create(None)
            ventanaX.Show()

        else:
            ventanaError = error.create(None)
            ventanaError.Show()

    def OnFrame2Close(self, event):
        self.Destroy()
        borrar = file("config.txt", "w")
        borrar.write("")
        borrar.close()
        
    def OnButton1Button(self, event):
        #contador ++
        self.dirBrowseButton5.Show(True)
        self.dirBrowseButton2.Show(True)
        self.dirBrowseButton3.Show(True)
        self.dirBrowseButton4.Show(True)
