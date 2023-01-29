import os
import sys
import subprocess

# Compiles code with gcc, run it and returns the output and the return code
def process(code):
    with open("/tmp/temp.c", "w") as f:
        f.write(code)
    os.system("gcc /tmp/temp.c -o /tmp/temp.out")
    os.system("chmod +x /tmp/temp.out")
    child = subprocess.Popen(["/tmp/temp.out"], stdout=subprocess.PIPE)
    output = child.communicate()[0]
    rc = child.returncode
    return (output, rc)


    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            print(process(f.read()))
    else:
        print("No code file provided")