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
# Loop control: loop stack
# -----------------------------
# Lexing:
# 1. def process code snippet - remove comments, whitespaces
# 2. Tokenize (including macros)
# 3. Interpret macros (process and substitute)
# 4. Do above until there is no macros

from lexer import tokenize
from macros import process_macros

from sys import argv
import os

__help_message = '''
-----------------------------------
Brainfuck with Macros (version 1.0)
[created by https://github.com/SAMFYB]
[see github source at https://github.com/SAMFYB/brainfuck]
----------------------------------------------------------
You need to supply a brainfuck program to run, like this:
    brainfuck hello_world.bf
To run in DEBUG mode:
    brainfuck program.bf -d
To see this help message:
    brainfuck
Enjoy!
------
'''.strip ()

if len (argv) <= 1:
    print (__help_message)
    os._exit (0)

program = argv [1]
__debug = False # debug mode

if len (argv) >= 3:
    if '-d' in argv:
        __debug = True

def __open_file (program):
    try:
        f = open (program.strip (), 'r')
    except:
        raise ValueError ('Brainfuck: program {name} does not exist.'.format (name = program))
    L = [line for line in f] # parse file
    T = tokenize (L)
    return T

T = __open_file (program) # initial tokens

base_path = os.path.dirname (program)
if len (base_path) > 0:
    base_path += '/'
T = process_macros (T, base_path) # substitute ALL macros

if __debug:
    print ('[DEBUG] processed token list: ' + str (T))
def __debug_token (s, i):
    if __debug:
        print ('[DEBUG] compute token {token} at index {index}'.format (token = s, index = i) + ' | ' + str (CELL))
    pass

# -----------------------------------------------------------------------------
# Interpreter begins here.

CELL = [0]
STACK = [] # append and pop at the end
cell_pointer = 0 # cell pointer
ins_pointer = 0 # instruction pointer

while (ins_pointer != len (T)): # pointer at len (T) program ends
    token = T [ins_pointer] # get command token
    __debug_token (token, ins_pointer)
    ins_pointer += 1 # increment instruction pointer to next instruction
    if token [0] == '$':
        # macro definition - ignore
        continue
    if token [0] == '+':
        while cell_pointer >= len (CELL):
            CELL.append (0)
        CELL [cell_pointer] += 1
        if CELL [cell_pointer] >= 128:
            CELL [cell_pointer] %= 128
        continue
    if token [0] == '-':
        while cell_pointer >= len (CELL):
            CELL.append (0)
        if CELL [cell_pointer] > 0:
            CELL [cell_pointer] -= 1
        continue
    if token [0] == '>':
        cell_pointer += 1
        while cell_pointer >= len (CELL):
            CELL.append (0)
        continue
    if token [0] == '<':
        if cell_pointer > 0:
            cell_pointer -= 1
        continue
    if token [0] == '#':
        # comment - ignore
        continue
    if token [0] == '.': # output current cell
        print (chr (CELL [cell_pointer]), end = '')
        continue
    if token [0] == ',': # accept an input int
        try:
            i = int (input ().strip ())
        except:
            raise ValueError ('Brainfuck: input is invalid.')
        i %= 128
        CELL [cell_pointer] = i
        continue
    if token [0] == '[': # start loop
        if CELL [cell_pointer] != 0: # execute loop
            STACK.append (ins_pointer) # push current instruction pointer
            continue
        # current cell is 0 - skip loop
        bracket_counter = 1
        while bracket_counter != 0:
            if T [ins_pointer] == '[':
                bracket_counter += 1
            elif T [ins_pointer] == ']':
                bracket_counter -= 1
            ins_pointer += 1
            continue
        # when bracket count is 0, ins_pointer is at next instruction after ']'
        continue # continue program execution
    if token [0] == ']': # loop back
        if len (STACK) == 0:
            raise ValueError ('Brainfuck: loop stack empty.')
        ins_pointer = STACK.pop () - 1 # move to '[' location
        continue
    raise ValueError ('Brainfuck: un-recognized command {c}'.format (c = token))

if __debug:
    print ('')
    print ('[DEBUG] program successfully exits.')
    print ('[DEBUG] data cells: ' + str (CELL))
    print ('[DEBUG] final data cell pointer: ' + str (cell_pointer))
    print ('[DEBUG] final stack has length ' + str (len (STACK)))

