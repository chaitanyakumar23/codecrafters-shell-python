import sys
import os 
import subprocess

def main():
    builtins = ["echo", "exit", "type", "pwd","cd" ]
    PATH = os.environ.get("PATH","")

    # Wait for user input
    while True:
        sys.stdout.flush()
        sys.stdout.write("$ ")
        command = input()
        paths = PATH.split(":")
        cmd = command.strip().split(" ")[0]
        args = command.strip().split(" ")[1:]
        cmd_path = None
        if command.strip() == "exit 0":
            sys.exit(0)
        elif cmd == "echo":
            print(" ".join(args))
        elif cmd == "type":
            for path in paths:
                if os.path.isfile(f"{path}/{args[0]}"):
                    cmd_path = f"{path}/{args[0]}"
            if args[0] in builtins:
                print(f'{args[0]} is a shell builtin')
            elif cmd_path:
                print(f"{args[0]} is {cmd_path}")
            else:
                print(f'{args[0]}: not found')
        elif cmd == "pwd":
             print(f"{os.getcwd()}")
        elif cmd == "cd":
            curr_dir = os.getcwd()
            if args[0].startswith("~"):
                home_dir = os.path.expanduser("~")
                os.chdir(home_dir)
            else:
                try:
                    os.chdir("".join(args))
                    os.chdir(os.path.join(curr_dir, "".join(args)))
                except FileNotFoundError:
                    print("cd: "+"".join(args)+": No such file or directory")
        else:
            for path in paths:
                if os.path.isfile(f"{path}/{cmd}"):
                    cmd_path = f"{path}/{cmd}"
            if cmd_path:
                try:
                    subprocess.run([cmd_path] + args, check=True)
                except subprocess.CalledProcessError as e:
                     print(f"Error executing command: {e}")
            else:
                 print(f"{cmd}: command not found")
        

if __name__ == "__main__":
    main()
