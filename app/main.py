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
        args = command.strip()
        if args:
            if args == "exit 0":
                sys.exit(0)
            elif args.startswith("echo "):
                print(args[len("echo ") :])
            else:
                print(f"{args}: command not found")
        

if __name__ == "__main__":
    main()
