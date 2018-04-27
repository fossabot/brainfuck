# This program puts Ascii 48 (int 0) on current cell, clearing the right cell.

$clear # import macro clear.bf

clear > clear < # clear both cells and move back

> ++++ ++++ # puts 8 on right cell
[
  < +++ +++ # add 6 to left cell
  > - # decrement right cell
]
< # move back
