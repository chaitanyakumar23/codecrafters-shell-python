import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    # sys.stdout.flush()

    # Wait for user input
    while (command := input()) != "":
        sys.stdout.flush()
        sys.stdout.write(f"{command}: command not found\n")
        sys.stdout.write("$ ")
    
if __name__ == "__main__":
    main()
