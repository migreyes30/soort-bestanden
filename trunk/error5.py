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
              pos=wx.Point(534, 316), size=wx.Size(414, 162),
              style=wx.DEFAULT_DIALOG_STYLE, title='Errocampos vacios')
        self.SetClientSize(wx.Size(406, 128))

        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR,
              label=u'Aceptar', name=u'botonAceptar', parent=self,
              pos=wx.Point(168, 88), size=wx.Size(75, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnButtonAceptarButton,
              id=wxID_DIALOG1BOTONACEPTAR)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label=u'Debes llenar todos los campos', name='staticText1',
              parent=self, pos=wx.Point(96, 32), size=wx.Size(299, 23),
              style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'error.png',
              wx.BITMAP_TYPE_PNG), id=wxID_DIALOG1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(24, 24),
              size=wx.Size(48, 48), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButtonAceptarButton(self, event):
        self.Destroy()
