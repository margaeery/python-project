import tkinter as tk
from tkinter import filedialog


def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        label.config(text=f"Выбран: {file_path}")


root = tk.Tk()
root.title("Выбор файла")
root.geometry("400x100")

button = tk.Button(root, text="Выбрать файл", command=select_file)
button.pack(pady=20)

label = tk.Label(root, text="Файл не выбран")
label.pack()

root.mainloop()
