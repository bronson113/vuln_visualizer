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
       # try:
            code = input(">>> ").strip()
            command = code.split(" ")[0]
            if command in ["exit", "quit"]:
                print("Resulting code:")
                print(create_template(includes, code_base))
                print("Exiting...")
                break

            elif command == "run":
                result, return_code = process(create_template(includes, code_base))
                if return_code != 0:
                    print(f"Program exit with error: {return_code}")
                else:
                    print(result)

            elif command == "clear":
                includes = ""
                code_base = ""
            
            elif command == "show":
                print("Current code:")
                print(create_template(includes, code_base))

            elif command == "help":
                print("""
run: run the code
clear: clear the code
show: show the code
exit: exit the program
help: show this message
<code>: add code to the code base
#include <header>: add a header to the code base
""")


            elif command == "#include" or command == "include":
                body = code.split(" ")[1:]
                includes += "#include" + " ".join(body) + "\n"

            elif "=" not in code:
                # no assignment in the current code, user is evaluating a varible / expression
                # add printf to the end of the code, and don't save the current line
                cur_code_base = code_base + f"printf(\"\\n\\n%d\", {code});\n"
                result, return_code = process(create_template(includes, cur_code_base))
                print(result.split(b"\n")[-1].decode())

            else:
                # add semicolon to the end for the user

                # TODO: add implicit type conversion / type inference
                # TODO: multiline input support (or scope tracking)
                # TODO: change code to printf if it's a simple expression
                code_base += "\t" + code + ";\n"
            
      #  except Exception as e:
       #     print(e)
       #     print("An error occured during compilation")

if __name__ == "__main__":
    interactive_prompt()
