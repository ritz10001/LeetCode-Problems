class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        operators = ["+", "-", "*", "/"]
        for i in range(len(tokens)):
            if tokens[i] in operators:
                n1 = int(stack.pop())
                n2 = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(n2+n1)
                elif tokens[i] == "-":
                    stack.append(n2-n1)
                elif tokens[i] == "*":
                    stack.append(n2*n1)
                else:
                    stack.append(int(float(n2)/n1))
            else:
                stack.append(int(tokens[i]))
        return stack[0]