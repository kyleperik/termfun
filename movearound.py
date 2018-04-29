from termfun.start import start, draw

start(
    (10, 10),
    lambda state, char: (
        state[0] + (1 if char in ['l', 'u', 'n'] else -1 if char in ['h', 'y', 'b'] else 0),
        state[1] + (1 if char in ['j', 'b', 'n'] else -1 if char in ['k', 'y', 'u'] else 0)
    ),
    lambda state: draw(*state, '@')
)
