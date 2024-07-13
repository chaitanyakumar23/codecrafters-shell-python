import sys
import os 
import subprocess

def main():
    # Uncomment this block to pass the first stage
    # sys.stdout.write("$ ")
    # sys.stdout.flush()

    builtins = ["echo", "exit", "type"]
    PATH = os.environ.get("PATH","")

    # Wait for user input
    while True:
        sys.stdout.flush()
        sys.stdout.write("$ ")
        command = input()
        paths = PATH.split(":")
        cmd = command.strip().split(" ")[0]
        args = command.strip().split(" ")[1]
        cmd_path = None
        if command.strip() == "exit 0":
            sys.exit(0)
        elif cmd == "echo":
            print(args)
        elif cmd == "type":
            for path in paths:
                if os.path.isfile(f"{path}/{args}"):
                    cmd_path = f"{path}/{args}"
            if args in builtins:
                print(f'{args} is a shell builtin')
            elif cmd_path:
                print(f"{args} is {cmd_path}")
            else:
                print(f'{args}: not found')
        else:
            for path in paths:
                if os.path.isfile(f"{path}/{args}"):
                    cmd_path = f"{path}/{args}"
            if cmd_path:
                subprocess.run([cmd_path] + args,check=True)  
            else:
                 print(f"{args}: command not found")
        

if __name__ == "__main__":
    main()
