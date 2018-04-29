# Termfun

Make making terminal games fun. Also functional.

# Usage

Get the repo, then install with `pip install ./`

Here's a test program, also included in `termfun/test`

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