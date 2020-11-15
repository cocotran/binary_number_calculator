from infix import *
from postfix import *

class Calculator():

	def infix_to_postfix(self, string):
		infix_obj = Infix(string)
		if infix_obj.is_balance():
			return infix_obj.to_postfix()

	def calculatate(self, string):
		postfix_obj = Postfix(self.infix_to_postfix(string))
		return postfix_obj.evaluate()

# Only work with unsigned binary numbers
calculator = Calculator()
print(calculator.calculatate("101 + (100 * 10) - 111"))
