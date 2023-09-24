import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing App")

        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self.master, bg="white", width=500, height=500)
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
        self.selected_color = 'black'

        self.color_palette = tk.Frame(self.master)
        self.color_palette.pack(side=tk.RIGHT)

        for color in self.colors:
            color_circle = tk.Canvas(self.color_palette, bg=color, height=30, width=30)
            color_circle.pack(pady=5)
            color_circle.bind('<Button-1>', lambda e, color=color: self.set_color(color))

 
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

    def set_color(self, color):
        self.selected_color = color
    
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
