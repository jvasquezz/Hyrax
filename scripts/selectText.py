import Tkinter as tk

root = tk.Tk()

# Create a Text widget with a red selected text background
# And green selected text background when not focused
text = tk.Text(root, selectbackground="red", inactiveselectbackground="green")
text.pack()

# Add some text, and select it
text.insert("1.0", "Hello, world!")
text.tag_add("sel", "1.0", "end")

# Create an Entry widget to easily test the focus behavior
entry = tk.Entry(root)
entry.pack()

entry.insert("0", "Focus me!")

root.mainloop()