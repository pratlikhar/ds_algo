def isMatching(a, b):
    if (a == '(' and b == ')') or (a == '[' and b == ']') or (a == '{' and b == '}'):
        return True
    return False

def check_balanced_paranthesis(a): # T(n) = O(n), S(n) = O(n)
    stack = []

    for x in a:
        if x in ('(','[','{'):
            stack.append(x)

        else:
            if not stack:
                return False
            elif not isMatching(stack[-1], x):
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True
        


print(check_balanced_paranthesis('[{()}]'))
print(check_balanced_paranthesis('(()))'))
print(check_balanced_paranthesis('((())'))
print(check_balanced_paranthesis('()[({})]'))
