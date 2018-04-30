# Brainfuck interpreter - Lexer

__built_in = ['+', '-', '>', '<', '.', ',', '[', ']', '#', '$', '|']

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

def __token_break (token):
    # further break down token (extract macro definition or macro use)
    if len (token) == 0: # which should not happen
        return []
    if len (token) == 1: # no further break
        return [token]
    if (token[0] in __built_in) and (token[0] != '$'):
        return [token[0]] + __token_break (token[1:]) # break leftmost out
    if (token[0] == '$'): # leftmost is macro definition
        first_command = -1
        for i in range (len (token)): # try to find a command
            if token[i] in __built_in:
                first_command = i
                break
        if first_command == -1: # no command found
            return [token] # macro definition itself
        return [token[:first_command]] + __token_break (token[first_command:])
    # leftmost is macro use
    first_command = -1
    for i in range (len (token)):
        if token[i] in __built_in:
            first_command = i
            break
    if first_command == -1:
        return [token]
    return [token[:first_command]] + __token_break (token[first_command:])

def __tokenize (L):
    # L is string list (without comments & empty lines)
    # LL is string list list (without whitespaces)
    LL = [[token.strip () for token in line.split (' ')] for line in L]
    for line in LL:
        line = [token for token in line if len (token) > 0] # remove empty token
    T = []
    for line in LL:
        for token in line:
            broken_tokens = __token_break (token)
            for t in broken_tokens:
                T.append (t)
    return T

def tokenize (L): # public version of tokenize
    # L is string list (no requires)
    # returns token list
    L = __remove_comments (L)
    L = __remove_whitespaces (L)
    T = __tokenize (L)
    return T

