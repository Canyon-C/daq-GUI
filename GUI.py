
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import time

root = tk.Tk()
root.configure(bg="black")

fig1, ax1 = plt.subplots(1, 1, figsize = (4, 4), tight_layout=True, layout="constrained")

fig2, ax2 = plt.subplots(1, 1,  figsize = (4, 4), tight_layout=True, layout="constrained")

ax1.set_title('Thrust')
ax1.set_xlabel("Raw Thrust: ")

ax2.set_title('Pressure')
ax2.set_xlabel("Raw Pressure: ")



topleft_frame = tk.Frame(root, bg='black')
topleft_frame.grid(row=0, column=0, rowspan=1, columnspan=1, sticky="nsew", pady=20, padx=20)
canvas1 = FigureCanvasTkAgg(fig1, master=topleft_frame)
canvas1.get_tk_widget().pack(fill="both", expand=True)
canvas1.draw()

bottomleft_frame = tk.Frame(root, bg='black')
bottomleft_frame.grid(row=1, column=0, rowspan=1, columnspan=1, sticky="nsew", pady=20, padx=20)
canvas2 = FigureCanvasTkAgg(fig2, master=bottomleft_frame)
canvas2.get_tk_widget().pack(fill="both", expand=True)

text_frame = tk.Frame(root, bg='black', padx= 10)
text_frame.grid(row=0, column=1, rowspan=1, columnspan=1, sticky="nsew")

current_file = tk.Label(text_frame, text=str("CURRENT_CSV_FILE"), font=('SF-Pro', 20), padx = 0, bg='black', fg='white')
current_file.grid(row=1, column=0, sticky="w", pady=50)

red_label = tk.Label(text_frame, text=str("Logging:"), font=('SF-Pro', 20), bg='black', fg='white')
red_label.grid(row=3, column=0, sticky="w")

canvas_circle = tk.Canvas(text_frame, width=50, height=50, bg='black', highlightthickness=0)
canvas_circle.grid(row=3, column=0, sticky="w", padx = 150)



green_label = tk.Label(text_frame, text=str("Continuity:"), font=('SF-Pro', 20), bg='black', highlightthickness=0, fg='white')
green_label.grid(row=2, column=0, sticky="w")

canvas_circle2 = tk.Canvas(text_frame, width=50, height=50, bg='black', highlightthickness=0)
canvas_circle2.grid(row=2, column=0, sticky="w", padx = 150)

def updatecircle():
    i = 0

    if i > 1:
        canvas_circle.create_oval(5, 5, 45, 45, width=2, fill="green")
    else:
        canvas_circle.create_oval(5, 5, 45, 45, width=2, fill="red")





root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

x_vals = [[] for _ in range(2)]
y_vals = [[] for _ in range(2)]
lines = [ax1.plot([], [])[0]]
lines2 = [ax2.plot([], [])[0]]
max_length = 67
start_time = time.perf_counter()

ax1.set_ylim([0, 500])
ax2.set_ylim([0, 1000])


def update_data():
    updatecircle()
    ellapsed_time = time.perf_counter() - start_time
    for j in range(2):
        if len(x_vals[j]) > max_length:
            x_vals[j].pop(0)
            y_vals[j].pop(0)

        value = random.randint(0, 500)
        x_vals[j].append(ellapsed_time)
        y_vals[j].append(value)

        lines[0].set_data(x_vals[j], y_vals[j])
        lines2[0].set_data(x_vals[j], y_vals[j])
        ax1.relim()
        ax2.relim()
        ax2.autoscale_view()
        ax1.autoscale_view()

    canvas1.draw()
    canvas2.draw()
    root.after(100, update_data)
  
update_data()
root.mainloop()