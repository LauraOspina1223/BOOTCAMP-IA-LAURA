# ui.py
# Capa de interfaz gráfica (Tkinter)

import tkinter as tk
from tkinter import filedialog, messagebox
from controller import procesar_instruccion
from processor import process_excel_safe



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
    # Ventana principal
    root = tk.Tk()
    root.title("Procesador Excel con IA")
    root.geometry("500x300")

    # Etiqueta
    tk.Label(root, text="Escriba una instrucción en lenguaje natural").pack(pady=10)

    # Campo de texto
    entrada = tk.Entry(root, width=60)
    entrada.pack(pady=5)

    # Acción del botón
    def ejecutar():
        texto = entrada.get()
        exito, mensaje = procesar_instruccion(texto,path)

        if exito:
            messagebox.showinfo("Resultado", mensaje)
        else:
            messagebox.showerror("Error", mensaje)

    # Botón
    tk.Button(root, text="Abrir archivo", command=on_clic_procesar).pack(pady=20)
    tk.Button(root, text="Ejecutar instrucción", command=ejecutar).pack(pady=20)
    root.mainloop()

