# interface.py
import tkinter as tk
from tkinter import messagebox
from gerador_cpf import gerar_cpf
from verificador_cpf import verificar_cpf

def gerar_cpf_interface():
    cpf_gerado = gerar_cpf()
    entry_gerado.delete(0, tk.END)
    entry_gerado.insert(0, cpf_gerado)

def verificar_cpf_interface():
    cpf = entry_verificar.get()
    if verificar_cpf(cpf):
        messagebox.showinfo("Resultado", f"{cpf} é válido.")
    else:
        messagebox.showerror("Resultado", f"{cpf} é inválido.")

# Configuração da interface gráfica
root = tk.Tk()
root.title("Gerador e Verificador de CPF")

# Seção para geração de CPF
frame_gerador = tk.Frame(root, padx=10, pady=10)
frame_gerador.pack(pady=10)

label_gerador = tk.Label(frame_gerador, text="Gerar CPF:")
label_gerador.grid(row=0, column=0, padx=5, pady=5)

entry_gerado = tk.Entry(frame_gerador, width=20)
entry_gerado.grid(row=0, column=1, padx=5, pady=5)

btn_gerar = tk.Button(frame_gerador, text="Gerar", command=gerar_cpf_interface)
btn_gerar.grid(row=0, column=2, padx=5, pady=5)

# Seção para verificação de CPF
frame_verificador = tk.Frame(root, padx=10, pady=10)
frame_verificador.pack(pady=10)

label_verificar = tk.Label(frame_verificador, text="Verificar CPF:")
label_verificar.grid(row=0, column=0, padx=5, pady=5)

entry_verificar = tk.Entry(frame_verificador, width=20)
entry_verificar.grid(row=0, column=1, padx=5, pady=5)

btn_verificar = tk.Button(frame_verificador, text="Verificar", command=verificar_cpf_interface)
btn_verificar.grid(row=0, column=2, padx=5, pady=5)

root.mainloop()
