import tkinter as tk


class WindowApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Приложение с окнами")
        self.root.geometry("300x200")

        self.second_window = None
        self.third_window = None

        self.setup_main_window()

    def setup_main_window(self):
        label = tk.Label(self.root, text="Главное окно")
        label.pack(pady=40)

        btn = tk.Button(
            self.root,
            text="Открыть второе окно",
            command=self.open_second_window
        )
        btn.pack(pady=5)

        btn2 = tk.Button(
            self.root,
            text="Открыть третье окно",
            command=self.open_third_window
        )
        btn2.pack(pady=5)

    def open_second_window(self):
        if self.second_window and self.second_window.winfo_exists():
            self.second_window.lift()
        else:
            self.second_window = tk.Toplevel(self.root)
            self.second_window.title("Второе окно")
            self.second_window.geometry("250x150")

            label = tk.Label(self.second_window, text="Это второе окно")
            label.pack(pady=30)

            btn = tk.Button(
                self.second_window,
                text="Закрыть",
                command=self.second_window.destroy
            )
            btn.pack()

    def open_third_window(self):
        if self.third_window and self.third_window.winfo_exists():
            self.third_window.lift()
        else:
            self.third_window = tk.Toplevel(self.root)
            self.third_window.title("Третье окно")
            self.third_window.geometry("250x200")

            label = tk.Label(self.third_window, text="Это третье окно")
            label.pack(pady=20)

            self.label_text = tk.Label(self.third_window, text="Нажми кнопку!")
            self.label_text.pack(pady=10)

            btn = tk.Button(
                self.third_window,
                text="Изменить текст",
                command=lambda: self.label_text.config(text="Текст изменен!")
            )
            btn.pack(pady=10)

            btn_close = tk.Button(
                self.third_window,
                text="Закрыть",
                command=self.third_window.destroy
            )
            btn_close.pack()

    def run(self):
        self.root.mainloop()


app = WindowApp()
app.run()
