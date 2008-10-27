#Boa:Frame:Frame2

import wx
import Frame1

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BITMAPBUTTON1, wxID_FRAME2STATICBITMAP1, 
 wxID_FRAME2STATICTEXT1, wxID_FRAME2STATICTEXT2, wxID_FRAME2STATICTEXT3, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(406, 150), size=wx.Size(600, 450),
              style=wx.DEFAULT_FRAME_STYLE, title='Ayuda')
        self.SetClientSize(wx.Size(592, 416))
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetIcon(wx.Icon(u'icon.ico',
              wx.BITMAP_TYPE_ICO))

        self.staticText1 = wx.StaticText(id=wxID_FRAME2STATICTEXT1,
              label=' que tengas del uso del programa.', name='staticText1',
              parent=self, pos=wx.Point(120, 184), size=wx.Size(324, 25),
              style=0)
        self.staticText1.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.Bitmap(u'regresar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BITMAPBUTTON1,
              name='bitmapButton1', parent=self, pos=wx.Point(8, 336),
              size=wx.Size(168, 64), style=wx.BU_AUTODRAW)
        self.bitmapButton1.Bind(wx.EVT_BUTTON, self.OnBitmapButton1Button,
              id=wxID_FRAME2BITMAPBUTTON1)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'imagen3.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(192, 24),
              size=wx.Size(200, 60), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME2STATICTEXT2,
              label='En la carpeta del programa podras encontrar un archivo de',
              name='staticText2', parent=self, pos=wx.Point(24, 120),
              size=wx.Size(559, 25), style=0)
        self.staticText2.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText3 = wx.StaticText(id=wxID_FRAME2STATICTEXT3,
              label='ayuda en donde podras consultar las dudas',
              name='staticText3', parent=self, pos=wx.Point(96, 152),
              size=wx.Size(408, 25), style=0)
        self.staticText3.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBitmapButton1Button(self, event):
        ventanaInicial = Frame1.create(None)
        self.Destroy()
        ventanaInicial.Show()

