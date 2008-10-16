#Boa:Dialog:Dialog1

import wx

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BOTONACEPTAR, wxID_DIALOG1STATICTEXT1, 
 wxID_DIALOG1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(500, 256), size=wx.Size(275, 170),
              style=wx.DEFAULT_DIALOG_STYLE,
              title='Se ha completado la petici\xf3n')
        self.SetClientSize(wx.Size(267, 136))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='la configuracion correctamente', name='staticText1',
              parent=self, pos=wx.Point(48, 40), size=wx.Size(177, 16),
              style=0)
        self.staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label='Se ha exportado/importado', name='staticText2',
              parent=self, pos=wx.Point(56, 16), size=wx.Size(157, 16),
              style=0)
        self.staticText2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR,
              label='Aceptar', name='botonAceptar', parent=self,
              pos=wx.Point(96, 80), size=wx.Size(75, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton,
              id=wxID_DIALOG1BOTONACEPTAR)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonAceptarButton(self, event):
        self.Destroy()
