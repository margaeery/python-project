import tkinter as tk

def show_selection(event):
    selected = listbox.get(listbox.curselection())
    label.config(text=f"Выбрано: {selected}")

root = tk.Tk()
root.title("Выбор животного")
root.geometry("250x250")

listbox = tk.Listbox(root)
animals = ["Кот", "Собака", "Шиншилла", "Попугай", "Хомяк", "Рыбка",
    "Кролик", "Морская свинка", "Черепаха", "Ящерица", "Змея"]
for animal in animals:
    listbox.insert(tk.END, animal)

listbox.pack(pady=20)
listbox.bind('<<ListboxSelect>>', show_selection)

label = tk.Label(root, text="Выберите животное")
label.pack()

root.mainloop()
