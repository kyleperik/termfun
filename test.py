from termfun import start, draw

# Create an initial state
# This could literally be anything
initialState = (0, '')

# Function used to process one change in state
def step(state, char): return (state[0] + 1, state[1] + char)

def render(state):
    # The draw helper function lets you draw something anywhere
    #   on the screen, with optional color
    # x y str [fgcolor] [bgcolor]
    draw(0, 0, f'Frames since start: {state[0]}')
    draw(0, 1, f'Typed chars with color: {state[1]}', 1, 6)

# Put it all together, and start!
start(initialState, step, render)
