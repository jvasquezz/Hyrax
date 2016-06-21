try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *

# from git import *
from evernote.api.client import *
from tkMessageBox import *

import xml.sax

# create an XMLReader
parser = xml.sax.make_parser()
# turn off namepsaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
# Handler = MovieHandler()
# parser.setContentHandler( Handler )

parser.parse("Hyrax-Styles.xml")

gui = Tk()


def save_remotely():
    showinfo("Evernote", "Saved to Evernote remote destination")


def save_locally():
    showinfo("Evernote", "Saved to local destination")


# def get_client
# def connect_user(auth_token):
# 	# connect to sandbox and get userrname
# 	client = EvernoteClient(token=auth_token, sandbox=False)
# 	userStore = client.get_user_store()
# 	return userStore.getUser()

auth_token = 'S=s116:U=c6683a:E=15cbd7eead1:C=15565cdbcf0:P=1cd:A=en-devtoken:V=2:H=30d64b69c592247912132328448813a1'
client = EvernoteClient(token=auth_token, sandbox=False)

# get user object
user = client.get_user_store()

# get all the users notebooks
note_store = client.get_note_store()
notebooks = note_store.listNotebooks()
notebooks = note_store.listNotebooks()

# here show all notebooks available
listbox = Listbox(gui)
# listbox.insert(END, "Notebooks")

for notebook in notebooks:
    listbox.insert(END, notebook.name)
listbox.config(font="Verdana 14 italic", selectbackground="Black")

# print "Found ", len(notebooks), " notebooks:"
# for notebook in notebooks:
# print "  * ", notebook.name
# :tclmacbag:

btn_save_to_Evernote = Button(gui)  # , text = "Save to Evernote", command = save_remotely)
btn_save_local = Button(gui)  # , text = "Save local", command = save_locally)

btn_save_to_Evernote.config(text='Save to Evernote', command=save_remotely)
btn_save_to_Evernote.config(highlightbackground='White', font="Verdana 13 bold")
btn_save_to_Evernote.config(relief='solid')

btn_save_local.config(text="Save local", command=save_locally)
btn_save_local.config(bg='#000000', fg='#b7f731', font="Verdana 13 bold")
btn_save_local.config(relief='sunken', activeforeground='Blue')
# background=Black)
# btn_save_to_Evernote['background'] = 'Black'
# btn_save_local['background'] = 'Black'

# for k in btn_save_to_Evernote.configure().keys():
# if options.has_key (k):

# canvas = Canvas(gui, 1000, 1000)
# canvas.create_text(200, 200, text="Example Text")

# canvas = Canvas(gui, width=400, height=400)
# canvas.create_text(200, 200, text="Test")

firstclick = True


def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""
    global firstclick
    if firstclick:  # if this is the first time they clicked it
        firstclick = False
        textbox.delete('1.0', END)  # delete all the text in the entry
    textbox.config(font="Verdana 13")
    textbox.tag_add("DEFAULT", '1.0', END)
    textbox.tag_config("DEFAULT", font="Verdana 13")


# bg="red", fg="#F8F8F2", font="Verdana 13")

word = ""


def on_key_press(event):
    if event.char is '#':
        countVar = StringVar()
        pos = textbox.search("#.+\n", "1.0", regexp=True)
        end = textbox.search(".+", pos, regexp=True)
        textbox.tag_add("COMMENTLINE", pos, end)  ##"%s + %sc" (pos, end))
        textbox.tag_config("COMMENTLINE", background="Blue")
    # textbox.tag_add("COMMENTLINE", )
    # text.tag_add("search", pos, "%s + %sc" (pos, countVar.get()))

    # global word
    # word += event.char
    # if len(word) > 5:
    # 	print textbox.get(word)


# sundriedClay = '#272822'

# <WordsStyle name="COMMENTLINE" styleID="1" fgColor="75715E" bgColor="272822" 
# fontName="" fontStyle="" fontSize="10" />


textbox = Text(gui, highlightthickness=0)
textbox.config(bg="#272822", fg="#F8F8F2", bd=0, font="Verdana 13")
# textbox.tag_config("DEFAULT", bg="red", fg="#F8F8F2", font="Verdana 13")

# textbox.insert(INSERT, "Shrewmouse...")
textbox.insert(INSERT, "Dassies..")

textbox.bind('<FocusIn>', on_entry_click)
textbox.bind('<Key>', on_key_press)

e = Entry(gui)
e.config(font="Verdana 14", selectbackground="#139C1A", selectforeground="White")
e.config()
e.focus_set()

textbox.pack()
textbox.focus_set()
# canvas.pack()
e.pack()
listbox.pack()
btn_save_to_Evernote.pack()
btn_save_local.pack()

gui.mainloop()
