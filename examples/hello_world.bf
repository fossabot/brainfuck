# This program prints 'Hello World'
# H  e   l l o   _  W  o   r   l   d
# 72 101 108 111 32 87 111 114 108 100

$int_zero_pure # puts 48 in current cell, no side effect
$clear

# H
int_zero_pure # 48
++++++ ++++++ # +12 = 60
++++++ ++++++ # +12 = 72
. clear

# e
int_zero_pure # 48
+++++ +++++ +++++ +++++ # +20 = 68
+++++ +++++ +++++ +++++ # +20 = 88
+++++ +++++ # +10 = 98
+++ . clear

# ll
int_zero_pure # 48 (-60)
> +++ +++ # [1] = 6
[
  < +++++ +++++ # [0] += 10
  > - # [1] --
] < # [108, 0]
.. clear

# o
> +++++ +++++ + # [1] = 11
[
  < +++++ +++++ # [0] += 10
  > - # [1] --
] < # [110, 0]
+ . clear

# SPACE
> ++++ ++++
[
  < ++++
  > -
] < . clear

# W
> +++++ +++++
[
  < ++++ ++++
  > -
] < # [80, 0]
++++ +++ . clear

# o
> +++++ +++++ + # [1] = 11
[
  < +++++ +++++ # [0] += 10
  > - # [1] --
] < # [110, 0]
+ .

# r
+++ .

# l
--- --- .

# d
---- ---- . clear

