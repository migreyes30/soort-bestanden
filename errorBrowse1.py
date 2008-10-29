#Boa:Dialog:Error1

import wx

def create(parent):
    return Error1(parent)

[wxID_ERROR1, wxID_ERROR1BUTTON1, wxID_ERROR1STATICBITMAP1, 
 wxID_ERROR1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Error1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ERROR1, name=u'Error1', parent=prnt,
              pos=wx.Point(490, 300), size=wx.Size(350, 150),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Error Direccion 1')
        self.SetClientSize(wx.Size(342, 116))

        self.button1 = wx.Button(id=wxID_ERROR1BUTTON1, label=u'Aceptar',
              name='button1', parent=self, pos=wx.Point(120, 80),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_ERROR1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_ERROR1STATICTEXT1,
              label=u'La direccion 1 no existe', name='staticText1',
              parent=self, pos=wx.Point(80, 24), size=wx.Size(245, 25),
              style=0)
        self.staticText1.SetFont(wx.Font(16, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.Destroy()
