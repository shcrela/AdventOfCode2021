%matplotlib tk
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from visualisations.scripts.day01_show_depth import show_depth

scanned_depths = np.loadtxt("data/day01a.txt")
show_depth(scanned_depths, title="Dive", xlabel="")

positions_arr = np.array(positions)
positions_arr[:,1] *=-1
ax = plt.gca()
fig = plt.gcf()
submarine, = ax.plot(positions_arr[0,0], positions_arr[0,1], ">r", ms=12)

n_positions = len(positions_arr)
def update(num, positions_arr, ax):
    submarine.set_data(positions_arr[num, 0], positions_arr[num, 1])
    ax.set_title(f"Position N° {num} / {n_positions}")



ani = FuncAnimation(fig, update, n_positions, fargs=[positions_arr, ax],
                    interval=50, blit=False)
plt.show()

# ani.save("visualisations/day02a_submarine.gif", dpi=80)