
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation #it makes an animation by repeatedly calling a function function
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

plt.style.use('fivethirtyeight')

xvalues = []
yvalues = []

index = count() #you take real time ecg signals from there


def plotting(i):
    xvalues.append(next(index))
    yvalues.append() # there might be y values
    plt.cla()  # clears the axe
    plt.plot(xvalues, yvalues)
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), plotting, interval=1000)

plt.tight_layout()
plt.show()