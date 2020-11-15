from collections import deque

class Postfix(object):

	def __init__(self, expression: list):
		# self.expression = ''.join(expression)
		self.expression = expression
		self.operators = {"+": self.add, "-": self.sub, "*": self.mul, "/": self.div}

	def add(self, num1: str, num2: str):
		result = bin(int(num1, 2) + int(num2, 2)).replace("0b", "")
		return result
	
	def sub(self, x: str, y: str):
		y = int(y)
		x = int(x, 2)
		flipped_y = ~y
		flipped_y += 1
		intflipped = int(str(flipped_y), 2)
		result = "{0:b}".format(x + intflipped)
		return (result)

	def mul(self, x: str, y: str):
		multiply = "{0:b}".format(int(x, 2) * int(y, 2))
		return (multiply)

	def div(self, x: str, y: str):
		divide = "{0:b}".format(int(x, 2) // int(y, 2))
		remainder = "{0:b}".format(int(x, 2) % int(y, 2))
		return (divide + ", remainder: " + remainder)

	def evaluate(self):
		stack = deque()
		for token in self.expression:
			if token.isdigit():
				stack.append(token)

			if token in self.operators.keys():
				if len(stack) >= 2:
					result = self.operators[token](stack.pop(), stack.pop())
					stack.append(result)

		if stack:
			return stack[0]

