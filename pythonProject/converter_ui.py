import wx

from coventer_controller import ConverterController

class ConverterPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.converter_controller=ConverterController()
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        self.list_ctrl = wx.ListCtrl(
            self, size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.list_ctrl.InsertColumn(0, 'To Save', width=140)
        self.list_ctrl.InsertColumn(1, 'Table Name', width=140)
        self.add_lines()
        main_sizer.Add(self.list_ctrl, 0, wx.ALL | wx.EXPAND, 5)
        save_button = wx.Button(self, label='Save')
        save_button.Bind(wx.EVT_BUTTON, self.on_save)
        main_sizer.Add(save_button, 0, wx.ALL | wx.CENTER, 5)
        self.SetSizer(main_sizer)

    def on_save(self, event):
        table_names = self.converter_controller.find_all_table_names()
        self.converter_controller.export_tables(table_names)

    def add_lines(self):
        rows = self.converter_controller.find_all_table_names()
        index = 0
        for row in rows:
            self.list_ctrl.InsertStringItem(index, False)
            self.list_ctrl.SetStringItem(index, 1, row)
            index += 1


class ConverterFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None,
                         title='DataBase Converter')
        self.panel = ConverterPanel(self)
        self.Show()


if __name__ == '__main__':
    app = wx.App(False)
    frame = ConverterFrame()
    app.MainLoop()
