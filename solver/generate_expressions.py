from expression import Op, Tile

"""
Generate a list of expression trees for a list of number tiles
e.g. generate_expressions([1,2,3]) = [ 1+(2+3), 1+(2-3), ... , (1*2)*3, ... ]
"""


def gen_expressions(tiles, valid_only=True):
    if len(tiles) == 1:
        return [Tile(tiles[0])]

    expressions = []

    # compute non-empty splits of tiles
    # e.g. splits [1,2,3] = [ ([1],[2,3]), ([1,2],[3]) ]
    splits = [(tiles[:i], tiles[i:]) for i in range(1, len(tiles))]
    for left_subtree, right_subtree in splits:

        # recursively compute expressions for each subtree
        left_expressions = gen_expressions(left_subtree)
        right_expressions = gen_expressions(right_subtree)

        for left_expr in left_expressions:
            for right_expr in right_expressions:
                expressions += [Op(op, left_expr, right_expr)
                                for op in ["+", "-", "*", "/"]]

    if valid_only:
        return [e for e in expressions if e.eval() is not None]
    return expressions
