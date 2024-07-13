import sys


def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()

    # Wait for user input
    while True:
        sys.stdout.flush()
        sys.stdout.write("$ ")
        command = input()
        sys.stdout.write(f"{command}: command not found\n")
        if command == 'exit 0':
            break
        

if __name__ == "__main__":
    main()
