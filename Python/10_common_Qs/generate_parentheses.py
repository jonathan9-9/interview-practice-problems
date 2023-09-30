# given an integer n, generate all the valid combinations of n pairs of parentheses(returns boolean)
def is_valid(combination):
    stack = []
    for par in combination:
        if par == '(':
            stack.append(par)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0


# result = is_valid("(()())")
# print(result)
result = is_valid("())(")
print(result)

# OR (returns possible combinations)


def generate(n):
    def rec(n, diff, comb, combs):
        if n < 0 or diff > n:
            return
        elif n == 0:
            if diff == 0:
                combs.append(''.join(comb))
        else:
            comb.append('(')
            rec(n - 1, diff + 1, comb, combs)
            comb.pop()
            comb.append(')')
            rec(n - 1, diff - 1, comb, combs)
            comb.pop()
    combs = []
    rec(2*n, 0, [], combs)
    return combs


result = generate(1)
print("recursive solution: ", result)
