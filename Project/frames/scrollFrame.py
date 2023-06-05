import customtkinter as tk

class ScrollFrame(tk.CTkFrame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.CTkCanvas(self)
        scrollbar = tk.CTkScrollbar(self, orientation="vertical", command=canvas.yview)
        self.scroll_frame = tk.CTkFrame(canvas)

        self.scroll_frame.bind("<Configure>",lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.scroll_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
