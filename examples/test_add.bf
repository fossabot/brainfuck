# This program tests the macro add.bf

$add $int_zero

++ # puts 2 in cell 0
> +++ # puts 3 in cell 1
> ++++ # puts 4 in cell 2
< add # add cell 2 to cell 1
< add # add cell 1 to cell 0
# current cells 9, 0, 0
> int_zero # puts int 0 (Ascii 48) in cell 1
< add # add cell 1 to cell 0
. # should print int 9
