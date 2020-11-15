from collections import deque
import re


class Infix():
    def __init__(self, expression):
        self.expression = expression.replace(" ", "")  # string
        self.operators = ["+", "-", "*", "/"]
        self.brackets = {'(': ')', "[": "]", "{": "}"}
        self.wild = ["(", "[", "{"]
        self.low = ["+", "-"]
        self.high = ["*", "/", "%"]
        self.immediate = [")", "]", "}"]

    def is_balance(self):
        balance_stack = deque()
        for char in self.expression:
            if char in self.brackets.keys():
                balance_stack.append(char)
            if char in self.brackets.values():
                if not balance_stack:
                    # stack is empty
                    return False
                if char == self.brackets[balance_stack[-1]]:
                    # looking at top item of the stack
                    balance_stack.pop()
                else:
                    # no matching bracket
                    return False
        return not balance_stack

    def get_precedence(self, operator):
        if operator in self.high:
            return 2
        if operator in self.low:
            return 1

    def to_postfix(self):
        expression = self.expression
        operator_stack = deque()
        output = []
        while len(expression) > 0:
            token = expression[0]

            if token.isdigit():
                number = re.search('\d+|$', expression).group()
                output.append(number)
                expression = expression[len(number)::]

            if token in self.operators:
                while operator_stack and operator_stack[
                        -1] not in self.wild and (self.get_precedence(
                            operator_stack[-1]) >= self.get_precedence(token)):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
                expression = expression[1::]

            if token in self.wild:
                operator_stack.append(token)
                expression = expression[1::]

            if token in self.immediate:
                while operator_stack[-1] not in self.wild:
                    output.append(operator_stack.pop())
                if operator_stack[-1] in self.wild:
                    operator_stack.pop()
                    expression = expression[1::]

        if not expression:
            while operator_stack:
                output.append(operator_stack.pop())

        return output
