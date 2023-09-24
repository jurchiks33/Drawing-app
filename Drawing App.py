import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing App")

        self.canvas = tk.Canvas(self.master, bg="white", width=500, height=500)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.button_clear = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        self.button_clear.pack(side=tk.BOTTOM)

        self.old_x = None
        self.old_y = None

        self.canvas.bind('<B1-Motion>' , self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def paint(self, event):
        x, y = event.x, event.y
        if self.old_x and self.old_y:
            self.canvas.create_line((self.old_x, self.old_y, x, y), width=2, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = x
        self.old_y = y    

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def clear_canvas(self):
        self.canvas.delete("all")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
