# This file contains code that handles the execution of simple, stack-based scripts
# The code starts with a string format script, tokenizes, and executes each op it encounters
#
# Author: Josh McIntyre
#
import op
from op import OPS

# This function tokenizes a string format script
def tokenize(script_string):

	# Split the space delimited script string
	raw_tokens = script_string.split(" ")

	# Properly format tokens
	tokens = []
	for tok in raw_tokens:
		if tok.isnumeric():
			tok = int(tok)
		tokens.append(tok)

	# Python stack operations (pop, append) operate from the "back" (right to left),
	# So we need to reverse the tokens that were added to the list from left to right
	tokens.reverse()

	return tokens

# This function executes on the script tokens using a stack
# When the end of the tokens are reached, the stack is returned
def execute(tokens, verbose=False):

	# Start with an empty stack
	stack = []

	if verbose:
		print("Script tokens are: {}".format(tokens))

	# Iterate over all tokens
	while tokens:

		# Fetch the item at the top of the stack
		next = tokens.pop()
		if verbose:
			print("Stack is: {}\nProcessing token: {}".format(stack, next))

		# If this item is an operator, execute the registered function for the op
		if next in OPS:
			stack = OPS[next](stack)

			# If at any point a VERIFY type OP returns false instead of the stack,
			# exit the script execution with a failure
			if not stack:
				return False

		# Otherwise, push the value on to the stack
		else:
			next = clean_val(next)
			stack.append(next)

		if verbose:
			print("Stack is now: {}\n----------".format(stack))

	return stack
	
# "Clean" non op data by interpreting it to bytes
def clean_val(val):

	if val.startswith("0x"):
		val = bytes.fromhex(val[2:])
	else:
		val = bytes([val])
		
	return val