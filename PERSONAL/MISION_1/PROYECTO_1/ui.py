# https://docs.python.org/3/library/tkinter.html

import tkinter as tk
from tkinter import filedialog, messagebox
from proccessor import process_excel_safe


def seleccionar_excel():
    return filedialog.askopenfilename(
    title = "Seleccionar archivo de Excel",
    filetypes = [("Archivos de Excel", "*.xlsx")]
    )
def on_clic_procesar():
    archivo = seleccionar_excel()
    exito,mensaje = process_excel_safe(archivo) # En el primero (exito) cargue el bool y en el segundo (mensaje) el mensaje
    if exito:
        messagebox.showinfo("Proceso completado", mensaje)
    else:
        messagebox.showerror("Error", mensaje)

def iniciar_app():
    root = tk.Tk()
    root.title("Procesador de archivos de Excel")
    root.geometry("400x400")
    root.resizable(False, False) # No permite redimensionar la ventana
    
    boton = tk.Button(
        root,
        text="Seleccionar archivo de Excel",
        command=on_clic_procesar,
        width=30,
        height=2
    )
    
    boton.pack(pady=60)
    root.mainloop()