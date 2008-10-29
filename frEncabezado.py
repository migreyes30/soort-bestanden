#Boa:Frame:Frame2

import wx
import wx.lib.filebrowsebutton
import configuracion
import guardaste
import error
import error5
import os.path

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2ARCHIVOENC, wxID_FRAME2BOTONGUARDAR, 
 wxID_FRAME2BOTONREGRESAR, wxID_FRAME2STATICBITMAP1, wxID_FRAME2STATICTEXT1, 
 wxID_FRAME2STATICTEXT2, wxID_FRAME2STATICTEXT3, wxID_FRAME2STATICTEXT4, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(400, 150), size=wx.Size(600, 450),
              style=wx.DEFAULT_FRAME_STYLE, title='Encabezado')
        self.SetClientSize(wx.Size(592, 416))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'config.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(104, 24),
              size=wx.Size(51, 47), style=0)

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label='Configuraci\xf3n :', name='staticText1', parent=self,
              pos=wx.Point(168, 32), size=wx.Size(181, 33), style=0)
        self.staticText1.SetFont(wx.Font(20, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_FRAME2STATICTEXT2,
              label='Encabezado', name='staticText2', parent=self,
              pos=wx.Point(368, 40), size=wx.Size(101, 23), style=0)
        self.staticText2.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText3 = wx.StaticText(id=wxID_FRAME2STATICTEXT3,
              label='la configuraci\xf3n de tu encabezado favorito.',
              name='staticText3', parent=self, pos=wx.Point(144, 120),
              size=wx.Size(304, 19), style=0)
        self.staticText3.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.staticText3.Center(wx.HORIZONTAL)

        self.botonGuardar = wx.BitmapButton(bitmap=wx.Bitmap(u'guardar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONGUARDAR,
              name='botonGuardar', parent=self, pos=wx.Point(416, 352),
              size=wx.Size(160, 48), style=wx.BU_AUTODRAW)
        self.botonGuardar.Bind(wx.EVT_BUTTON, self.OnBotonGuardarButton,
              id=wxID_FRAME2BOTONGUARDAR)

        self.botonRegresar = wx.BitmapButton(bitmap=wx.Bitmap(u'regresarMenuConfig.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BOTONREGRESAR,
              name='botonRegresar', parent=self, pos=wx.Point(16, 344),
              size=wx.Size(160, 64), style=wx.BU_AUTODRAW)
        self.botonRegresar.Bind(wx.EVT_BUTTON, self.OnBotonRegresarButton,
              id=wxID_FRAME2BOTONREGRESAR)

        self.archivoEnc = wx.lib.filebrowsebutton.FileBrowseButton(buttonText='Examinar',
              dialogTitle='Choose a file', fileMask='*.*',
              id=wxID_FRAME2ARCHIVOENC, initialValue='', labelText='Archivo : ',
              parent=self, pos=wx.Point(136, 184), size=wx.Size(296, 48),
              startDirectory='.', style=wx.TAB_TRAVERSAL,
              toolTip='Type filename or click browse to choose file')
        self.archivoEnc.SetLabel('Archivo :')
        self.archivoEnc.SetValue('')
        self.archivoEnc.SetName('archivoEnc')
        self.archivoEnc.SetHelpText('')

        self.staticText4 = wx.StaticText(id=wxID_FRAME2STATICTEXT4,
              label='Por favor selecciona el archivo donde tienes guardada',
              name='staticText4', parent=self, pos=wx.Point(106, 88),
              size=wx.Size(380, 19), style=0)
        self.staticText4.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))
        self.staticText4.Center(wx.HORIZONTAL)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonGuardarButton(self, event):
        cosa = open('config.txt','r')
        x = cosa.readlines()
     
        if len(x) < 4:
			temp = self.archivoEnc.GetValue().encode('utf8')
			temp2 = temp.split('\\')
			if os.path.exists(temp) and os.path.isfile(temp2[-1]):
				archivoEnc = self.archivoEnc.GetValue().encode('utf8')
				output = file("config.txt", "a")
				output.write(archivoEnc)
				output.close()
				ventanaX = guardaste.create(None)
				ventanaX.Show()
			else :
				ventanaE = error5.create(None)
				ventanaE.Show()
        else:
            ventanaError = error.create(None)
            ventanaError.Show()


    def OnBotonRegresarButton(self, event):
        ventanaInicial = configuracion.create(None)
        self.Destroy()
        ventanaInicial.Show()
