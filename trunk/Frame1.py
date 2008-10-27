#Boa:Frame:ventanita

import wx
import configuracion
import Dialogo
import frOrdenar
import frAyuda

def create(parent):
    global ventanota 
    ventanota = ventanita(parent)
    return ventanota

def matar(parent):
    borrar = file("config.txt", "w")
    borrar.write("")
    borrar.close()
    exit()

[wxID_VENTANITA, wxID_VENTANITABOTONAYUDA, wxID_VENTANITABOTONCONFIGURAR, 
 wxID_VENTANITABOTONORDENAR, wxID_VENTANITABOTONSALIR, 
] = [wx.NewId() for _init_ctrls in range(5)]

[wxID_VENTANITAARCHIVOITEMS0, wxID_VENTANITAARCHIVOITEMS1, 
] = [wx.NewId() for _init_coll_Archivo_Items in range(2)]

class ventanita(wx.Frame):
    def _init_coll_Archivo_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_VENTANITAARCHIVOITEMS0,
              kind=wx.ITEM_NORMAL, text='Archivo')
        parent.Append(help='hola', id=wxID_VENTANITAARCHIVOITEMS1,
              kind=wx.ITEM_NORMAL, text='Abrir')
        self.Bind(wx.EVT_MENU, self.OnArchivoItems1Menu,
              id=wxID_VENTANITAARCHIVOITEMS1)

    def _init_coll_barraMenu_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=wx.Menu(), title='Archivo')

    def _init_utils(self):
        # generated method, don't edit
        self.barraMenu = wx.MenuBar()
        self.barraMenu.SetBackgroundColour(wx.Colour(0, 0, 0))
        self.barraMenu.SetFont(wx.Font(8, wx.SWISS, wx.NORMAL, wx.NORMAL, False,
              'Tahoma'))
        self.barraMenu.SetAutoLayout(True)
        self.barraMenu.SetBackgroundStyle(2)
        self.barraMenu.SetExtraStyle(1)
        self.barraMenu.SetHelpText('hola')

        self.Archivo = wx.Menu(title='Archivo')

        self._init_coll_barraMenu_Menus(self.barraMenu)
        self._init_coll_Archivo_Items(self.Archivo)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_VENTANITA, name='ventanita',
              parent=prnt, pos=wx.Point(400, 150), size=wx.Size(600, 450),
              style=wx.DEFAULT_FRAME_STYLE, title='QuickOrder')
        self._init_utils()
        self.SetClientSize(wx.Size(592, 416))
        self.SetBackgroundColour(wx.Colour(226, 226, 231))
        self.SetAutoLayout(False)
        self.SetStatusBarPane(0)
        self.SetToolTipString('Organizador de archivos')
        self.SetHelpText('')
        self.SetBackgroundStyle(wx.BG_STYLE_COLOUR)
        self.SetWindowVariant(wx.WINDOW_VARIANT_NORMAL)
        self.SetIcon(wx.Icon(u'icon.ico',
              wx.BITMAP_TYPE_ICO))

        self.botonSalir = wx.BitmapButton(bitmap=wx.Bitmap(u'salir.png',
              wx.BITMAP_TYPE_PNG), id=wxID_VENTANITABOTONSALIR,
              name='botonSalir', parent=self, pos=wx.Point(160, 312),
              size=wx.Size(264, 70), style=wx.BU_AUTODRAW)
        self.botonSalir.Bind(wx.EVT_BUTTON, self.OnBotonSalirButton,
              id=wxID_VENTANITABOTONSALIR)
        self.botonSalir.Bind(wx.EVT_LEFT_DCLICK, self.OnBotonSalirLeftDclick)

        self.botonAyuda = wx.BitmapButton(bitmap=wx.Bitmap(u'imagen3.png',
              wx.BITMAP_TYPE_PNG), id=wxID_VENTANITABOTONAYUDA,
              name='botonAyuda', parent=self, pos=wx.Point(160, 216),
              size=wx.Size(264, 67), style=wx.BU_AUTODRAW)
        self.botonAyuda.Bind(wx.EVT_BUTTON, self.OnBotonAyudaButton,
              id=wxID_VENTANITABOTONAYUDA)

        self.botonOrdenar = wx.BitmapButton(bitmap=wx.Bitmap(u'ordenar1.png',
              wx.BITMAP_TYPE_PNG), id=wxID_VENTANITABOTONORDENAR,
              name='botonOrdenar', parent=self, pos=wx.Point(160, 120),
              size=wx.Size(264, 67), style=wx.BU_AUTODRAW)
        self.botonOrdenar.Bind(wx.EVT_BUTTON, self.OnBotonOrdenarButton,
              id=wxID_VENTANITABOTONORDENAR)

        self.botonConfigurar = wx.BitmapButton(bitmap=wx.Bitmap(u'configurar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_VENTANITABOTONCONFIGURAR,
              name='botonConfigurar', parent=self, pos=wx.Point(160, 24),
              size=wx.Size(264, 70), style=wx.BU_AUTODRAW)
        self.botonConfigurar.Bind(wx.EVT_BUTTON, self.OnBotonConfigurarButton,
              id=wxID_VENTANITABOTONCONFIGURAR)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonSalirButton(self, event):
        ventanaSeguro = Dialogo.create(None)
        ventanaSeguro.Show()  
        

    def OnBotonSalirLeftDclick(self, event):
        event.Skip()

    def OnBitmapButton1Button(self, event):
        event.Skip()

    def OnBotonConfigurarButton(self, event):
        ventanaConfigura = configuracion.create(None)
        self.Destroy()
        ventanaConfigura.Show()

    def OnArchivoItems1Menu(self, event):
        event.Skip()

    def OnBotonOrdenarButton(self, event):
        ventanaOrdenar = frOrdenar.create(None)
        self.Destroy()
        ventanaOrdenar.Show()

    def OnBotonAyudaButton(self, event):
        ventanaAyuda = frAyuda.create(None)
        self.Destroy()
        ventanaAyuda.Show()

        
