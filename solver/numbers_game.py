from functools import reduce, partial
from generate_choices import gen_choices
from generate_expressions import gen_expressions

"""
An instance of a numbers game takes a list of up to 11 positive integers (tiles)
and a positive integer target number, and is solved via the solve() method.

The solve() function can return all solutions, the first n solutions, or
the closest n solutions if an exact solution does not exist.
"""

class NumbersGame:

    def __init__(self, tiles, target):

        self.tiles = tiles
        self.target = target

        # validate inputs
        if len(self.tiles) > 11:
            raise Exception("cannot use more than 11 tiles for a numbers game")
        for tile in self.tiles:
            if not isinstance(tile, int) or tile < 0:
                raise Exception(f'tile {tile} is not a positive integer')
        if not isinstance(self.target, int) or self.target < 0:
            raise Exception(f'target {self.target} is not a positive integer')


    def solve(self, all_solutions=True, n_solutions=10, n_closest_solutions=5):

        # generate all expressions from tiles
        all_selections = gen_choices(self.tiles)
        all_exprs_2d = [gen_expressions(s) for s in all_selections]
        all_exprs = reduce(lambda l1, l2: l1 + l2, all_exprs_2d)  # flatten list

        # evaluate expressions and compute distance from solution
        expr_vals = [e.eval() for e in all_exprs]
        expr_val_pairs = list(zip(all_exprs, expr_vals))

        # sort solutions by accuracy and elegance
        expr_val_pairs.sort(key=lambda ev: (abs(ev[1] - self.target),
                                            ev[0].num_operators(),
                                            ev[0].num_muldiv()))

        return expr_val_pairs[n_solutions]


game = NumbersGame([3,6,25,50,75,100],952)
game.solve()