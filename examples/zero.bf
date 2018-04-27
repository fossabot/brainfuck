# This program puts Ascii 48 (zero) on right cell
# Assuming current cell and right cell are both 0
++++ ++++   # Add 8 to current cell
[           # Start loop at current cell
  > +++ +++ # Move right, Add 6
  < -       # Move left, Decre 1
]
> .         # Move right, Output Ascii 48
