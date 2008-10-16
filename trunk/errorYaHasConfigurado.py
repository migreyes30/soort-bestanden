#Boa:Dialog:errorYaConfig

import wx

def create(parent):
    return errorYaConfig(parent)

[wxID_ERRORYACONFIG, wxID_ERRORYACONFIGBUTTON1, 
 wxID_ERRORYACONFIGSTATICBITMAP1, wxID_ERRORYACONFIGSTATICTEXT1, 
 wxID_ERRORYACONFIGSTATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(5)]

class errorYaConfig(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_ERRORYACONFIG, name='errorYaConfig',
              parent=prnt, pos=wx.Point(486, 247), size=wx.Size(377, 171),
              style=wx.DEFAULT_DIALOG_STYLE, title='Error')
        self.SetClientSize(wx.Size(369, 137))

        self.staticText1 = wx.StaticText(id=wxID_ERRORYACONFIGSTATICTEXT1,
              label='Ya has configurado esta opci\xf3n.', name='staticText1',
              parent=self, pos=wx.Point(80, 24), size=wx.Size(238, 18),
              style=0)
        self.staticText1.SetFont(wx.Font(11, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'C:/ProyectoCognitiva/error.png',
              wx.BITMAP_TYPE_PNG), id=wxID_ERRORYACONFIGSTATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(8, 16),
              size=wx.Size(48, 48), style=0)

        self.staticText2 = wx.StaticText(id=wxID_ERRORYACONFIGSTATICTEXT2,
              label='Borra la configuraci\xf3n actual para que puedas configurarla.',
              name='staticText2', parent=self, pos=wx.Point(32, 72),
              size=wx.Size(317, 14), style=0)
        self.staticText2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Tahoma'))

        self.button1 = wx.Button(id=wxID_ERRORYACONFIGBUTTON1, label='Aceptar',
              name='button1', parent=self, pos=wx.Point(144, 104),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_ERRORYACONFIGBUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.Destroy()
