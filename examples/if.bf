# This program tests if current cell is greater/equal than the right, puts 1/0 on the one after, using the four after.
# [2, 3] => [2, 3, 0, 0, 0, 0]; [3, 2] => [3, 2, 1, 0, 0, 0]; [2, 2] => [2, 2, 1, 0, 0, 0]

$copy # copy current to the right, clearing the one after
# [x, y]

> copy < # [x, y, y, 0]
>> copy << # [x, y, y, y, 0]
copy # [x, x, 0, y, 0]
>>> copy <<< # [x, x, 0, y, y, 0]

[
  >>> - # [3] --
  <<< - # [0] --
]

# if x < y [0, x, 0, y - x (+), y, 0]
# if x >= y [0, x, 0, 0, y, 0]

$clear
>>> # ptr = 3
[
  < clear # clear [2]
  + # [2] = 1
  > - # [3] --
] <<<

# [0, x, 0/1, 0, y, 0]

> [
  < + # [0] ++
  > - # [1] --
] < # [x, 0, 0/1, 0, y, 0]

>>>> [
  <<< + # [1] ++
  >>> - # [4] --
] <<<< # [x, y, 0/1, 0, 0, 0]

>> # ptr = 2 - flip 0/1 to 1/0
> + < # [x, y, 0/1, 1, 0, 0]
[
  > clear # if [2] = 1, clear [3]
  <
] # ptr = 2
# [x, y, 0, 1/0, 0, 0]
> [
  < + > -
] # [x, y, 1/0, 0, 0, 0] ptr = 3
<<<

