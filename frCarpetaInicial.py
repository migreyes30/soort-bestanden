#Boa:Frame:Frame2

import wx
import wx.html
import wx.lib.filebrowsebutton
import configuracion
import guardaste
import error
import errorNombreCorrecto

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BOTONDIRECTORIO, wxID_FRAME2BOTONGUARDAR, 
 wxID_FRAME2BOTONREGRESAR, wxID_FRAME2STATICBITMAP1, wxID_FRAME2STATICTEXT1, 
 wxID_FRAME2STATICTEXT2, wxID_FRAME2STATICTEXT3, wxID_FRAME2STATICTEXT4, 
 wxID_FRAME2STATICTEXT5, 
] = [wx.NewId() for _init_ctrls in range(10)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(400, 150), size=wx.Size(600, 451),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Configura la carpeta inicial')
        self.SetClientSize(wx.Size(592, 417))
        self.SetBackgroundColour(wx.Colour(235, 235, 235))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'config.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(128, 32),
              size=wx.Size(51, 47), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='Configuraci\xf3n :', name='staticText1', parent=self,
              pos=wx.Point(192, 48), size=wx.Size(159, 29), style=0)
        self.staticText1.SetFont(wx.Font(18, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME2STATICTEXT2,
              label='Escriba la ruta o seleccione la carpeta donde se encuentran los ',
              name='staticText2', parent=self, pos=wx.Point(80, 104),
              size=wx.Size(445, 19), style=0)
        self.staticText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText3 = wx.StaticText(id=wxID_FRAME2STATICTEXT3,
              label='el boton de guardar que se encuentra debajo.',
              name='staticText3', parent=self, pos=wx.Point(80, 152),
              size=wx.Size(323, 19), style=0)
        self.staticText3.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText4 = wx.StaticText(id=wxID_FRAME2STATICTEXT4,
              label='Pantalla Inicial', name='staticText4', parent=self,
              pos=wx.Point(368, 50), size=wx.Size(137, 25), style=0)
        self.staticText4.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.botonRegresar = wx.BitmapButton(bitmap=wx.Bitmap(u'regresarMenuConfig.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONREGRESAR,
              name='botonRegresar', parent=self, pos=wx.Point(16, 344),
              size=wx.Size(160, 64), style=wx.BU_AUTODRAW)
        self.botonRegresar.Bind(wx.EVT_BUTTON, self.OnBotonRegresarButton,
              id=wxID_FRAME2BOTONREGRESAR)

        self.botonGuardar = wx.BitmapButton(bitmap=wx.Bitmap(u'guardar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONGUARDAR,
              name='botonGuardar', parent=self, pos=wx.Point(400, 344),
              size=wx.Size(160, 48), style=wx.BU_AUTODRAW)
        self.botonGuardar.Bind(wx.EVT_BUTTON, self.OnBotonGuardarButton,
              id=wxID_FRAME2BOTONGUARDAR)

        self.botonDirectorio = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Examinar',
              dialogTitle='Puto', id=wxID_FRAME2BOTONDIRECTORIO,
              labelText='Selecciona un directorio', newDirectory=False,
              parent=self, pos=wx.Point(160, 208), size=wx.Size(296, 48),
              startDirectory='Puto', style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')
        self.botonDirectorio.SetName('botonDirectorio')

        self.staticText5 = wx.StaticText(id=wxID_FRAME2STATICTEXT5,
              label='archivos que desea ordenar. Una vez hecho esto has click en',
              name='staticText5', parent=self, pos=wx.Point(80, 128),
              size=wx.Size(427, 19), style=0)
        self.staticText5.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonRegresarButton(self, event):
        ventanaInicial = configuracion.create(None)
        self.Destroy()
        ventanaInicial.Show()

    def OnButton1Button(self, event):
        x = self.botonDirectorio.GetValue()
        print x

    def OnBotonGuardarButton(self, event):
        cosa = open('config.txt','r')
        x = cosa.readlines()
        direc = self.botonDirectorio.GetValue()
        
        if direc == "":
            ventanaError2 = errorNombreCorrecto.create(None)
            ventanaError2.Show()
        elif len(x) < 1:
            ruta = self.botonDirectorio.GetValue()
            ruta = "" +ruta + "\n"
            output = file("config.txt", "a")
            output.write(ruta)
            output.close()
            ventanaX = guardaste.create(None)
            ventanaX.Show()
        else:
            ventanaError = error.create(None)
            ventanaError.Show()
