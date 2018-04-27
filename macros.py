# Brainfuck interpreter - Macros Handler

from lexer import tokenize

__built_in = ['+', '-', '>', '<', '.', ',', '[', ']', '#', '$']

def __find_macros (T):
    # T is token list
    # remove '$' macro definition in T
    # return updated T and M (macro definition list)
    T_ = [token for token in T if token [0] != '$']
    M_ = [token for token in T if token [0] == '$']
    M = [macro [1:] for macro in M_] # remove definition command '$'
    return (T_, M)

def __substitute_once (T, M):
    # T is token list (without macro definitions)
    # M is macro definitions of T
