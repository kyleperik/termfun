# Termfun

Simple way to create a game in your terminal!

![Demo](https://raw.githubusercontent.com/kyleperik/termfun/master/demo.gif)

# Usage

Get the repo, then install with `pip install ./`

Here's a test program, also included in `test.py` as shown above

``` python
from termfun import start, draw

# Create an initial state
# This could literally be anything
initialState = (0, '')

# Function used to process one change in state
def step(state, char): return (state[0] + 1, state[1] + char)

# Run each frame to display the state
def render(state):
    # The draw helper function lets you draw something anywhere
    #   on the screen, with optional color
    # x y str [fgcolor] [bgcolor]
    draw(0, 0, f'Frames since start: {state[0]}')
    draw(0, 1, f'Typed chars with color: {state[1]}', 1, 6)

# Put it all together, and start!
start(initialState, step, render)
```

# What is this?

Essentially, this is a small framework, that lets you make a game or application in the terminal.

All you need to do is provide an initial state, a function that transforms your state and returns a new one each time a character is typed, and lastly, a function that is used just to render a given state on screen. Each "frame" the screen is cleared for the new rendering to take place. Also a draw function is made available as well.

Because you have to return a new state each round, it enables you to be more functional with your coding style. As opposed to a while loop like so, where you are forced to modify state each time.

``` python
state = 0
while True:
    state += 1
    draw(5, 5, state)
```

Termfun's approch makes it seem more like recursion (although underneath, it truly is a while loop to avoid a maximum recursion exceeded error)

For those of you who like nethack, it's easy to make a simple nethack like game, I included a small sample `movearound.py` with a simple player who moves around.

Although the examples here use simple lambda expressions, I'd suggest especially for a larger program that functions are split out or you will be eaten by a [velociraptor](https://www.xkcd.com/292/)

There's an optional function that will evaluate whether it will skip prompting for a character. Append it to the end of `start` like this `lambda state: state.skip`.

# Why?

I like functional programming and I wanted to make a simple game. I couldn't find any thing that would make that easy for me, so I made this just to make this easier for myself.

# Frames

The optional parameters `fps` and `step` are made available. Set `fps` to the desired frames per second, and `step` to a function which is processes the state each frame.