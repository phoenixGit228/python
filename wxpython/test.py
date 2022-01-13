# import spare
# print(spare.__doc__)
import wx
class MyApp(wx.App):
    def OnInit(self):
        self.frm = wx.Frame(None, id=-1,title='软件测试')
        self.frm.Show()
        self.SetTopWindow(self.frm)
        return True

app = MyApp()
app.MainLoop()
