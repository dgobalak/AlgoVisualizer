import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import sys


x_axis = [x for x in range(50)]
y_axis = [y for y in range(50)]
random.shuffle(y_axis)

c = count()

def animate(a):
    if a == len(y_axis):
        sys.exit()
    plt.clf()
    bar = plt.bar(x_axis, y_axis,color="black", edgecolor="black")
    selection_sort(y_axis, a, bar)


def selection_sort(y_axis, a, bar):
    bar[a].set_color('red')
    bar[a].set_edgecolor('red')
    min_i, min_val = a, 1E10
    for i in range(a, len(y_axis)):
        if y_axis[i] <= min_val:
            min_val = y_axis[i]
            min_i = i
    y_axis[min_i], y_axis[a] = y_axis[a], y_axis[min_i]
    bar[min_i].set_color('green')
    bar[min_i].set_edgecolor('green')


ani = FuncAnimation(plt.gcf(), animate, blit=False, frames=c, repeat=True)
plt.show()