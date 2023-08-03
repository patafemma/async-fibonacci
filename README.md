# Asynchronous fibonacci

This program reads a positive integer _n_ from stdin and returns the _n_:th
value from Fibonacci sequence.

### Requirements

- Python 3.9 or later

### Description

The function that calculates the Fibonacci number is executed twice concurrently,
using **asyncio** from Python standard library. The program then prints the results
and which of the two call finished first.

Two implementations of the Fibonacci calculation is included. The first one solves
the number iteratively. A random wait of up to one second is included in the function.
To use this implementation, run:

```
$ python fibonacci.py
```

The second implementation is a recursive implementation. It also includes a random
wait up to one second but the wait is included in every recursive call so higher
_n_ results in longer run time. To use this implementation, run:

```
$ python fibonacci.py --recursive
```
