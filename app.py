import json
import threading

import sqlite3

import evernote.edam.type.ttypes as types
import os
import resources.R as R
import tkinter as tk
from dotenv import load_dotenv
from evernote.api.client import EvernoteClient
import settings

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
print('cwd:', os.getcwd())


class TextFormat(tk.Text):
    tags = [['default', 'Verdana 13', '#F8F8F2'],
            ['comment', 'Verdana 13 italic', '#75715E']]

    def __init__(self, root):
        tk.Text.__init__(self, root)
        self.line_count = '1'
        self.config_tags()
        self.config(width=40, height=28, insertbackground='white')
        self.config(relief=tk.SOLID, selectbackground='#8000FF')
        self.config(wrap=tk.NONE, insertborderwidth='1', highlightthickness=0)
        self.config(bg="#272822", fg="#F8F8F2", bd=0, font="Verdana 13")

        self.tag_add('default', '1.0', tk.END)
        self.bind(sequence='<Shift-KeyRelease-#>', func=self.shf_hash_release)
        self.bind(sequence='<Return>', func=self.on_line_break)
        self.bind(sequence='<Command-Return>', func=self.cmd_enter)
        pass

    def cmd_enter(self, event):
        ArdentButton.save_to_local(event)

    def config_tags(self):
        for tag in self.tags:
            self.tag_config(tagName=tag[0], font=tag[1], foreground=tag[2])

    def remove_tags(self, start, end):
        for tag in self.tags:
            self.tag_remove(tag[0], start, end)

    def shf_hash_release(self, event):
        current_line = self.index(tk.INSERT).split('.')[0]
        if current_line == self.line_count:
            self.tag_add("comment", tk.INSERT + '-1c', tk.END)
            return

        last_col = 0
        char = self.get('%s.%d' % (current_line, last_col))
        while char != '\n':
            last_col += 1
            char = self.get('%s.%d' % (current_line, last_col))
        end_of_line = current_line + '.' + str(last_col)
        self.tag_add("comment", tk.INSERT + '-1c', end_of_line)

    def on_line_break(self, event):
        self.line_count = self.index(tk.END).split('.')[0]
        self.remove_tags(tk.INSERT, tk.END)
        self.tag_add('default', tk.INSERT + '-1c', tk.END)
        ''' auto save on line break '''
        with open('data.json', 'wb') as f:
            data = self.get('1.0', tk.END)
            json.dump({'data': data, 'line_count': self.line_count}, f)


# threads any decorated function
def threaded(function):
    def wrapper(*args, **kwargs):
        threading.Thread(target=function, args=args, kwargs=kwargs).start()

    return wrapper


class ArdentButton(tk.Button):
    def __init__(self, root, which):
        tk.Button.__init__(self, root)
        self.icon = tk.PhotoImage(file=R.icons.get(which))
        self.config(image=self.icon, width='25', height='25', bd=0)
        self.config(relief=tk.RIDGE)
        if 'evernote' is which:
            self.bind('<Button-1>', self.save_to_evernote)
        if 'local' is which:
            self.bind('<Button-1>', self.save_to_local)
        pass

    @staticmethod
    @threaded
    def save_to_evernote(event):
        note = types.Note()
        note.title = "Hyrax rune"
        client = accounts.evernote
        # user = client.get_user_store()
        # print(user.getUser())
        note_store = client.get_note_store()
        note.content = '<?xml version="1.0" encoding="UTF-8"?>' \
                       '<!DOCTYPE en-note SYSTEM ' \
                       '"http://xml.evernote.com/pub/enml2.dtd">' \
                       '<en-note>'
        note.content += textbox.get('1.0', tk.END)
        note.content += '</en-note>'
        # notebooks = note_store.listNotebooks()
        note_store.createNote(note)
        print('saved to evernote')

    @staticmethod
    def save_to_local(event):
        con = sqlite3.connect('files.db')
        with con:
            cur = con.cursor()
            notes_table = 'CREATE TABLE IF NOT EXISTS notes (title, content, date)'
            cur.execute(notes_table)
            first_line = '1st line'
            content = textbox.get('1.0', tk.END)
            t = (first_line, content, 'today')
            cur.execute('INSERT INTO notes VALUES (?,?,?)', t)
            cur.execute('SELECT * FROM notes')
            for data in cur.fetchall():
                print(data)

        print(event.char)
        print('saved to local')


class Accounts:
    evernote = EvernoteClient
    load_from_cache = []

    def __init__(self):
        self.init_evernote()
        self.load_local_cache()
        pass

    def init_evernote(self):
        ev = EvernoteClient(token=settings.EVERNOTE_API_KEY,
                            consumer_key=settings.EVERNOTE_CONSUMER_KEY,
                            consumer_secret=settings.EVERNOTE_CONSUMER_SECRET,
                            sandbox=True)
        self.evernote = ev

    def load_local_cache(self):
        try:
            with open('data.json') as cached_json_object:
                self.load_from_cache = json.load(cached_json_object)
                textbox.insert(tk.INSERT, self.load_from_cache['data'])
                textbox.line_count = self.load_from_cache['line_count']
        except IOError:
            pass


if __name__ == '__main__':
    gui = tk.Tk()
    gui.title('hyrax')
    textbox = TextFormat(gui)
    accounts = Accounts()

    ''' button declarations '''
    evernote_button = ArdentButton(gui, 'evernote')
    save_local_button = ArdentButton(gui, 'local')
    save_to_google_drive = ArdentButton(gui, 'google_drive')
    save_git_lab = ArdentButton(gui, 'git_lab')
    search_duck_duck_go = ArdentButton(gui, 'duck_duck_go')
    remove_trash = ArdentButton(gui, 'thrash')
    copy_to_clipboard = ArdentButton(gui, 'clipboard')

    ''' packs and layout '''
    textbox.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
    evernote_button.pack(side=tk.LEFT)
    save_local_button.pack(side=tk.LEFT)
    save_to_google_drive.pack(side=tk.LEFT)
    save_git_lab.pack(side=tk.LEFT)
    search_duck_duck_go.pack(side=tk.LEFT)
    remove_trash.pack(side=tk.RIGHT)
    copy_to_clipboard.pack(side=tk.RIGHT)
    gui.mainloop()
