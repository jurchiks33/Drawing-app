import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Drawing App")

        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.LEFT)

        self.canvas = tk.Canvas(self.master, bg="white", width=500, height=500)
        self.canvas.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)

        self.colors = ['red', 'blue', 'green', 'yellow', 'black', 'white']
        self.selected_color = 'black'

        self.color_palette = tk.Frame(self.master)
        self.color_palette.pack(side=tk.RIGHT)

        self.button_increase_brush = tk.Button(self.color_palette, text="+", command=self.increase_brush)
        self.button_increase_brush.pack()
        self.button_decrese_brush = tk.Button(self.color_palette, text="-", command=self.decrease_brush)
        self.button_decrese_brush.pack()

        self.brush_size = 2

        self.sticker_pallete = tk.Frame(self.master)
        self.sticker_pallete.pack(side=tk.RIGHT)

        self.stickers = []
        for i in range(1, 11):
            try:
                # Loading and resizing the image
                image = Image.open(f'sticker{i}.gif')
                resized_image = image.resize((37, 37), Image.LANCZOS)  # Resizing to 37x37 pixels
                sticker_image = ImageTk.PhotoImage(resized_image)
                self.stickers.append(sticker_image)
            except Exception as e:
                print(f"Error loading sticker{i}.gif: {e}")
        
        for i, sticker_image in enumerate(self.stickers):
            sticker_button = tk.Button(self.sticker_pallete, image=sticker_image, command=lambda i=i: self.set_sticker(i))
            sticker_button.pack()

        self.selected_sticker = None

        self.old_x = None
        self.old_y = None

        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        for color in self.colors:
            color_canvas = tk.Canvas(self.color_palette, bg='white', height=30, width=30)
            color_canvas.pack(pady=5)
            color_canvas.create_oval(5, 5, 25, 25, outline=color, fill=color)
            color_canvas.bind('<Button-1>', lambda e, color=color: self.set_color(color))
        
        self.button_clear = tk.Button(self.master, text="Clear", command=self.clear_canvas)
        self.button_clear.pack(side=tk.BOTTOM)


    def paint(self, event):
        x, y = event.x, event.y
        if self.selected_sticker:
            self.canvas.create_image(x, y, image=self.stickers[self.selected_sticker])
        elif self.old_x and self.old_y:
            self.canvas.create_line((self.old_x, self.old_y, x, y), width=self.brush_size, fill=self.selected_color, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.old_x = x
        self.old_y = y

    def reset(self, event):
        self.old_x = None
        self.old_y = None
    
    def clear_canvas(self):
        self.canvas.delete("all")

    def set_color(self, color):
        self.selected_color = color

    def set_sticker(self, index):
        self.selected_sticker = index    

    def increase_brush(self):
        self.brush_size += 1

    def decrease_brush(self):
        self.brush_size -= 1
        if self.brush_size < 1:
            self.brush_size = 1

    
if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()    

 
        
    

    

    
    
   
