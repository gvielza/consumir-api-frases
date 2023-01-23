import requests
import tkinter as tk
from api_key import API_KEY as key
from translate import Translator

from tkinter import messagebox
import pyperclip


response = requests.get(f'https://favqs.com/api/qotd', headers={'Authorization': f'Token token={key}'})
quote = response.json()
phrase = quote["quote"]["body"]
autor = quote["quote"]["author"]

print(phrase)



translator = Translator(to_lang='es')
translation = translator.translate(phrase)
print(translation)
print(autor)

root = tk.Tk()
root.geometry("900x500")

root.title("Tu frase para Twiter")
# Crear una etiqueta para mostrar el texto
label = tk.Label(root, text="Hola, la frase de hoy es:")
label1 = tk.Label(root, text=phrase)
label1.config(anchor="center")
label2 = tk.Label(root, text=translation)
label2.config(anchor="center")
label3 = tk.Label(root, text=autor)
label3.config(anchor="center")

# Colocar la etiqueta en la ventana
label.pack()
label1.pack()
label2.pack()
label3.pack();
def copy_text(label):
    text = label["text"]
    pyperclip.copy(text)
    messagebox.showinfo("Información", "El texto se ha copiado al portapapeles.")

button = tk.Button(root, text="Copiar frase en español", command=lambda: copy_text(label2))
button.pack()

root.mainloop()




