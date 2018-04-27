# Brainfuck interpreter - Macros Handler

from lexer import tokenize

__built_in = ['+', '-', '>', '<', '.', ',', '[', ']', '#', '$']

def __find_macros (T):
    # T is token list
    # remove '$' macro definition in T
    # return updated T and M (macro definition list)
    T_ = [token for token in T if token [0] != '$']
    print (T_)
    M_ = [token for token in T if token [0] == '$']
    print (M_)
    M = [macro [1:] for macro in M_] # remove definition command '$'
    print (M)
    return (T_, M)

def __open_file (name):
    # name is string without '.bf' suffix
    file_path = name.strip () + '.bf'
    try:
        f = open (file_path, 'r')
    except:
        raise ValueError ('Brainfuck: macro definition does not exist.')
    L = [line for line in f] # parse file
    T = tokenize (L)
    f.close ()
    return T

def __substitute_once (T, M):
    # T is token list (without macro definitions)
    # M is macro definitions of T
    M = list (set (M)) # remove duplicate definitions
    MACROS = {} # M definition as key, token list as value
    print (M)
    for macro in M:
        macro_tokens = __open_file (macro)
        MACROS [macro] = macro_tokens
    for A in MACROS:
        for B in MACROS: # pairwise loop
            if A != B: # distinct items
                if (A in MACROS [B]) and (B in MACROS [A]):
                    # mutual recursive definition - not allow!
                    raise ValueError ('Brainfuck: mutually recursive macro definition in {_A} and {_B}'.format (_A = A, _B = B))
    S = [] # substituted new token list
    for token in T:
        if token [0] in __built_in: # a regular built-in command
            S.append (token)
        else:
            if token not in MACROS: # definition non-exist
                raise ValueError ('Brainfuck: cannot find macro definition of {_def}'.format (_def = token))
            for _token in MACROS [token]: # retrieve macro definition token list
                S.append (_token)
    return S

def process_macros (T):
    # T is token list
    def exist_macros (T): # exist USE of macros, not definitions
        for token in T:
            if token [0] not in __built_in:
                return True
        return False
    counter = 0
    while (exist_macros (T)): # substitute until no macros
        (T, M) = __find_macros (T)
        T = __substitute_once (T, M)
        counter += 1
        if counter >= 100:
            raise ValueError ('Brainfuck: macro definition exceed maximum recursive depth.')
    return T # T is token list without macros

