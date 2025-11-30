import tkinter as tk
from tkinter import filedialog, messagebox


def save_note():
    text = text_area.get("1.0", "end-1c")
    if text.strip():
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)
            messagebox.showinfo("Успех", "Заметка сохранена!")


def open_note():
    file_path = filedialog.askopenfilename(
        filetypes=[("Текстовые файлы", "*.txt")])
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        text_area.delete("1.0", "end")
        text_area.insert("1.0", text)


root = tk.Tk()
root.title("Заметки")
root.geometry("500x400")

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

save_btn = tk.Button(button_frame, text="Сохранить", command=save_note)
open_btn = tk.Button(button_frame, text="Открыть", command=open_note)

save_btn.pack(side="left", padx=5)
open_btn.pack(side="left", padx=5)

text_area = tk.Text(root, font=("Arial", 12))
text_area.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()
