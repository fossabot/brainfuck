# Brainfuck interpreter in Python
# -------------------------------
# Additional (anti-)features:
# 1. Comments must start with '#'
# 2. Macros can be any bf+ snippet with identifier [a-zA-Z_]+
# 3. Use macros with keyword '$'
# ------------------------------
# Keywords for parsing:
# + # Incre 1 to current cell
# - # Decre 1 to current cell (if current cell > 0)
# > # Move instruction pointer right a cell
# < # Move instruction pointer left a cell (if current cell index != 0)
# . # Output current cell decoded in Ascii
# , # Input to current cell Ascii encoded
# [ # Start loop at current cell (if current cell > 0)
# ] # Match loop-start
# --------------------
# Cell representation: int list with infinite right-append
# Loop control: program counter
# -----------------------------
# Lexing:
# 1. def process code snippet - remove comments, whitespaces
# 2. Tokenize (including macros)
# 3. Interpret macros (process and substitute)
# 4. Do above until there is no macros

