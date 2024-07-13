import sys
import os 

def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()

    builtins = ["echo", "exit", "type"]
    PATH = os.environ.get("PATH")

    # Wait for user input
    while True:
        sys.stdout.flush()
        sys.stdout.write("$ ")
        command = input()
        args = command.strip()
        cmd = args.split(" ")[1]
        cmd_path = None
        paths = PATH.split(":")
        for path in paths:
            if os.path.isfile(f"{path}/{cmd}"):
                cmd_path = f"{path}/{cmd}"
                os.system(args.split(" ")[0](cmd))        
        if args == "exit 0":
            sys.exit(0)
        elif args.startswith("echo "):
            print(args[len("echo ") :])
        elif args.startswith("type"):
            if cmd in builtins:
                print(f'{args[len("type ") :]} is a shell builtin')
            elif cmd_path:
                print(f"{cmd} is {cmd_path}")
            else:
                print(f'{args[len("type ") :]}: not found')
        else:
            print(f"{args}: command not found")
        

if __name__ == "__main__":
    main()
