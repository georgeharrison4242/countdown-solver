"""
Numbers game solutions are represented by op-trees, with the numbers, or
'tiles', as leaves and operations (+, -, *, /) as branches. The expression
(5+2) * (8/4) is uniquely expressed in tree form with * at the root, for example.
"""

class Tile:
    is_tile = True

    def __init__(self, number):
        self.number = number

    def eval(self) -> int:
        return self.number

    def num_operators(self):
        return 0

    def num_muldiv(self):
        return 0

    def __repr__(self):
        return str(self.number)



class Op:
    # convert op_type string to its natural function
    op_func = {"+": lambda l, r: l + r, "-": lambda l, r: l - r,
               "*": lambda l, r: l * r, "/": lambda l, r: l / r}

    # op_type is either "+", "-", "*", or "/"
    # left and right are either Op or Tile objects
    def __init__(self, op_type, left, right):
        self.op_type = op_type
        self.left = left
        self.right = right

        # validate inputs
        if self.op_type not in ["+","-","*","/"]:
            raise ValueError(f'{self.op_type} is not a valid operation. use +, -, *, or /')

        if (not isinstance(left, Op)) and (not isinstance(left, Tile)):
            raise TypeError('left sub-tree must be a Tile or Op object')
        if (not isinstance(right, Op)) and (not isinstance(right, Tile)):
            raise TypeError('right sub-tree must be a Tile or Op object')

    def eval(self):
        # evaluate left and right subtrees
        left_value = self.left.eval()
        right_value = self.right.eval()

        if left_value is None or right_value is None:
            return None

        # evaluate this op
        result = Op.op_func[self.op_type](left_value, right_value)

        # return None if this operation produced an invalid expression
        # according to countdown rules
        if result <= 0 or not result % 1 == 0:
            return None

        return int(result)

    # used for comparing 'elegance' of expressions: less operators is better
    def num_operators(self):
        return 1 + self.left.num_operators() + self.right.num_operators()

    # used for comparing 'elegance' of expressions: more * and / operations
    # are considered less elegant
    def num_muldiv(self):
        return (1 if self.op_type in ["*","/"] else 0) + \
                self.left.num_muldiv() + self.right.num_muldiv()

    def __repr__(self):
        return "(" + str(self.left) + self.op_type + str(self.right) + ")"
