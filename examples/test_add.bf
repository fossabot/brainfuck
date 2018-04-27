# This program tests the macro add.bf

$add

++++ # puts 4 in cell 0
> ++++++ # puts 6 in cell 1
> ++++++++ # puts 8 in cell 2
< add # add cell 2 to cell 1
< add # add cell 1 to cell 0
. # should print 18
