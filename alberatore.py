import tkinter as tk
from tkinter import filedialog
import os

def genera_alberatura(percorso_cartella):
    alberatura = ''
    for root, dirs, files in os.walk(percorso_cartella):
        livello = root.replace(percorso_cartella, '').count(os.sep)
        indentazione = ' ' * 4 * livello
        alberatura += '{}{}/\n'.format(indentazione, os.path.basename(root))
        sottoindentazione = ' ' * 4 * (livello + 1)
        for file in files:
            alberatura += '{}{}\n'.format(sottoindentazione, file)
    return alberatura

def seleziona_cartella():
    cartella = filedialog.askdirectory()
    percorso_cartella.set(cartella)

def genera():
    cartella = percorso_cartella.get()
    if cartella:
        alberatura = genera_alberatura(cartella)
        text_widget.delete(1.0, tk.END)
        text_widget.insert(tk.END, alberatura)

root = tk.Tk()
root.title("Generatore di Alberatura Cartella")

percorso_cartella = tk.StringVar()

btn_seleziona = tk.Button(root, text="Seleziona Cartella", command=seleziona_cartella)
btn_seleziona.pack(pady=5)

btn_genera = tk.Button(root, text="Genera", command=genera)
btn_genera.pack(pady=5)

text_widget = tk.Text(root, width=80, height=20)
text_widget.pack(pady=5)

root.mainloop()
