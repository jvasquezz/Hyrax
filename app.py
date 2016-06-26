import io
import os
import tkinter as tk
import resources.R as R
import settings
import threading
from evernote.api.client import EvernoteClient as evernote_client
import evernote.edam.type.ttypes as types
from dotenv import load_dotenv
import json

load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))
print('cwd:', os.getcwd())


class TextFormat(tk.Text):
    tags = [['default', 'Verdana 13', '#F8F8F2'],
            ['comment', 'Verdana 13 italic', '#75715E']]
    line_count = 1

    def __init__(self, root):
        tk.Text.__init__(self, root)
        self.config_tags()
        self.config(width=40, height=28, insertbackground='white', relief=tk.SOLID, selectbackground='#8000FF',
                    wrap=tk.NONE,
                    insertborderwidth='1', highlightthickness=0, bg="#272822", fg="#F8F8F2", bd=0, font="Verdana 13")
        self.tag_add('default', '1.0', tk.END)
        self.bind(sequence='<Shift-KeyRelease-#>', func=self.on_shift_hash_release)
        self.bind(sequence='<Return>', func=self.on_line_break)
        pass

    def config_tags(self):
        for tag in self.tags:
            self.tag_config(tagName=tag[0], font=tag[1], foreground=tag[2])

    def remove_tags(self, start, end):
        for tag in self.tags:
            self.tag_remove(tag[0], start, end)

    def on_shift_hash_release(self, event):
        line = self.index(tk.INSERT).split('.')[0]
        last_col = 0
        char = self.get('%s.%d' % (line, last_col))
        while char != '\n':
            last_col += 1
            char = self.get('%s.%d' % (line, last_col))
        if line is str(self.line_count):
            self.tag_add("comment", tk.INSERT + '-1c', tk.END)
        else:
            self.tag_add("comment", tk.INSERT + '-1c', line + '.' + str(last_col))

    def on_line_break(self, event):
        self.line_count += 1
        self.remove_tags(tk.INSERT, tk.END)
        self.tag_add('default', tk.INSERT + '-1c', tk.END)
        # accounts.local


# it threads any decorated function - http://en.wikipedia.org/wiki/Python_syntax_and_semantics#Decorators
def threaded(function):
    def wrapper(*args, **kwargs):
        threading.Thread(target=function, args=args, kwargs=kwargs).start()

    return wrapper


class ArdentButton(tk.Button):
    def __init__(self, root, which):
        tk.Button.__init__(self, root)
        self.icon = tk.PhotoImage(file=R.icons.get(which))
        self.config(image=self.icon, width='25', height='25', bd=0, relief=tk.RIDGE)
        if 'evernote' is which:
            self.bind('<Button-1>', self.evernote)
        if 'local' is which:
            self.bind('<Button-1>', self.local_storage)
        pass

    @staticmethod
    @threaded
    def evernote(event):
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
    def local_storage(event):
        data = textbox.get('1.0', tk.END)
        # encoded = json.dumps(data, ensure_ascii=False).encode('utf8')
        with open('data.json', 'wb') as f:
            json.dump({'data': data}, f)
            print(data)
            # print(encoded)


class Accounts:
    evernote = evernote_client
    load_from_cache = []

    def __init__(self):
        self.init_evernote()
        self.local_storage()
        pass

    def init_evernote(self):
        self.evernote = evernote_client(token=settings.EVERNOTE_API_KEY,
                                        consumer_key=settings.EVERNOTE_CONSUMER_KEY,
                                        consumer_secret=settings.EVERNOTE_CONSUMER_SECRET,
                                        sandbox=True)

    def local_storage(self):
        try:
            with open('data.json') as cached_json_object:
                self.load_from_cache = json.load(cached_json_object)
                textbox.insert(tk.INSERT, self.load_from_cache['data'])
        except IOError:
            pass

if __name__ == '__main__':
    gui = tk.Tk()
    gui.title('hyrax')
    textbox = TextFormat(gui)
    accounts = Accounts()

    ''' button declares '''
    save_to_evernote = ArdentButton(gui, 'evernote')
    save_to_local = ArdentButton(gui, 'local')
    save_to_google_drive = ArdentButton(gui, 'google_drive')
    save_git_lab = ArdentButton(gui, 'git_lab')
    search_duck_duck_go = ArdentButton(gui, 'duck_duck_go')
    remove_trash = ArdentButton(gui, 'thrash')
    copy_to_clipboard = ArdentButton(gui, 'clipboard')

    ''' packs and layout '''
    textbox.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.YES)
    save_to_evernote.pack(side=tk.LEFT)
    save_to_local.pack(side=tk.LEFT)
    save_to_google_drive.pack(side=tk.LEFT)
    save_git_lab.pack(side=tk.LEFT)
    search_duck_duck_go.pack(side=tk.LEFT)
    remove_trash.pack(side=tk.RIGHT)
    copy_to_clipboard.pack(side=tk.RIGHT)
    gui.mainloop()
