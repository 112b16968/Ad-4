import tkinter as tk
import random
import time

def color_choice():
    number = random.randrange(0, 256)
    return number

window = tk.Tk()

def create_canvas(x, y):
    red = color_choice()
    green = color_choice()
    blue = color_choice()
    color = '#%02x%02x%02x' % (red, green, blue)
    canvas = tk.Canvas(window, bg=color, width=200, height=100)
    canvas.place(x=x, y=y)
    return canvas, color

def update_color(red_slider, green_slider, blue_slider):
    red = red_slider.get()
    green = green_slider.get()
    blue = blue_slider.get()
    color = '#%02x%02x%02x' % (red, green, blue)
    canvas2.config(bg=color)
    return color


def create_slider(x, y):
    scale = tk.Scale(window, from_=0, to=255, command=lambda _: update_color(red_slider, green_slider, blue_slider))
    scale.place(x=x, y=y)
    return scale


def create_button(x, y, slider):
    def increment_slider():
        current_value = slider.get()
        slider.set(current_value + 1)
        update_color(red_slider, green_slider, blue_slider)
    
    button = tk.Button(window, text="+1", command=increment_slider)
    button.place(x=x, y=y)
    return button

def check_color():
    color = update_color(red_slider, green_slider, blue_slider)
    if color == initial_color:
        end_time = time.time()
        elapsed_time = end_time - start_time
        time_label.config(text="TOTAL_TIME: {:.2f} seconds".format(elapsed_time))
    else:
        window.after(100, check_color)  

canvas1, initial_color = create_canvas(0, 0)
canvas2, _ = create_canvas(0, 400)

red_slider = create_slider(0, 150)
green_slider = create_slider(50, 150)
blue_slider = create_slider(100, 150)

red_button = create_button(0, 300, red_slider)
green_button = create_button(60, 300, green_slider)
blue_button = create_button(120, 300, blue_slider)

start_time = time.time()

time_label = tk.Label(window, text="")
time_label.place(x=0, y=500)  
  

window.after(100, check_color)  

window.mainloop()

