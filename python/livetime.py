from __future__ import division
import time
import pandas as pd

import numpy as np
import scipy.io

import drawnow
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
t = 0
data = pd.read_csv('data.csv')
y1 = data['x_value']
x = data['total_1']
def animate(i):
    data = pd.read_csv('Filtereddata.csv')
    temp=len(data['t'])
    y1 = data['f']
    x = data['t']
    plt.cla()
    
    plt.plot(x,y1)
    plt.xlim(x[temp-1]-3,x[temp-1])
    
    #plt.xlim(left=t-5,right=t-1)



t = len(x)
    #t=(x[t-1])
    
ani = FuncAnimation(plt.gcf(),animate,interval=30)
plt.show()    
        
   

