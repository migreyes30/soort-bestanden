#Boa:Frame:Frame2

import wx
import wx.html
import Frame1

page = """<html><body> 

This silly example shows how custom tags can be defined and used in a wx.HtmlWindow. We've defined a new tag, &lt;blue&gt; that will change the <blue>foreground color</blue> of the portions of the document that it encloses to some shade of blue. The tag handler can also use parameters specified in the tag, for example: 

<ul>

<li> <blue shade='sky'>Sky Blue</blue>

<li> <blue shade='midnight'>Midnight Blue</blue>

<li> <blue shade='dark'>Dark Blue</blue>

<li> <blue shade='navy'>Navy Blue</blue>

</ul>

</body></html>

"""

def create(parent):
    return Frame2(parent)

[wxID_FRAME2, wxID_FRAME2BITMAPBUTTON1, wxID_FRAME2PAGINA, 
 wxID_FRAME2STATICBITMAP1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(406, 150), size=wx.Size(600, 450),
              style=wx.DEFAULT_FRAME_STYLE, title='Ayuda')
        self.SetClientSize(wx.Size(592, 416))
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetIcon(wx.Icon(u'icon.ico',wx.BITMAP_TYPE_ICO))

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.Bitmap(u'regresar.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2BITMAPBUTTON1,
              name='bitmapButton1', parent=self, pos=wx.Point(8, 336),
              size=wx.Size(168, 64), style=wx.BU_AUTODRAW)
        self.bitmapButton1.Bind(wx.EVT_BUTTON, self.OnBitmapButton1Button,
              id=wxID_FRAME2BITMAPBUTTON1)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('ayuda.png',
              wx.BITMAP_TYPE_PNG), id=wxID_FRAME2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(168, 8),
              size=wx.Size(224, 64), style=0)

        self.pagina = wx.html.HtmlWindow(id=wxID_FRAME2PAGINA, name='pagina',
              parent=self, pos=wx.Point(48, 80), size=wx.Size(480, 240),
              style=wx.html.HW_SCROLLBAR_AUTO)
        
        html = wx.html.HtmlWindow(self)
        html.SetStandardFonts()
        html.SetPage(page)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnBitmapButton1Button(self, event):
        ventanaInicial = Frame1.create(None)
        self.Destroy()
        ventanaInicial.Show()

