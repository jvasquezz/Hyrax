import Tkinter as tk


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
        # self.bind('<Key>', self.on_key_press)

    def config_tags(self):
        for tag in self.tags:
            self.tag_config(tagName=tag[0], font=tag[1], foreground=tag[2])

    def remove_tags(self, start, end):
        for tag in self.tags:
            self.tag_remove(tag[0], start, end)

    def on_shift_hash_release(self, event):
        cline = self.index(tk.INSERT).split('.')[0]
        line = self.index(tk.INSERT).split('.')[0]
        last_col = 0
        char = self.get('%s.%d' % (line, last_col))
        while char != '\n':
            last_col += 1
            char = self.get('%s.%d' % (line, last_col))
        # self.remove_tags(cline, '%s.%d' % (line, last_col))
        self.tag_add("comment", tk.INSERT + '-1c', tk.END)

    def on_line_break(self, event):
        # self.remove_tags('%s.%d' % (cline, 0), '%s.%d' % ())
        self.remove_tags(tk.INSERT, tk.END)
        self.tag_add('default', tk.INSERT + '-1c', tk.END)


if __name__ == '__main__':
    gui = tk.Tk()
    textbox = TextFormat(gui)
    textbox.pack()
    gui.title('hyrax')
    gui.mainloop()
