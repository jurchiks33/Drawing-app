import tkinter as tk

class DrawingApp;
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing App")

        self.canvas = tk.canvas(self.master, bg="white", width=500, height=500)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.button_clear = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        self.button_clear.pack(side=tk.BOTTOM)