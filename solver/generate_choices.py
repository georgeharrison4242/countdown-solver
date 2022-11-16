from itertools import combinations, permutations

"""
Generate a list of all permutations of non-empty subsequences of a list
e.g. generate_choices([1,2,3]) = [[1],[2],[3],[1,2],[2,1],[1,3], ... , [3,2,1]]
This corresponds to all selections that a numbers solution (tree) could be made from
"""

def gen_choices(tiles):

    # generate all non-empty subsets of tiles
    subsets = []
    for i in range(1, len(tiles) + 1):
        subsets += list(combinations(tiles, i))

    # and all permutations of each subset
    perms = []
    for s in subsets:
        perms += list(permutations(s))

    # convert tuples to lists
    choices = list(map(lambda p: list(p), perms))

    return choices
