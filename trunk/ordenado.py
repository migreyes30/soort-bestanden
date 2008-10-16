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
              pos=wx.Point(368, 144), size=wx.Size(280, 176),
              style=wx.DEFAULT_DIALOG_STYLE, title='Ordenando...')
        self.SetClientSize(wx.Size(272, 142))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='Se esta ordenando .....', name='staticText1', parent=self,
              pos=wx.Point(72, 32), size=wx.Size(132, 16), style=0)
        self.staticText1.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.staticText2 = wx.StaticText(id=wxID_DIALOG1STATICTEXT2,
              label='espera unos segundos.', name='staticText2', parent=self,
              pos=wx.Point(64, 56), size=wx.Size(132, 16), style=0)
        self.staticText2.SetFont(wx.Font(10, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.botonAceptar = wx.Button(id=wxID_DIALOG1BOTONACEPTAR,
              label='Aceptar', name='botonAceptar', parent=self,
              pos=wx.Point(96, 96), size=wx.Size(75, 23), style=0)
        self.botonAceptar.Bind(wx.EVT_BUTTON, self.OnBotonAceptarButton,
              id=wxID_DIALOG1BOTONACEPTAR)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBotonAceptarButton(self, event):
        self.Destroy()
