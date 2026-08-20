import sys
import os

if len(sys.argv) < 2:
    print("You must enter a word to search for.", file=sys.stderr)
    print("Usage: python word_search.py <word>", file=sys.stderr)
    sys.exit(1)
word = sys.argv[1]
file = os.getenv('FILE_TO_TEST')


try:
    if not file:
        print("The environment variable 'FILE_TO_TEST' is not set.", file=sys.stderr)
        sys.exit(2)

    with open(file, 'r') as f:
        for line in f:
            if word in line:
                print(line.strip())
                sys.exit(0)
except FileNotFoundError: 
    print(f"The file '{file}' was not found.", file=sys.stderr)
    sys.exit(3)
except PermissionError:
    print(f"Permission denied when trying to read the file '{file}'.", file=sys.stderr)
    sys.exit(4)
except Exception as e:
    print(f"An unexpected error occurred: {e}", file=sys.stderr)
    sys.exit(5)

print(f"The word '{word}' was not found in the file '{file}'.", file=sys.stderr)
sys.exit(6)
        