from termfun import start, draw

start(
    # State: can be anything
    (0, ''),
    # On Char: function used to process one character being entered
    lambda state, char: (state[0], state[1] + char),
    # Render: render your state here
    lambda state: draw(5, 5, f'{state[0]}  {state[1]}', 6, 8), # x, y, string, fgcolor, bgcolor
    # Step: Function to process state each frame
    lambda state: (state[0] + 1, state[1]),
    fps=10
)
