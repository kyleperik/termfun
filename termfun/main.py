from blessings import Terminal
from termfun.nbinput import BlockingInput

term = Terminal()

# cred https://gist.github.com/jasonrdsouza/1901709
def getchar():
    with BlockingInput() as bi:
        return bi.escape_code()

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
    if c is None:
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
