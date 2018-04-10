# Termfun

Make making terminal games fun. Also functional.

# Usage

```
from termfun import start

start(
	0, # State: could be literally anything
	lambda s, c: s + 1, # Step: function used to process one change in state
)   lambda s: print(s) # Render: render your state here
```