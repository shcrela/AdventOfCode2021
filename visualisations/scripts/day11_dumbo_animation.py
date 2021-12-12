from matplotlib.animation import FuncAnimation

filename = "./data/day11a.txt"
with open(filename, 'r') as ff:
    data = ff.read()

puss = np.array([[int(x) for x in line] for line in data.split("\n")])

plt.close()
counter = 1000
fig, ax = plt.subplots()
dambo = ax.imshow(puss, vmin=0, vmax=35);

def update(num, puss, ax):
    puss+=1
    puss, broj = energize_neighbours(puss)
    slika = np.copy(puss)
    slika[slika==0] = 35
    
    dambo.set_data(slika)
    ax.set_title(f"Position N° {num}")



ani = FuncAnimation(fig, update, counter, fargs=[puss, ax],
                    interval=50, blit=False, repeat=True)
plt.show()

# ani.save("visualisations/day11a_Dambos.gif")