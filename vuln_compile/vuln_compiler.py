import os
import sys
import subprocess
import tempfile
import stat

# Compiles code with gcc, run it and returns the output and the return code
def process(code):
    # write code into temporary file
    tmp_input = tempfile.NamedTemporaryFile(suffix=".c", prefix="compile_tmp_", delete=False)
    tmp_input.write(code.encode())
    tmp_input.close()

    # compile code
    tmp_output = tempfile.NamedTemporaryFile(prefix="compile_tmp_", delete=False)
    tmp_output.close()
    # TODO: Find a way to compile in different OS (Windows)
    os.system(f"gcc {tmp_input.name} -o {tmp_output.name}")
    os.chmod(tmp_output.name, stat.S_IRWXU)

    # run code
    child = subprocess.Popen([tmp_output.name], stdout=subprocess.PIPE)
    output = child.communicate()[0]
    rc = child.returncode

    # cleanup
    os.unlink(tmp_input.name)
    os.unlink(tmp_output.name)

    return (output, rc)


    
if __name__ == "__main__":
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            print(process(f.read()))
    else:
        print("No code file provided")