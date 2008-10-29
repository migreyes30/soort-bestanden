#Boa:Dialog:asd

import wx

def create(parent):
    return asd(parent)

[wxID_ASD, wxID_ASDBOTONACEPTAR, wxID_ASDSTATICBITMAP1, wxID_ASDSTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class asd(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ASD, name='asd', parent=prnt,
              pos=wx.Point(500, 290), size=wx.Size(398, 141),
              style=wx.DEFAULT_DIALOG_STYLE, title='Felicidades')
        self.SetClientSize(wx.Size(390, 107))

        self.staticText1 = wx.StaticText(id=wxID_ASDSTATICTEXT1,
              label='Se ha guardado correctamente!. ', name='staticText1',
              parent=self, pos=wx.Point(80, 32), size=wx.Size(311, 23),
              style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.botonAceptar = wx.Button(id=wxID_ASDBOTONACEPTAR, label='Aceptar',
              name='botonAceptar', parent=self, pos=wx.Point(136, 72),
              size=wx.Size(104, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton,
              id=wxID_ASDBOTONACEPTAR)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'carita.png',
              wx.BITMAP_TYPE_PNG), id=wxID_ASDSTATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(8, 16),
              size=wx.Size(60, 60), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonAceptarButton(self, event):
        self.Destroy()
