from matplotlib.animation import FuncAnimation


def tile_2d(ttt, rows=10, cols=10):
    a, b, c = ttt.shape
    assert(a == rows*cols), "Wrong dimensions"
    return np.moveaxis(np.resize(ttt, (rows, cols, b, c)),
                       1, 2).reshape(rows*b, cols*c)

def retile_3d(lll, rows=10, cols=10):
    finalshape=(rows*cols, 5, 5)
    rn, cn = lll.shape
    a, b, c = finalshape
    # assert((rn/rows) * (rc/cols) == a), "Wrong dimensions"
    return np.moveaxis(lll.reshape(rows, b, cols, c), 1, 2).reshape(finalshape)
    return np.moveaxis(lll.reshape(rows, b, cols, c), 1, 2).reshape(finalshape)


marked_numbers = np.zeros_like(boards, dtype=bool)
unfilled_boards = np.ones(len(boards), dtype=bool)
winning_boards = []
n_board = []

r = np.zeros_like(boards, dtype='uint8')
g = np.copy(tile_2d(marked_numbers))
b = tile_2d(np.zeros_like(boards, dtype='uint8'))
img = 250*np.stack((tile_2d(r), g, b), axis=-1)

fig, ax = plt.subplots()
bingo = ax.imshow(img)#, cmap="tab10")
ax.set_xticks(np.arange(-.5, 51, 5))
ax.set_xticklabels("")
ax.set_yticks(np.arange(-.5, 51, 5))
ax.set_yticklabels("")
ax.set_xticks(np.arange(-.5, 50, 1), minor=True)
ax.set_xticklabels("", minor=True)
ax.set_yticks(np.arange(-.5, 50, 1), minor=True)
ax.set_yticklabels("", minor=True)
ax.grid(which='major', linewidth=3, color='dimgray', linestyle='-')
ax.grid(which='minor', linewidth=.5, color='gray', linestyle='-')
def update(num):
    global boards, marked_numbers, sequence, unfilled_boards, n_board, winning_boards, r, b, ax
    broj = sequence[num]
    marked_numbers[boards==broj] = True
    column_filled = np.sum(marked_numbers, axis=1)==5
    line_filled = np.sum(marked_numbers, axis=2)==5

    if np.sum(line_filled[unfilled_boards])>0:
        n_board = list(np.intersect1d(np.where(line_filled)[0],np.where(unfilled_boards)[0]))
        unfilled_boards[n_board] = False
        if len(winning_boards) > 0:
            kokoska = winning_boards + n_board
            winning_boards = list(set(kokoska))
        else:
            winning_boards = n_board

    elif np.any(column_filled[unfilled_boards]):
        n_board = list(set(np.where(column_filled)[0]).intersection(set(np.where(unfilled_boards)[0])))
        unfilled_boards[n_board] = False
        if len(winning_boards) > 0:
            kokoska = winning_boards + n_board
            winning_boards = list(set(kokoska))
        else:
            winning_boards = n_board
    r[winning_boards] = True
    g = np.copy(250*tile_2d(marked_numbers).astype(int))
    maska = np.zeros_like(marked_numbers, dtype=bool)
    maska[winning_boards] = True
    g[tile_2d(maska)]//=2
    img = np.stack((35*tile_2d(r).astype(int), g, g), axis=-1) 
    bingo.set_data(img)
    bingo.set_clim(0, 255)
    ax.set_title(f"{num+1}. Number: {broj:2d} \n"
                 f"{n_board}\n"
                 f"{len(winning_boards)}/100 winning boards")
    plt.draw()



ani = FuncAnimation(fig, update, len(sequence),
                    # fargs=[boards, marked_numbers, sequence, unfilled_boards,
                    #        n_board, winning_boards, r, b, ax],
                    interval=350, blit=False, repeat=False)
# ani.save("visualisations/day04_bingo.gif")