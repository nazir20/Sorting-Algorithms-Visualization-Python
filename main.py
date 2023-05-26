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
graph_type = StringVar()
sorting_alg = SortingAlgorithms()


# Buttons
def start_btn():

    global dataset, stop_flag
    generateBtn.config(state=DISABLED)
    startBtn.config(state=DISABLED)
    stopBtn.config(state=NORMAL)
    resetBtn.config(state=DISABLED)

    if stop_flag:
        stop_flag = False
    if sorting_algorithm.get() == 'Bubble Sort':
        sorting_alg.bubble_sort(dataset, draw_data, animation_speed.get(), stop_flag)
        update_header_labels(sorting_alg.get_comparisons_count(), 'O(n^2)')

    elif sorting_algorithm.get() == 'Quick Sort':
        sorting_alg.quick_sort(dataset, 0, len(dataset) - 1, draw_data, animation_speed.get())
        draw_data(dataset, ['green' for i in range(len(dataset))])
        update_header_labels(sorting_alg.get_comparisons_count(), 'O(n log n)')

    elif sorting_algorithm.get() == 'Insertion Sort':
        sorting_alg.insertion_sort(dataset, draw_data, animation_speed.get())
        update_header_labels(sorting_alg.get_comparisons_count(), 'O(n^2)')

    elif sorting_algorithm.get() == 'Selection Sort':
        sorting_alg.selection_sort(dataset, draw_data, animation_speed.get())
        update_header_labels(sorting_alg.get_comparisons_count(), 'O(n^2)')

    elif sorting_algorithm.get() == 'Merge Sort':
        sorting_alg.merge_sort(dataset, draw_data, animation_speed.get())
        draw_data(dataset, ['green' for i in range(len(dataset))])
        update_header_labels(sorting_alg.get_comparisons_count(), 'O(n^2)')

    generateBtn.config(state=NORMAL)
    startBtn.config(state=NORMAL)
    stopBtn.config(state=DISABLED)
    resetBtn.config(state=NORMAL)


def stop_btn():
    global stop_flag
    stop_flag = True


def reset_btn():
    global dataset
    dataset = []
    comparison_label.config(text="")
    algorithm_complexity_label.config(text="")
    draw_data(dataset, [])


# A utility function to draw the dataset. It can draw the dataset in 3 different ways:
# 1. Bar
# 2. Scatter
# 3. Stem
def draw_data(data_set, clr):

    if graph_type.get() == 'Bar':
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

    elif graph_type.get() == 'Stem':
        cv.delete('all')
        cv_height = 380
        cv_width = 700
        x_width = cv_width / (len(data_set) + 1)
        offset = 30
        data = [i / max(data_set) for i in data_set]

        for i, h in enumerate(data):
            x = i * x_width + offset
            y = cv_height - h * 320

            cv.create_line(x, cv_height, x, y, fill=clr[i], width=2)
            cv.create_oval(x - 2, y - 2, x + 2, y + 2, fill=clr[i])
            cv.create_text(x + 5, y - 5, anchor=SW, text=str(data_set[i]))

    elif graph_type.get() == 'Scatter':
        cv.delete('all')
        cv_height = 380
        cv_width = 700
        x_width = cv_width / (len(data_set) + 1)
        offset = 30
        data = [i / max(data_set) for i in data_set]

        for i, h in enumerate(data):
            x = i * x_width + offset
            y = cv_height - h * 320

            cv.create_oval(x - 2, y - 2, x + 2, y + 2, fill=clr[i])
            cv.create_text(x + 5, y - 5, anchor=SW, text=str(data_set[i]))

    root.update_idletasks()


# A utility function to generate a dataset with random numbers
# this function is called in case the user did not enter any values through entry
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


# A utility function to show the comparisons count and time
# complexity of a sorting algorithm to user
def update_header_labels(comparisons_count, time_complexity):
    comparison_label.config(text=f"Comparisons Count: {comparisons_count}")
    algorithm_complexity_label.config(text=f"Algorithm Complexity: {time_complexity}")


def process_input():
    global dataset
    user_input = entry.get()
    # Process the input array
    array = [int(x) for x in user_input.split(",")]
    dataset = []
    # copying the entry values into our dataset
    for i in array:
        dataset.append(i)
    # draw data
    draw_data(dataset, ['#FF597B' for i in range(len(dataset))])
    # make the entry empty after its processed
    entry.delete(0, END)


# GUI Setup
sidebar_fr = Frame(root, width=220, height=230, background='#ECF2FF')
sidebar_fr.grid(row=0, column=0, rowspan=3, sticky='ns')

header = Frame(root, width=820, height=130, background='#F3F1F5', padx=0, pady=0)
header.grid(row=0, column=1, padx=0, pady=5, columnspan=1)

comparison_label = Label(header, text="", bg='#fff', font=('consolas', 14, "bold"), pady=12)
comparison_label.pack()

algorithm_complexity_label = Label(header, text="", bg='#fff', font=('consolas', 14, "bold"), pady=12)
algorithm_complexity_label.pack()

cv = Canvas(root, width=820, height=480, background='#fff')
cv.grid(row=1, column=1, padx=0, pady=5, columnspan=1)

sorting_algo = tkinter.ttk.Combobox(sidebar_fr, values=['Sorting Algorithm', 'Bubble Sort', 'Quick Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort'], textvariable=sorting_algorithm)
sorting_algo.grid(row=1, column=0, padx=5, pady=5)
sorting_algo.current(0)

graph = tkinter.ttk.Combobox(sidebar_fr, values=['Graph Type', 'Bar', 'Scatter', 'Stem'], textvariable=graph_type)
graph.grid(row=2, column=0, padx=5, pady=5)
graph.current(0)

dataset_size = Scale(sidebar_fr, from_=3, to=50, resolution=1, orient=HORIZONTAL, label="Dataset Size", background='#fff', length=150)
dataset_size.grid(row=3, column=0, padx=5, pady=5, sticky=W)

dataset_min_value = Scale(sidebar_fr, from_=1, to=100, resolution=1, orient=HORIZONTAL, label="Minimum Value", background='#fff', length=150)
dataset_min_value.grid(row=4, column=0, padx=5, pady=5, sticky=W)

dataset_max_value = Scale(sidebar_fr, from_=100, to=1000, resolution=1, orient=HORIZONTAL, label="Maximum Value", background='#fff', length=150)
dataset_max_value.grid(row=5, column=0, padx=5, pady=5, sticky=W)

animation_speed = Scale(sidebar_fr, from_=0.1, to=5.0, length=150, digits=2, resolution=0.1, orient=HORIZONTAL, label='Select Speed(sec)', background='#fff')
animation_speed.grid(row=6, column=0, padx=5, pady=5, sticky=W)

generateBtn = Button(sidebar_fr, text='Generate Dataset', command=generate_dataset, bg='#764AF1', fg='white', width=20)
generateBtn.grid(row=7, column=0, padx=5, pady=5)
startBtn = Button(sidebar_fr, text='Start', command=start_btn, bg='#019267', fg='white', height=1, width=20)
startBtn.grid(row=8, column=0, padx=5, pady=5)
resetBtn = Button(sidebar_fr, text='Reset', command=reset_btn, bg='#FF597B', fg='white', height=1, width=20)
resetBtn.grid(row=9, column=0, padx=5, pady=5)
stopBtn = Button(sidebar_fr, text='Stop', command=stop_btn, bg='orange', fg='white', height=1, width=20, state=DISABLED)
stopBtn.grid(row=10, column=0, padx=5, pady=5)


Label(sidebar_fr, text="---------Or---------", bg='#ECF2FF', font=('consolas', 10, "bold")).grid(row=11, column=0, padx=5, pady=5)
Label(sidebar_fr, text="Enter numbers(,)", bg='#ECF2FF', font=('consolas', 10, "bold")).grid(row=12, column=0, padx=5, pady=5)
entry = Entry(sidebar_fr, width=25)
entry.grid(row=13, column=0, padx=5, pady=5)
Button(sidebar_fr, text="Process Input", height=1, width=20, fg='#fff', bg='purple', command=process_input).grid(row=14, column=0, padx=5, pady=5)


# start the main event loop of the Application
root.mainloop()
