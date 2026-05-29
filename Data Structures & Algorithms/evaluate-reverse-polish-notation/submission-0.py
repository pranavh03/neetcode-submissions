import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul
        }

        stack = []

        for token in tokens:

            if token in operations:

                b = stack.pop()
                a = stack.pop()

                result = operations[token](a, b)

                stack.append(result)

            elif token == "/":

                b = stack.pop()
                a = stack.pop()

                stack.append(int(a / b))

            else:
                stack.append(int(token))

        return stack[0]