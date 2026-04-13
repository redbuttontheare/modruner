from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import ScrolledText
import subprocess
import tempfile
import os

from Creator.Mod import *
from Creator.Block import *

current_file = None

def open_file():
    global current_file
    file_path = askopenfilename(
        filetypes=[
            ("Python Files", "*.py"),
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    current_file = file_path

    with open(file_path, "r", encoding="utf-8") as file:
        Code.delete(1.0, END)
        Code.insert(END, file.read())


def save():
    global current_file

    if current_file:
        with open(current_file, "w", encoding="utf-8") as file:
            file.write(Code.get(1.0, "end-1c"))
    else:
        save_as()


def save_as():
    global current_file

    file_path = asksaveasfilename(
        defaultextension=".py",
        filetypes=[
            ("Python Files", "*.py"),
            ("No console files", "*.pyw"),
            ("All Files", "*.*")
        ]
    )

    if not file_path:
        return

    current_file = file_path

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(Code.get(1.0, "end-1c"))


def run_code():
    code = Code.get(1.0, "end-1c")

    # створюємо тимчасовий файл
    with tempfile.NamedTemporaryFile(delete=False, suffix=".py", mode="w", encoding="utf-8") as tmp:
        tmp.write(code)
        tmp_path = tmp.name

    # запускаємо
    subprocess.Popen(["python", tmp_path])

def block():
    Blocker(1)


id = "1568.4444"
name = "PyCreator"
studio = "Heigts studios©"
ver = "6.0"
fount = ("Consolas", 16)
lic = "All rights"

registr(id, name)
license(studio, lic)

writer("This mod was be created for easy mods creating!")
writer("If you did'n need PyCreator you can delete PyCreator")

app = Tk()
app.title(f"PyCreator | v{ver}")
app.geometry("700x400")

top = Menu(app)
app.config(menu=top)

# FILE MENU
filemenu = Menu(top, tearoff=0)
top.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save)
filemenu.add_command(label="Save As", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=app.quit)

editmenu = Menu(top, tearoff=0)
top.add_cascade(label="Edit", menu=editmenu)

editmenu.add_separator()
editmenu.add_command(label="Block app", command=block)

# EDITOR
Code = ScrolledText(
    app,
    background="gray",
    foreground="white",
    insertbackground="white",
    font=fount
)
Code.pack(fill="both", expand=True)
Code.insert("1.0", """import Creator
from Creator.Mod import *

mod = 'MyMod'

registr('444.7584', mod)
license('', 'USR license')
# if in your mod/plugin USR license other users
# can edit your mod/plugin

writer('Hello, world!') # you can
# print msg as 'App Console'""")

app.mainloop()
