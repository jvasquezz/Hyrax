import Tkinter as tk


class TextFormat(tk.Text):
    def __init__(self, root):
        tk.Text.__init__(self, root)
        self.config_tags()
        self.config(highlightthickness=0, bg="#272822", fg="#F8F8F2", bd=0, font="Verdana 13")
        self.bind(self, '<Shift-KeyRelease-#>', self.on_shift_hash_release)
        self.bind('<Key>', self.on_key_press)

    def config_tags(self):
        self.tag_config(tagName="comment", font='Verdana 13 italic', foreground="#75715E")
        self.tag_config(tagName="default", font="Verdana 13", foreground="#F8F8F2")

    def on_shift_hash_release(self, event):
        # self.tag_remove("default", tk.INSERT + '-1c', tk.END)
        self.tag_add("comment", tk.INSERT + '-1c', tk.END)

    def on_key_press(self, event):
        print '#'

if __name__ == '__main__':
    root = tk.Tk()
    sht = TextFormat(root)
    sht.pack()
    root.mainloop()