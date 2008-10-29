#Boa:Dialog:Error2

import wx

def create(parent):
    return Error2(parent)

[wxID_ERROR2, wxID_ERROR2BUTTON1, wxID_ERROR2STATICBITMAP1, 
 wxID_ERROR2STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(4)]


class Error2(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ERROR2, name=u'Error2', parent=prnt,
              pos=wx.Point(490, 300), size=wx.Size(350, 150),
              style=wx.DEFAULT_DIALOG_STYLE, title='Error Direccion 2')
        self.SetClientSize(wx.Size(342, 116))

        self.button1 = wx.Button(id=wxID_ERROR2BUTTON1, label=u'Aceptar',
              name='button1', parent=self, pos=wx.Point(136, 80),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_ERROR2BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_ERROR2STATICTEXT1,
              label=u'La direccion 2 no existe', name='staticText1',
              parent=self, pos=wx.Point(72, 24), size=wx.Size(245, 25),
              style=0)
        self.staticText1.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'error.png',
              wx.BITMAP_TYPE_PNG), id=wxID_ERROR2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(8, 16),
              size=wx.Size(48, 48), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.Destroy()
