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

# [x + y, 0], ptr = 0

> +++ +++ +++ + < # [x + y, 10]
$if if # [x + y, 10, 1/0] [2] = 1 iff x + y >= 10

> int_zero_pure # [1] = 48
> # ptr = 2
[ # if [2] = 1
  << --- --- --- - # [0] -= 10
  > + # [1] = 1
  > - # [2] --
]
<< # [0] += 48
++++ ++++ ++++
++++ ++++ ++++
++++ ++++ ++++
