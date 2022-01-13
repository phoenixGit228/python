"""
helloworld程序，但是更丰富
"""

# # 第一步，导入wxpython 包
# import wx
# # 创建一个App对象
# app = wx.App()
# # 下一步，创建Frame
# frm = wx.Frame(None, title='hello world')
# # 显示
# frm.Show()
# # 让时间循环
# app.MainLoop()


# import wx

# class App(wx.App):
#     def OnInit(self):
#         frame = wx.Frame(parent=None, title='hello world')
#         frame.Show()
#         return True

# app = App()
# app.MainLoop()

import wx
class MyApp(wx.App):
    def OnInit(self):
        frm = wx.Frame(None, id=-1,title='bare')
        frm.Show()
        return True

app = MyApp()
app.MainLoop()
# print(dir(wx.Frame))