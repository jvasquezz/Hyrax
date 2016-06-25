from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import *

import sys
import xml.sax
import jenkinsapi

try:
    # for Python2
    from Tkinter import *
    from tkMessageBox import *
except ImportError:
    # for Python3
    from tkinter import *
    from tkinter import messagebox as tkMessageBox

# from __future__ import *
# from
# from git import *
# from evernote3.api.client import *

# from past import autotranslate
from past import autotranslate

autotranslate(['evernote.api.client'])
from evernote.api.client import evernote_client

# import evernote

assert sys.version_info >= (2, 5)

print('Python v:', sys.version)
print('Jenkins api v:', jenkinsapi.__version__)


# create an XMLReader
parser = xml.sax.make_parser()
# turn off namespaces
parser.setFeature(xml.sax.handler.feature_namespaces, 0)

# override the default ContextHandler
# Handler = MovieHandler()
# parser.setContentHandler( Handler )

parser.parse("Hyrax-Styles.xml")

gui = Tk()
gui.title('Hyrax')


def save_remotely():
    btn_save_to_Evernote.config(text="Saved remotely", fg="#75715E", font="Verdana 13 italic bold")


def save_locally():
    btn_save_local.config(text="Saved locally", fg="#75715E", font="Verdana 13 italic bold")


# def get_client
# def connect_user(auth_token):
# 	# connect to sandbox and get userrname
# 	client = EvernoteClient(token=auth_token, sandbox=False)
# 	userStore = client.get_user_store()
# 	return userStore.getUser()

auth_token = 'S=s116:U=c6683a:E=15cd2641d76:C=1557ab2ef78:P=1cd:A=en-devtoken:V=2:H=81b3a396006e4ac040c1403dcb017a2c'
client = evernote_client(token=auth_token, sandbox=False)

# get user object
user = client.get_user_store()
note_store = client.get_note_store()

# note_store = client.get_note_store()
# get all the user's notebooks
# note_store = client.get_note_store()
notebooks = note_store.listNotebooks()

# here show all notebooks available
listbox = Listbox(gui)
# listbox.insert(END, "Notebooks")

for notebook in notebooks:
    listbox.insert(END, notebook.name)
listbox.config(font="Verdana 14 italic", selectbackground="Black")

print("Found ", len(notebooks), " notebooks:")
for notebook in notebooks:
    print(notebook.name)

btn_save_to_Evernote = Button(gui)  # , text = "Save to Evernote", command = save_remotely)
btn_save_local = Button(gui)  # , text = "Save local", command = save_locally)

btn_save_to_Evernote.config(text='Save to Evernote', command=save_remotely)
btn_save_to_Evernote.config(highlightbackground='White', font="Verdana 13 bold")
btn_save_to_Evernote.config(relief='solid')

btn_save_local.config(text="Save locally", command=save_locally)
btn_save_local.config(bg='#000000', fg='#b7f731', font="Verdana 13 bold")
btn_save_local.config(relief='sunken', activeforeground='Blue')
# background=Black)
# btn_save_to_Evernote['background'] = 'Black'
# btn_save_local['background'] = 'Black'

# # for k in btn_save_to_Evernote.configure().keys():
# # if options.has_key (k):
#
# # canvas = Canvas(gui, 1000, 1000)
# # canvas.create_text(200, 200, text="Example Text")
#
# # canvas = Canvas(gui, width=400, height=400)
# # canvas.create_text(200, 200, text="Test")
#
first_click = True


def on_entry_click(event):
    """function that gets called whenever entry1 is clicked"""
    global first_click
    if first_click:  # if this is the first time they clicked it
        first_click = False
        textbox.delete('1.0', END)  # delete all the text in the entry
    textbox.config(font="Verdana 13")
    textbox.tag_add("DEFAULT", '1.0', END)

#
#
# # bg="red", fg="#F8F8F2", font="Verdana 13")
#
word = ""
current_index = 1


def on_key_press(event):
    global isCommentsOn


def on_shift_hash_release(event):
    textbox.tag_config(tagName="COMMENTLINE", font='Verdana 13 italic', foreground="#75715E")
    textbox.tag_remove("COMMENTLINE", INSERT+'-1c', END)
    textbox.tag_add("COMMENTLINE", INSERT+'-1c', END)


def on_enter(event):
    global isCommentsOn
    isCommentsOn = False
    pos = textbox.index(INSERT)

    textbox.tag_config("DEFAULT", font="Verdana 13", foreground="#F8F8F2")
    textbox.tag_remove("COMMENTLINE", pos, END)
    textbox.tag_add("DEFAULT", pos, END)

isCommentsOn = False


textbox = Text(gui, highlightthickness=0)
textbox.config(bg="#272822", fg="#F8F8F2", bd=0, font="Verdana 13")
textbox.tag_config("DEFAULT", font="Verdana 13", foreground="#F8F8F2")
textbox.tag_config("COMMENTLINE", font='Verdana 13 italic', foreground="#75715E")


textbox.insert(INSERT, 'Shrew mouse...')
# textbox.insert(INSERT, "Dassies..")

textbox.bind('<FocusIn>', on_entry_click)
# textbox.bind('<KeyRelease>', on_key_release)
# textbox.bind('<Key>', on_key_press)

textbox.bind('<Shift-KeyRelease-#>', on_shift_hash_release)
# textbox.bind('<Return>', on_enter)

textbox.pack()
textbox.focus_set()
# # canvas.pack()
# e.pack()
# listbox.pack()
btn_save_to_Evernote.pack()
btn_save_local.pack()
gui.mainloop()
