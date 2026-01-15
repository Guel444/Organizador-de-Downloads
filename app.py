import tkinter as tk
from tkinter import messagebox

from main import mapear_arquivos, organizar


def simular():
    arquivos = mapear_arquivos()
    total = sum(len(lista) for lista in arquivos.values())

    if total == 0:
        messagebox.showinfo('Simulação', 'Nenhum arquivo para organizar.')
        return

    resumo = '\n'.join(
        f'{pasta}: {len(lista)} arquivo(s)'
        for pasta, lista in arquivos.items()
        if lista
    )

    messagebox.showinfo(
        'Simulação',
        f'{total} arquivos encontrados:\n\n{resumo}'
    )


def executar():
    arquivos = mapear_arquivos()
    total = sum(len(lista) for lista in arquivos.values())

    if total == 0:
        messagebox.showinfo('Organizar', 'Nada para organizar.')
        return

    if not messagebox.askyesno(
        'Confirmação',
        f'{total} arquivos serão movidos.\nDeseja continuar?'
    ):
        return

    organizar(arquivos)
    messagebox.showinfo('Concluído', 'Downloads organizados com sucesso!')


root = tk.Tk()
root.title('Organizador de Downloads')
root.geometry('320x200')
root.resizable(False, False)

tk.Label(
    root,
    text='Organizador de Downloads',
    font=('Arial', 12, 'bold')
).pack(pady=10)

tk.Button(root, text='🔍 Simular', width=25, command=simular).pack(pady=5)
tk.Button(root, text='📂 Organizar', width=25, command=executar).pack(pady=5)
tk.Button(root, text='❌ Sair', width=25, command=root.destroy).pack(pady=5)

root.mainloop()
