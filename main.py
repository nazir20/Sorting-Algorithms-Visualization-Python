# needed libraries
from tkinter import *
import tkinter.ttk
from sorting_algorithms import *
import random

root = Tk()
root.title('Sorting Algorithms Visualization')
root.geometry('900x600')
root.config(background='#fff')

# variables
dataset = []
stop_flag = False
sorting_algorithm = StringVar()


# Buttons
def start_btn():
    global dataset, stop_flag
    if stop_flag:
        stop_flag = False
    if sorting_algorithm.get() == 'Bubble Sort':
        SortingAlgorithms.bubble_sort(dataset, draw_data, animation_speed.get(), stop_flag)
    # this part will be updated


def stop_btn():
    global stop_flag
    stop_flag = True


def reset_btn():
    global dataset
    dataset = []
    draw_data(dataset, [])


# Data manipulation
def draw_data(data_set, clr):
    cv.delete('all')
    cv_height = 380
    cv_width = 700
    x_width = cv_width / (len(data_set) + 1)
    offset = 30
    space_between = 5
    data = [i / max(data_set) for i in data_set]

    for i, h in enumerate(data):
        x0 = i * x_width + offset + space_between
        y0 = cv_height - h * 320
        x1 = (i + 1) * x_width + offset
        y1 = cv_height

        cv.create_rectangle(x0, y0, x1, y1, fill=clr[i])
        cv.create_text(x0 + 2, y0, anchor=SW, text=str(data_set[i]))

    root.update_idletasks()


def generate_dataset():
    global dataset
    min_val = int(dataset_min_value.get())
    max_val = int(dataset_max_value.get())
    data_size = int(dataset_size.get())

    dataset = []
    for i in range(data_size):
        dataset.append(random.randrange(min_val, max_val + 1))
    # draw data
    draw_data(dataset, ['#FF597B' for i in range(len(dataset))])


# GUI Setup
sidebar_fr = Frame(root, width=220, height=230, background='#ECF2FF')
sidebar_fr.grid(row=0, column=0, rowspan=3, sticky='ns')

header = Frame(root, width=820, height=130, background='#F3F1F5', padx=0, pady=0)
header.grid(row=0, column=1, padx=0, pady=5, columnspan=1)

cv = Canvas(root, width=820, height=480, background='#fff')
cv.grid(row=1, column=1, padx=0, pady=5, columnspan=1)

combobox = tkinter.ttk.Combobox(sidebar_fr, values=['Bubble Sort', 'Quick Sort'], textvariable=sorting_algorithm)
combobox.grid(row=1, column=0, padx=5, pady=5)
combobox.current(0)


dataset_size = Scale(sidebar_fr, from_=3, to=50, resolution=1, orient=HORIZONTAL, label="Dataset Size", background='#fff', length=150)
dataset_size.grid(row=2, column=0, padx=5, pady=5, sticky=W)

dataset_min_value = Scale(sidebar_fr, from_=1, to=100, resolution=1, orient=HORIZONTAL, label="Minimum Value", background='#fff', length=150)
dataset_min_value.grid(row=3, column=0, padx=5, pady=5, sticky=W)

dataset_max_value = Scale(sidebar_fr, from_=100, to=1000, resolution=1, orient=HORIZONTAL, label="Maximum Value", background='#fff', length=150)
dataset_max_value.grid(row=4, column=0, padx=5, pady=5, sticky=W)

animation_speed = Scale(sidebar_fr, from_=0.1, to=5.0, length=150, digits=2, resolution=0.1, orient=HORIZONTAL, label='Select Speed(sec)', background='#fff')
animation_speed.grid(row=5, column=0, padx=5, pady=5, sticky=W)

Button(sidebar_fr, text='Generate Dataset', command=generate_dataset, bg='#764AF1', fg='white', width=20).grid(row=6, column=0, padx=5, pady=5)
Button(sidebar_fr, text='Start', command=start_btn, bg='#019267', fg='white', height=1, width=20).grid(row=7, column=0, padx=5, pady=5)
Button(sidebar_fr, text='Reset', command=reset_btn, bg='#FF597B', fg='white', height=1, width=20).grid(row=8, column=0, padx=5, pady=5)
Button(sidebar_fr, text='Stop', command=stop_btn, bg='orange', fg='white', height=1, width=20).grid(row=9, column=0, padx=5, pady=5)

# start the main event loop of the Application
root.mainloop()
