import customtkinter as tk
import controller
tk.set_default_color_theme("custom_theme.json")


if __name__ == '__main__':
    root=tk.CTk()
    root.geometry("1280x768")
    root.title("Cumbaya")
    root.resizable(False, False)
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)


    control = controller.Controller(root)
    root.mainloop()