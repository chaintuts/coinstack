## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* Coinstack is a mock interpreter for basic Bitcoin scripts

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build directory

### Features
* Take a basic bitcoin script in string format
* Supports basic operators: OP\_ADD, OP\_SUB, OP\_DUP, OP\_HASH160, OP\_EQUALVERIFY, OP\_CHECKSIGVERIFY*, OP\_VERIFY
* \* NOTE: In real Bitcoin scripts, OP_CHECKSIG needs message data that exists outside the script. 
For this educational interpreter, the op will automatically assume the signature is valid so that interpretation can continue.
A future update may allow the user to manually pass in message data for real ECDSA signature verification.

### Requirements
* Requires Python 3.7

### Platforms
* Linux
* Windows
* MacOSX
* FreeBSD

## Usage
____________

### Command line usage
* Write a Bitcoin script with the supported ops and any data in hex format (preceded by 0x) and save in a file.
* Call the script with `python coinstack.py filename.script`
* Optionally, specify "-v" after the script name for verbose processing. This option is very useful for debugging and the educational nature of this tool.
