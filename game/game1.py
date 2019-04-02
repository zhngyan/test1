#弹窗功能
import tkinter as tk
import tkinter.messagebox as mbox

class MainUi(tk.Frame):
    def __init__(self,maseter = None):
        tk.Frame.__init__(self,maseter)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.firstLabel = tk.Label(self,text = "【EVA】")
        self.firstLabel.grid()
        self.clickButton  = tk.Button(self, text =  "   点击进入EVA的世界", command = self.answer)
        self.clickButton.grid()

    def answer(self):
        mbox.showinfo("EVA",'''加载中。。。''')

app = MainUi()
app.master.title('EVA')
app.master.geometry('400x100')
app.mainloop()