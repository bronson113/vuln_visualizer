from flask import Flask, render_template, request
import os, subprocess
app = Flask(__name__)

@app.route("/")
def index():
  return render_template('index.html')

def compile_code_os(code_string):
  with open("/tmp/temp.c", "w") as f:
    f.write(code_string)
  os.system("gcc /tmp/temp.c -o /tmp/temp.out")
  os.system("chmod +x /tmp/temp.out")
  output = subprocess.check_output("/tmp/temp.out", stderr=subprocess.STDOUT).decode()
  return output


@app.route("/compile", methods = ['POST'])
def compile_code():
  input_code = request.form['input_code']
  try:
    result = compile_code_os(input_code)
  except Exception as e:
    print(e)
    result = "An error occured during compilation"
  return render_template('compile.html', result=result)

@app.route("/d3")
def d3_test():
  return render_template('d3_test.html')


if __name__ == "__main__":
  app.run()