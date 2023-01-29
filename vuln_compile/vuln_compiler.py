import os
import sys


def process(code):
    with open("/tmp/temp.c", "w") as f:
        f.write(code)
    os.system("gcc /tmp/temp.c -o /tmp/temp.out")
    os.system("chmod +x /tmp/temp.out")
    output = os.popen("/tmp/temp.out").read()
    return output


    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            print(process(f.read()))
    else:
        print("No code file provided")