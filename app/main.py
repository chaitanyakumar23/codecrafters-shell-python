import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    # sys.stdout.flush()

    # Wait for user input
    while (command := input()) != "":
        sys.stdout.flush()
        sys.stdout.write("$ ")
        if command == 'exit 0':
            break
        else:
            sys.stdout.write(f"{command}: command not found\n")
            
if __name__ == "__main__":
    main()
