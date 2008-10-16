#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BOTONACEPTAR, wxID_DIALOG1STATICBITMAP1, 
 wxID_DIALOG1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(448, 273), size=wx.Size(478, 141),
              style=wx.DEFAULT_DIALOG_STYLE, title='Error')
        self.SetClientSize(wx.Size(470, 107))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'error.png',
              wx.BITMAP_TYPE_PNG), id=wxID_DIALOG1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(8, 16),
              size=wx.Size(48, 48), style=0)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='Primero debes de elegir las opciones anteriores.',
              name='staticText1', parent=self, pos=wx.Point(64, 32),
              size=wx.Size(393, 19), style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR,
              label='Aceptar', name='botonAceptar', parent=self,
              pos=wx.Point(184, 72), size=wx.Size(112, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton,
              id=wxID_DIALOG1BOTONACEPTAR)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonAceptarButton(self, event):
        self.Destroy()
