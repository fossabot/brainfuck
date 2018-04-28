# This program tests integer digit addition macro int_add.bf

$int_add $int_zero_pure

int_zero_pure ++++ # [0] = int 4
> int_zero_pure +++ # [1] = int 3
< int_add
> . < .
