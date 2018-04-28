# This program copies current cell to the right, overwriting the right, clearing the one after.
# [x, y] => [x, x, 0]

$clear

> clear > clear << # [x, 0, 0]

[
  > + # [1] ++
  > + # [2] ++
  << - # [0] --
] # [0, x, x]

>> # ptr = 2

[
  << + # [0] ++
  >> - # [2] --
] # [x, x, 0], ptr = 2

<<
