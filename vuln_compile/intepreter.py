from vuln_compiler import process

def create_template(includes, code):
    return f"""
#include <stdio.h>
#include <stdlib.h>
{includes}
int main(){{
    {code}
    return 0;
}}
"""

# interactive prompt
def interactive_prompt():
    includes = ""
    code_base = ""
    while True:
        try:
            code = input(">>> ")
            if code == "exit":
                break

            elif code == "run":
                result = process(create_template(includes, code_base))
                print(result)

            elif code == "clear":
                includes = ""
                code_base = ""
            
            elif code == "show":
                print(create_template(includes, code_base))

            elif code == "help":
                print("""
run: run the code
clear: clear the code
show: show the code
exit: exit the program
help: show this message
<code>: add code to the code base
#include <header>: add a header to the code base
""")


            elif "#include" in code.replace(" ", ""):
                includes += code + "\n"

            else:
                code_base += code + "\n"
            
        except Exception as e:
            print("An error occured during compilation")

if __name__ == "__main__":
    interactive_prompt()
