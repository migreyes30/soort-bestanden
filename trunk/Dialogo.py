#Boa:Dialog:Dialog1

import wx
import Frame1

def create(parent):
    return Dialog1(parent)

[wxID_DIALOG1, wxID_DIALOG1BUTTON1, wxID_DIALOG1BUTTON2, 
 wxID_DIALOG1STATICBITMAP1, wxID_DIALOG1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Dialog1(wx.Dialog):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG1, name='', parent=prnt,
              pos=wx.Point(500, 250), size=wx.Size(310, 137),
              style=wx.DEFAULT_DIALOG_STYLE, title='Advertencia')
        self.SetClientSize(wx.Size(302, 103))

        self.button1 = wx.Button(id=wxID_DIALOG1BUTTON1, label='Si',
              name='button1', parent=self, pos=wx.Point(64, 64),
              size=wx.Size(88, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG1BUTTON1)

        self.button2 = wx.Button(id=wxID_DIALOG1BUTTON2, label='No',
              name='button2', parent=self, pos=wx.Point(176, 64),
              size=wx.Size(91, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_DIALOG1BUTTON2)

        self.staticText1 = wx.StaticText(id=wxID_DIALOG1STATICTEXT1,
              label='\xbf Estas seguro ?', name='staticText1', parent=self,
              pos=wx.Point(88, 16), size=wx.Size(156, 23), style=0)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.BOLD,
              False, 'Tahoma'))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap(u'pregunta.png',
              wx.BITMAP_TYPE_PNG), id=wxID_DIALOG1STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(56, 52), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
        
    def OnButton1Button(self, event):
        self.Destroy()

    def OnButton2Button(self, event):
        self.Destroy()
