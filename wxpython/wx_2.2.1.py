import wx
class App(wx.App):
    def __init__(self, redirect=False, filename=None, useBestVisual=False, clearSigInt=True):
        wx.App.__init__(self, redirect, filename, useBestVisual, clearSigInt)
    
    def OnInit(self):
        return True

if __name__ == '__main__':
    app = wx.App()
    frame = MyNewFrame(None)
    frame.Show(True)
    app.MainLoop()
