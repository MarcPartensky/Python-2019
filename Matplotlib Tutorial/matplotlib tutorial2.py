import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import random

style.use("fivethirtyeight")
fig=plt.figure()
ax1=fig.add_subplot(1,1,1)

x=[i for i in range(100)]


def animate(i):
    y=[random.randint(0,10) for i in range(100)]
    ax1.clear()
    ax1.plot(x,y)

ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
