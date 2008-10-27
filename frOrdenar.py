#Boa:Frame:Frame2

import wx
import ciencia_revis
import Frame1
import frOrdenaPrimero
import ordenado
import configuracion

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BOTONCONFIGURAR, wxID_FRAME2BOTONORDENAR, 
 wxID_FRAME2BOTONREGRESAR, wxID_FRAME2STATICBITMAP1, wxID_FRAME2STATICTEXT1, 
 wxID_FRAME2STATICTEXT2, wxID_FRAME2STATICTEXT3, wxID_FRAME2STATICTEXT4, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(400, 150), size=wx.Size(600, 450),
              style=wx.DEFAULT_FRAME_STYLE, title='Ordenador de archivos')
        self.SetClientSize(wx.Size(592, 416))
        self.SetBackgroundColour(wx.Colour(225, 225, 225))
        self.SetIcon(wx.Icon(u'icon.ico',
              wx.BITMAP_TYPE_ICO))

        self.staticText2 = wx.StaticText(id=wxID_FRAME2STATICTEXT2,
              label='has click en el boton de abajo para iniciar el ordenamiento.',
              name='staticText2', parent=self, pos=wx.Point(40, 112),
              size=wx.Size(497, 23), style=0)
        self.staticText2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText3 = wx.StaticText(id=wxID_FRAME2STATICTEXT3,
              label='Si has realizado la configuracion y todo esta bien,',
              name='staticText3', parent=self, pos=wx.Point(80, 80),
              size=wx.Size(415, 23), style=0)
        self.staticText3.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.botonOrdenar = wx.BitmapButton(bitmap=wx.Bitmap(u'ordenar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONORDENAR,
              name='botonOrdenar', parent=self, pos=wx.Point(152, 168),
              size=wx.Size(256, 80), style=wx.BU_AUTODRAW)
        self.botonOrdenar.Bind(wx.EVT_BUTTON, self.OnBotonOrdenarButton,
              id=wxID_FRAME2BOTONORDENAR)

        self.botonRegresar = wx.BitmapButton(bitmap=wx.Bitmap(u'regresar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONREGRESAR,
              name='botonRegresar', parent=self, pos=wx.Point(24, 344),
              size=wx.Size(160, 64), style=wx.BU_AUTODRAW)
        self.botonRegresar.Bind(wx.EVT_BUTTON, self.OnBotonRegresarButton,
              id=wxID_FRAME2BOTONREGRESAR)

        self.staticText4 = wx.StaticText(id=wxID_FRAME2STATICTEXT4,
              label='\xbfOlvidaste realizar la configuraci\xf3n?',
              name='staticText4', parent=self, pos=wx.Point(352, 304),
              size=wx.Size(233, 16), style=0)
        self.staticText4.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.botonConfigurar = wx.BitmapButton(bitmap=wx.Bitmap(u'configurarChiquito.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONCONFIGURAR,
              name='botonConfigurar', parent=self, pos=wx.Point(424, 328),
              size=wx.Size(107, 74), style=wx.BU_AUTODRAW)
        self.botonConfigurar.Bind(wx.EVT_BUTTON, self.OnBotonConfigurarButton,
              id=wxID_FRAME2BOTONCONFIGURAR)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'ordenarArchivos.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(120, 32),
              size=wx.Size(356, 24), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='Nota : Esta acci\xf3n es irreversible.',
              name='staticText1', parent=self, pos=wx.Point(152, 264),
              size=wx.Size(272, 19), style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonOrdenarButton(self, event):    
        archivo = file("config.txt", "r")
        x = archivo.read()
        print x
        if x != "":
            ventanaX = ordenado.create(None)
            ventanaX.Show()
            ciencia_revis.configurar()
            ciencia_revis.hacer_la_magia()

        else:
                ventanaError = frOrdenaPrimero.create(None)
                ventanaError.Show()
    

    def OnBotonRegresarButton(self, event):
        ventanaInicial = Frame1.create(None)
        self.Destroy()
        ventanaInicial.Show()

    def OnBotonConfigurarButton(self, event):
        self.Destroy()
        ventanaConfig = configuracion.create(None)
        ventanaConfig.Show()
