# This code provides a command-line interface for using the Coinstack interpreter
#
# Author: Josh McIntyre
#
import sys
from interpreter import tokenize, execute

# Parse the command line filename argument
def parse_args():

	args = []
	
	# Read the script string from the specified file
	try:
		filename = sys.argv[1]
		args.append(filename)
	except IndexError as e:
		print("No script file specified.")
		exit(1)
		
	# Check for verbose option
	try:
		verbose = sys.argv[2]
		args.append(True)
	except IndexError as e:
		args.append(False)
		
	return args

# Read the script string from a specified file
def read_file(filename):

	with open(filename) as f:
		script_string = f.readline().strip()
		
	return script_string

# This is the main entry point for the program
def main():

	# Get the script string
	args = parse_args()
	script_string = read_file(args[0])

	# Tokenize the script string and then execute
	tokens = tokenize(script_string)
	final = execute(tokens, verbose=args[1])

	# Display the final result to the user
	if final:
		print("The transaction is valid!")
	else:
		print("The transaction didn't properly validate.")

if __name__ == "__main__":

	main()
