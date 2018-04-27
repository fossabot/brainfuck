# Brainfuck with Macros

See [Wikipedia](https://en.wikipedia.org/wiki/Brainfuck) on the original Brainfuck.

This implementation of Brainfuck introduces __macro definition__.

### Built-in Commands

- `+` Increment the cell at current data pointer.
- `-` Decrement the cell at current data pointer, __do nothing__ if the cell has value `0`.
- `>` Move data pointer to the right.
- `<` Move data pointer to the left, __do nothing__ if data pointer has value `0`, i.e. at the leftmost cell.
- `[` If the current cell has value `0`, jump to the command after the matching `]`, otherwise continue execution.
- `]` Jump backward to the matching `[`.
- `#` Start an end-of-line comment.
- `$` Import definition of a macro, in the form of `$macro_name`, no space between `$` and the macro name.

### Macros

- A macro can be any snippet of Brainfuck code.
- A macro is defined in a seperate `.bf` file where the file name is the macro name.
- A macro can itself invoke definitions of other macros.
- A macro should not invoke itself. (no self-recursion)
- Two macros cannot invoke each other. (no mutual-recursion)
- The name of a macro can be anything matching the regex `[a-zA-Z_]+`

Here's an example of using macro `zero.bf` in `one.bf`. `one.bf` outputs number `1`.

```brainfuck
# zero.bf
# This program puts Ascii 48 (zero) on the right cell.
# Assuming both current cell and right cell has value 0.
++++ ++++ # Add 8 to current cell
[
  > +++ +++ # Add 6 to right cell
  < - # Decrement current cell by 1
]
```

```brainfuck
# one.bf
$zero # use zero.bf
zero # put zero into the right cell
> + # move right and add 1
. # output
```

## Roadmap

- Make a REPL
- Fix program base path finding with relative path

