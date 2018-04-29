from blessings import Terminal

term = Terminal()

# cred https://gist.github.com/jasonrdsouza/1901709
def getchar():
    #Returns a single character from standard input
    import tty, termios, sys
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def draw(x, y, v, color=7, bgcolor=None):
    s = str(v)
    for i, line in enumerate(s.splitlines()):
        with term.location(x, y + i):
            print(
                term.color(color)(
                    term.on_color(bgcolor)(line)
                    if bgcolor is not None
                    else line
                )
            )

def main(state, render, step, skip):
    print(term.clear)
    render(state)
    c = getchar() if not skip(state) else ' '
    if ord(c) == 3:
        return
    nextstate = step(state, c)
    if nextstate is None: return
    return lambda: main(nextstate, render, step, skip)

def start(state, step, render, skip=lambda x: False):
    print(
        term.enter_fullscreen,
        term.cursor_invisible
    )
    try:
        with term.hidden_cursor():
            r = lambda: main(state, render, step, skip)
            while r is not None:
                r = r()
    finally:
        print(
            term.exit_fullscreen)
