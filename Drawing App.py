import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing App")

        self.canvas = tk.canvas(self.master, bg="white", width=500, height=500)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.button_clear = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        self.button_clear.pack(side=tk.BOTTOM)

        self.button_clear = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        self.button_clear.pack(side=tk.BOTTOM)

        self.old_x = None
        self.olf_y = None

        self.canvas.bind('<B1-Motion>' , self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        

