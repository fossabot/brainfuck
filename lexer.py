# Brainfuck interpret - Lexer

__built_in = ['+', '-', '>', '<', '.', ',', '[', ']', '#', '$']

def __remove_comments (L):
    # L is string list
    # truncates strings in L where comments start
    for i in range (len (L)):
        if '#' in L[i]:
            comment_start = L[i].find ('#') # find first occurance of '#'
            L[i] = L[i] [:comment_start] # slice string before comment_start
    return L

def __remove_whitespaces (L):
    # L is string list (without comments)
    # removes empty lines & whitespaces around lines
    L = [line.strip () for line in L] # remove whitespaces around
    L = [line for line in L if len (line) > 0] # remove empty lines
    return L

def __tokenize (L):
    # L is string list (without comments & empty lines)
    # LL is string list list (without whitespaces)
    LL = [[token.strip () for token in line.split (' ')] for line in L]
    for line in LL:
        line = [token for token in line if len (token) > 0] # remove empty token
    T = []
    for line in LL:
        for token in line:
            # check if token is string of built-in commands
            if token [0] in __built_in:
                # add individual chars into token list
                for c in token:
                    T.append (c)
            else:
                # add entire token into token list
                T.append (token)
    return T

def tokenize (L): # public version of tokenize
    # L is string list (no requires)
    # returns token list
    L = __remove_comments (L)
    L = __remove_whitespaces (L)
    T = __tokenize (L)
    return T

