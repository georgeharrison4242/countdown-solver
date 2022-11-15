# Countdown Solver
A Python-based desktop application to solve number and word 
problems from the UK gameshow 'Countdown'.

Number problems are described as follows:
* **Input**: 6 integers from the sets {25,50,75,100} and {1,...,10},
and a target 3-digit integer. Between 0 and 4 of the 6 starting numbers must
be chosen (distinctly) from the set of large numbers, and the remaining numbers
must be chosen from the set of small numbers. There can be no more than 2 of 
any small number.
* **The aim**: using only the operators +, -, x, /, and the 6 given numbers,
the contestant must get as close as possible to the target number.
* **Rules**:
  * The result at every intermediate step must be a non-negative integer.
  * Each number can only be used once (a number may be used twice if it is
  selected twice, however).
  * Not all numbers must be used.


Contestants are given 30 seconds to attempt to achieve the target number, and
are awarded 10, 7, and 5 points for being within 0, 5, or 10 points of the
target number respectively.

Countdown Solver takes inspiration from this 'pure' form of the game, but adds
scope in the following ways:

* Any number of inputs are permitted rather than the default 6.
* Input numbers (and the target number) may be any non-negative integer (32-bit).
* Solutions are ordered by their elegance; the solution that uses the fewest
operators is the most elegant! Ties are broken by the number (and in favour-) of
+/- operations. 50+4 is a more elegant solution than 27x2, although this might
make the mathematicians angry...