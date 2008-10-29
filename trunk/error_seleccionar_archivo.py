#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BOTONACEPTAR, wxID_DIALOG1STATICBITMAP1, 
 wxID_DIALOG1STATICTEXT1, wxID_DIALOG1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(490, 300), size=wx.Size(369, 144),
              style=wx.DEFAULT_DIALOG_STYLE, title='\xa1 Error !')
        self.SetClientSize(wx.Size(361, 110))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='para poder leerlo.', name='staticText1', parent=self,
              pos=wx.Point(80, 40), size=wx.Size(146, 19), style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label='Debes seleccionar un archivo', name='staticText2',
              parent=self, pos=wx.Point(80, 16), size=wx.Size(235, 19),
              style=0)
        self.staticText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR,
              label='Aceptar', name='botonAceptar', parent=self,
              pos=wx.Point(128, 72), size=wx.Size(104, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton,
              id=wxID_DIALOG1BOTONACEPTAR)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'error.png',
              wx.BITMAP_TYPE_PNG), id=wxID_DIALOG1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(16, 24),
              size=wx.Size(48, 48), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonAceptarButton(self, event):
        self.Destroy()
