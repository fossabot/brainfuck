# This program moves the current cell data to the right, clearing both.
$clear

> clear < # clear the right cell
[
  > + # move right, increment
  < - # move back, decrement
]
> # move right data pointer
