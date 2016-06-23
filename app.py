import Tkinter as tk
import os

print 'cwd:', os.getcwd()


class TextFormat(tk.Text):
    tags = [['default', 'Verdana 13', '#F8F8F2'],
            ['comment', 'Verdana 13 italic', '#75715E']]

    def __init__(self, root):
        tk.Text.__init__(self, root)
        self.config_tags()
        self.config(highlightthickness=0, bg="#272822", fg="#F8F8F2", bd=0, font="Verdana 13")
        self.tag_add('default', '1.0', tk.END)
        self.bind(sequence='<Shift-KeyRelease-#>', func=self.on_shift_hash_release)
        self.bind(sequence='<Return>', func=self.on_line_break)

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
        self.tag_add("comment", tk.INSERT + '-1c', tk.END)

    def on_line_break(self, event):
        self.remove_tags(tk.INSERT, tk.END)
        self.tag_add('default', tk.INSERT + '-1c', tk.END)


class ArdentButton(tk.Button):
    icons_dict = {'evernote': '/Users/jonathanvasquez/PycharmProjects/Hyrax/resources/evernote0.gif',
                  'local': '/Users/jonathanvasquez/PycharmProjects/Hyrax/resources/icon_save.gif',
                  'google_drive': '/Users/jonathanvasquez/PycharmProjects/Hyrax/resources/google_drive.gif',
                  'duck_duck_go': '/Users/jonathanvasquez/PycharmProjects/Hyrax/resources/duck_duck_go.gif',
                  'git_lab': '/Users/jonathanvasquez/PycharmProjects/Hyrax/resources/git_lab.gif',
                  'thrash': '/Users/jonathanvasquez/PycharmProjects/Hyrax/resources/thrash.gif',
                  }

    def __init__(self, root, which):
        tk.Button.__init__(self, root)
        self.icon = tk.PhotoImage(file=self.icons_dict.get(which))
        self.config(image=self.icon, width='25', height='25', bd=0, relief=tk.RIDGE)


if __name__ == '__main__':
    gui = tk.Tk()
    gui.title('hyrax')
    textbox = TextFormat(gui)
    save_to_evernote = ArdentButton(gui, 'evernote')
    save_to_local = ArdentButton(gui, 'local')
    save_to_google_drive = ArdentButton(gui, 'google_drive')
    save_git_lab = ArdentButton(gui, 'git_lab')

    search_duck_duck_go = ArdentButton(gui, 'duck_duck_go')
    remove_trash = ArdentButton(gui, 'thrash')

    textbox.pack()
    save_to_evernote.pack(side=tk.LEFT)
    save_to_local.pack(side=tk.LEFT)
    save_to_google_drive.pack(side=tk.LEFT)
    save_git_lab.pack(side=tk.LEFT)
    search_duck_duck_go.pack(side=tk.LEFT)
    remove_trash.pack(side=tk.RIGHT)
    gui.mainloop()
