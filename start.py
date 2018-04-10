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

def main(state, render, step):
    print(term.clear)
    render(state)
    c = getchar()
    if ord(c) == 3:
        return
    nextstate = step(state, c)
    if nextstate is None: return
    return lambda: main(nextstate, render, step)

def start(state, step, render):
    print(
        term.enter_fullscreen,
        term.cursor_invisible
    )
    try:
        with term.hidden_cursor():
            r = lambda: main(state, render, step)
            while r is not None:
                r = r()
    finally:
        print(
            term.exit_fullscreen)
