#Boa:Dialog:Error2

import wx

def create(parent):
    return Error2(parent)

[wxID_ERROR2, wxID_ERROR2BUTTON1, wxID_ERROR2STATICBITMAP1, 
 wxID_ERROR2STATICTEXT1, wxID_DIALOG1STATICBITMAP1,
] = [wx.NewId() for _init_ctrls in range(5)]


class Error2(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ERROR2, name=u'Error2', parent=prnt,
              pos=wx.Point(464, 327), size=wx.Size(492, 211),
              style=wx.DEFAULT_DIALOG_STYLE, title='Error Direccion 2')
        self.SetClientSize(wx.Size(484, 177))

        self.button1 = wx.Button(id=wxID_ERROR2BUTTON1, label=u'Aceptar',
              name='button1', parent=self, pos=wx.Point(200, 128),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_ERROR2BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_ERROR2STATICTEXT1,
              label=u'La direccion 2 no existe', name='staticText1',
              parent=self, pos=wx.Point(120, 48), size=wx.Size(346, 35),
              style=0)
        self.staticText1.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'error.png',
              wx.BITMAP_TYPE_PNG), id=wxID_ERROR2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(32, 40),
              size=wx.Size(48, 48), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.Destroy()
