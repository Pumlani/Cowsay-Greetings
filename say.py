import cowsay  # Importing the cowsay module for ASCII art of a cow saying text
import sys  # Importing the sys module for accessing command-line arguments

# Checking if exactly one command-line argument is provided
if len(sys.argv) == 2:
    # Generating a message with the provided argument and displaying it using cowsay
    cowsay.cow("hello, " + sys.argv[1])
