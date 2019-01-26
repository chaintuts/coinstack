#!/usr/bin/python

# This file contains script operator functions
# Each function takes a copy of the stack and returns the modified stack
#
# Author: Josh McIntyre
#

# Necessary imports for operators
import hashlib

# Pop two number off the top of the stack and add them
def op_add(stack):

	# First, ensure both numbers to add can be popped from the stack
	try:
		first = stack.pop()
		second = stack.pop()
	except IndexError as e:
		raise SyntaxError("Not enough elements left on stack for OP_ADD")

	# Verfiy numbers are valid integers
	if not (isinstance(first, int) and isinstance(second, int)):
		raise SyntaxError("Invalid numberical value for OP_ADD")

	# Add and push result to the stack
	result = first + second

	stack.append(result)

	return stack

# Pop two number off the top of the stack and subtract them
def op_subtract(stack):

	# First, ensure both numbers to add can be popped from the stack
	try:
		first = stack.pop()
		second = stack.pop()
	except IndexError as e:
		raise SyntaxError("Not enough elements left on stack for OP_ADD")

	# Verfiy numbers are valid integers
	if not (isinstance(first, int) and isinstance(second, int)):
		raise SyntaxError("Invalid numerical value for OP_ADD")

	# Subtract and push result to the stack
	result = second - first

	stack.append(result)

	return stack

# Duplicate the top stack value
def op_duplicate(stack):

	# Append the duplicated top item to the stack
	if not stack:
		raise SyntaxError("Not enough elements left on stack for OP_DUPLICATE")	

	top = stack[-1]
	stack.append(top)

	return stack

# Hash the top item on the stack
# The Bitcoin specs define OP_HASH160 as first
# hashing the data with SHA-256, and then RIPEMD160
def op_hash160(stack):

	# First check the stack is not empty
	if not stack:
		raise SyntaxError("Not enough elements left on stack for OP_DUPLICATE")	
	
	top = stack.pop()

	# First, hash the data using SHA-256
	hash_sha = hashlib.sha256()
	hash_sha.update(top)
	
	sha_digest = hash_sha.digest()

	# Next, hash the data using RIPEMD160
	hash_ripe = hashlib.new("ripemd160")
	hash_ripe.update(sha_digest)
	
	ripe_digest = hash_ripe.digest()

	# Put the digest back on the stack
	stack.append(ripe_digest)

	return stack

# Determine if the two top items on the stack are bitwise equal
# After running the equality check, call and return the result of
# OP_VERIFY
def op_equalverify(stack):

	# First, ensure two values can be popped from the stack
	try:
		first = stack.pop()
		second = stack.pop()
	except IndexError as e:
		raise SyntaxError("Not enough elements left on stack for OP_EQUALVERIFY")

	# Check for equality
	if first == second:
		stack.append(1)
	else:
		stack.append(0)

	# Run OP_VERIFY and return its output
	return op_verify(stack)
	
# Determine if the signature on the stack matches the public key on the stack
# After running the signature check, call and return the result of
# OP_VERIFY
def op_checksigverify(stack):

	# First, ensure two values can be popped from the stack
	try:
		first = stack.pop()
		second = stack.pop()
	except IndexError as e:
		raise SyntaxError("Not enough elements left on stack for OP_EQUALVERIFY")
	
	# In real Bitcoin scripts, the signature message data is formed from
	# transaction data not included in the script
	# For the purposes of testing scripts using this tool, we'll assume the signature
	# is valid and push true on to the stack
	# A future update could allow the user to manually specify the message for real
	# ECDSA signature verification
	stack.append(1)

	# Run OP_VERIFY and return its output
	return op_verify(stack)

# Verify that the top stack value is true
# This is a special operator as it returns False if 
# verification is not correct, or an unmodified stack otherwise 
def op_verify(stack):

	# First verify the stack size
	if len(stack) < 1:
		return False

	# Next verify a numerical value of true left on the stack
	top = stack[-1]
	if top == 1:
		return stack

	# If not, fail out with a value of False
	return False
		
# Register each op function to its op string
OPS = {
	"OP_ADD" : op_add,
	"OP_SUB" : op_subtract,
	"OP_DUP" : op_duplicate,
	"OP_HASH160" : op_hash160,
	"OP_EQUALVERIFY" : op_equalverify,
	"OP_CHECKSIGVERIFY" : op_checksigverify,
	"OP_VERIFY" : op_verify
      }

