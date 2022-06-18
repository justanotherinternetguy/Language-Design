INTEGER, PLUS, MINUS, TIMES, DIVIDE, EOF = 'INTEGER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EOF'

class Token(object):
	def __init__(self, type, value):
		self.type = type # INTGER, PLUS, MINUS, TIMES, DIVIDE, EOF
		self.value = value # token value, non-negative int, +, -, or None

	def __str__(self):
		"""
		String represenation of class instance

		Example:
			Token(INTEGER, 3)
			Token(PLUS '+")
		"""
		return 'Token({type}, {value})'.format(type = self.type, value = repr(self.value))

	def __repr__(self):
		return self.__str__()


class Interpreter(object):
	def __init__(self, text):
		self.text = text
		self.pos = 0
		self.current_token = None
		self.current_char = self.text[self.pos]

	def error(self):
		raise Exception('Error parsing input')

	def advance(self):
		"""
		Advance pos pointer and set current_char
		"""
		self.pos += 1
		if self.pos > len(self.text) - 1:
			self.current_char = None # end of input
		else:
			self.current_char = self.text[self.pos]

	def skip_whitespace(self):
		while self.current_char != None and self.current_char.isspace():
			self.advance()

	def integer(self):
		"""Return a (multidigit) integer consumed from the input."""
		result = ''
		while self.current_char != None and self.current_char.isdigit():
			result += self.current_char
			self.advance()
		return int(result)


	def get_next_token(self):
		"""Lexlical analysis"""
		while self.current_char != None:
			if self.current_char.isspace():
				self.skip_whitespace()
				continue
			if self.current_char.isdigit():
				return Token(INTEGER, self.integer())

			if self.current_char == "+":
				self.advance()
				return Token(PLUS, "+")

			if self.current_char == "-":
				self.advance()
				return Token(MINUS, "-")

			if self.current_char == "*":
				self.advance()
				return Token(TIMES, "*")

			if self.current_char == "/":
				self.advance()
				return Token(DIVIDE, "/")

			self.error()
		return Token(EOF, None)

	def eat(self, token_type):
		if self.current_token.type == token_type:
			self.current_token = self.get_next_token()
		else:
			self.error()

	def term(self):
		"""Return INTEGER token"""
		token = self.current_token
		self.eat(INTEGER)
		return token.value

	def expr(self):
		"""Parser / interpreter"""

		self.current_token = self.get_next_token()

		result = self.term()
		while self.current_token.type in (PLUS, MINUS, TIMES, DIVIDE):
			token = self.current_token
			if token.type == PLUS:
				self.eat(PLUS)
				result += self.term()
			elif token.type == MINUS:
				self.eat(MINUS)
				result -= self.term()
			elif token.type == TIMES:
				self.eat(TIMES)
				result *= self.term()
			elif token.type == DIVIDE:
				self.eat(DIVIDE)
				result /= self.term()
		return result

		########################
		# SPLIT IMPLEMENTATION #
		########################


		# left = self.current_token
		# self.eat(INTEGER)

		# op = self.current_token
		# if op.type == PLUS:
		# 	self.eat(PLUS)
		# if op.type == MINUS:
		# 	self.eat(MINUS)
		# if op.type == TIMES:
		# 	self.eat(TIMES)
		# if op.type == DIVIDE:
		# 	self.eat(DIVIDE)

		# right = self.current_token
		# self.eat(INTEGER)

		# if op.type == PLUS:
		# 	result = left.value + right.value
		# if op.type == MINUS:
		# 	result = left.value - right.value
		# if op.type == TIMES:
		# 	result = left.value * right.value
		# if op.type == DIVIDE:
		# 	result = left.value / right.value

		return result


def main():
	while True:
		try:
			text = input("C>>> ")
		except EOFError:
			break

		if not text:
			continue

		interp = Interpreter(text)
		result = interp.expr()
		print(result)


#entrypoint
if __name__ == '__main__':
	main()
