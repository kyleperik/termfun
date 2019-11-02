from termfun import start, draw

start(
    (10, 10, 0, 0),
    lambda state, char: (
        state[0],
        state[1],
        state[2] + (1 if char in ['l', 'u', 'n'] else -1 if char in ['h', 'y', 'b'] else 0) * 0.5,
        state[3] + (1 if char in ['j', 'b', 'n'] else -1 if char in ['k', 'y', 'u'] else 0) * 0.5
    ),
    lambda state: draw(round(state[0]), round(state[1]), '@'),
    lambda state: (
        state[0] + state[2],
        state[1] + state[3],
        state[2] * 0.9,
        state[3] * 0.9,
    ),
    fps=30
)
