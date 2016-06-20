from Tkinter import *

class Application(Frame):
    def say_hi(self):
        print "hi there, everyone!"

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

------------------------------------------------------

from Tkinter import *

root = Tk()
T = Text(root, height=2, width=30)
T.pack()
T.insert(END, "Just a text Widget\nin two lines\n")
mainloop()

------------------------------------------------------

# import pdb; 
# from Tkinter import *
from evernote.api.client import EvernoteClient

# pdb.set_trace()
# top = Tkinter.Tk()
# Code to add widgets will go here...
# top.mainloop()

# connect to sandbox and get userrname
dev_token = 'S=s116:U=c6683a:E=15cbd7eead1:C=15565cdbcf0:P=1cd:A=en-devtoken:V=2:H=30d64b69c592247912132328448813a1'
client = EvernoteClient(token=dev_token, sandbox=False)
userStore = client.get_user_store()
user = userStore.getUser()
print user.username

# root = Tk()
# T = Text(root, height=2, width=30)
# T.pack()
# T.insert(END, "user")
# mainloop()