from screeninfo import get_monitors


# gets the [0] (main) monitor and return one of it's characteristics

def get_sizes(which_one):
    primary_monitor = get_monitors()[0]
    if which_one == "width":
        return primary_monitor.width
    elif which_one == "heigth":
        return primary_monitor.height
    else:
        return None
