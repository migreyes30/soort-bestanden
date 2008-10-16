#Boa:Frame:Frame2

import wx

def create(parent):
    return Frame2(parent)

[wxID_FRAME2] = [wx.NewId() for _init_ctrls in range(1)]

class Frame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(88, 116), size=wx.Size(400, 492),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame2')
        self.SetClientSize(wx.Size(392, 458))

    def __init__(self, parent):
        self._init_ctrls(parent)
