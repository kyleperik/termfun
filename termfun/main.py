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

def main(state, render, step, onchar, skip, fps, i):
    print(term.clear)
    render(state)
    if fps: sleep(60 / fps / 100)
    c = (
        (' ' if skip(state) else i.escape_code())
        if fps is None
        else i.char()
    )
    if c is None and fps is None:
        return
    # Process all chars hit
    charstate = state
    if fps is not None:
        while c:
            charstate = onchar(charstate, c)
            c = i.char()
    else:
        charstate = onchar(charstate, c or ' ')
    nextstate = step(charstate)
    if nextstate is None: return
    return lambda: main(nextstate, render, step, onchar, skip, fps, i)

def start(state, onchar, render, step=lambda s: s, skip=lambda x: False, fps=None):
    print(
        term.enter_fullscreen,
        term.cursor_invisible
    )
    try:
        with term.hidden_cursor():
            with (NonBlockingInput() if fps else BlockingInput()) as nbi:
                r = lambda: main(state, render, step, onchar, skip, fps, nbi)
                while r is not None:
                    r = r()
    finally:
        print(
            term.exit_fullscreen)
