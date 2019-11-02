from blessings import Terminal
from termfun.nbinput import BlockingInput, NonBlockingInput

from time import sleep

term = Terminal()

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

def main(state, render, step, skip, fps, i):
    c = (i.escape_code() if not skip(state) else ' ') if fps is None else i.char()
    # Clear the rest of the chars queued, if any
    if type(i) is NonBlockingInput:
        cleared_c = c
        while cleared_c: cleared_c = i.char()
    if c is None and fps is None:
        return
    nextstate = step(state, c or ' ')
    if nextstate is None: return
    print(term.clear)
    render(nextstate)
    if fps: sleep(60 / fps / 100)
    return lambda: main(nextstate, render, step, skip, fps, i)

def start(state, step, render, skip=lambda x: False, fps=None):
    print(
        term.enter_fullscreen,
        term.cursor_invisible
    )
    try:
        with term.hidden_cursor():
            with (NonBlockingInput() if fps else BlockingInput()) as nbi:
                r = lambda: main(state, render, step, skip, fps, nbi)
                while r is not None:
                    r = r()
    finally:
        print(
            term.exit_fullscreen)
