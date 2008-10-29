#Boa:Dialog:Error3

import wx

def create(parent):
    return Error3(parent)

[wxID_ERROR3, wxID_ERROR3BUTTON1, wxID_ERROR3STATICBITMAP1, 
 wxID_ERROR3STATICTEXT1, wxID_DIALOG1STATICBITMAP1,
] = [wx.NewId() for _init_ctrls in range(5)]

class Error3(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ERROR3, name=u'Error3', parent=prnt,
              pos=wx.Point(446, 267), size=wx.Size(489, 210),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Error Direccion 3')
        self.SetClientSize(wx.Size(481, 176))

        self.button1 = wx.Button(id=wxID_ERROR3BUTTON1, label=u'Aceptar',
              name='button1', parent=self, pos=wx.Point(184, 120),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_ERROR3BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_ERROR3STATICTEXT1,
              label=u'La direccion 3 no existe', name='staticText1',
              parent=self, pos=wx.Point(104, 48), size=wx.Size(346, 35),
              style=0)
        self.staticText1.SetFont(wx.Font(22, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, u'Tahoma'))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'error.png',
              wx.BITMAP_TYPE_PNG), id=wxID_ERROR3STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(24, 40),
              size=wx.Size(48, 48), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def OnButton1Button(self, event):
        self.Destroy()

