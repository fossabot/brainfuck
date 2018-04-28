# This program tests looping control in Brainfuck implementation.

+++
>> ++ > +
<<< # [3, 0, 2, 1]

[ # start loop at [0]
  >> [ # start inner loop at [2]
    > + # [3] ++
    < - # [2] --
    ]
  ++ # restore [2] = 2
] # [0, 0, 0, 7]

$int_zero $add
>> int_zero # [0, 0, 48, 7]
add # [0, 0, 0, int 7]
> . # print 7
