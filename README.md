# Termfun

Make making terminal games fun. Also functional.

# Usage

Get the repo, then install with `pip install ./`

Here's a test program, also included in `test.py`

```
from termfun.start import start, draw

start(
    # State: could be literally anything
    (0, ''),
    # Step: function used to process one change in state
    lambda state, char: (state[0] + 1, state[1] + char),
    # Render: render your state here
    lambda state: draw(5, 5, f'{state[0]}  {state[1]}', 6, 8) # x, y, string, fgcolor, bgcolor
)
```

# What is this?

Essentially, this is a small framework, that lets you make a game or application in the terminal.

All you need to do is provide an initial state, a function that transforms your state and returns a new one each time a character is typed, and lastly, a function that is used just to render a given state on screen. Each "frame" the screen is cleared for the new rendering to take place. Also a draw function is made available as well.

Because you have to return a new state each round, it enables you to be more functional with your coding style. As opposed to a while loop like so, where you are forced to modify state each time.

```
state = 0
while True:
    state += 1
    draw(5, 5, state)
```

Termfun's approch makes it seem more like recursion (although underneath, it truly is a while loop to avoid a maximum recursion exceeded error)

# Why?

I like functional programming and I wanted to make a simple game. I couldn't find any thing that would make that easy for me, so I made this just to make this easier for myself.
