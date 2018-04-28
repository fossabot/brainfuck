# This program adds two integer digits.
# Ascii | int
#    48 | 0
#    49 | 1
#    50 | 2
#    51 | 3
#    52 | 4
#    53 | 5
#    54 | 6
#    55 | 7
#    56 | 8
#    57 | 9

$add # add right cell to this, clearing right cell
$int_zero_pure # puts 48 in current cell, affecting no other
$remove_48 # remove 48 from current cell, affecting no other

# [0] = A(x), [1] = A(y)
remove_48 # [0] = x
> remove_48 # [1] = y
< add # [0] = x + y, [1] = 0

