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
              pos=wx.Point(494, 286), size=wx.Size(388, 135),
              style=wx.DEFAULT_DIALOG_STYLE, title='Felicidades')
        self.SetClientSize(wx.Size(380, 101))

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label='borrado satisfactoriamente.', name='staticText2',
              parent=self, pos=wx.Point(88, 40), size=wx.Size(227, 19),
              style=0)
        self.staticText2.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR,
              label='Aceptar', name='botonAceptar', parent=self,
              pos=wx.Point(144, 72), size=wx.Size(96, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton,
              id=wxID_DIALOG1BOTONACEPTAR)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'carita.png',
              wx.BITMAP_TYPE_PNG), id=wxID_DIALOG1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(16, 16),
              size=wx.Size(64, 64), style=0)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='El archivo de configuraci\xf3n ha sido',
              name='staticText1', parent=self, pos=wx.Point(88, 16),
              size=wx.Size(281, 19), style=0)
        self.staticText1.SetFont(wx.Font(12, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonAceptarButton(self, event):
        self.Destroy()
