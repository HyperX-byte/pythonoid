# Push argument as tkinter frame object
def center_window(screen,w=300, h=200):
    # get screen width and height
    ws = screen.winfo_screenwidth()
    hs = screen.winfo_screenheight()
    # calculate position x, y
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)
    screen.geometry('%dx%d+%d+%d' % (w, h, x, y))

