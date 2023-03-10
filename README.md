# Vuln Visualizer

Vuln visualizer is a tool to interactively visualize the vulnerabilities in a given c source. 

## Requirements

- *nix enviornment (Tested on Windows WSL 2)
- Python 3.6
- Flask
- GCC

see `requirements.txt` for more information

## Usage

### Web application UI
Start the project using python:

```bash
python app.py
```

Then navigate to the given url in your browser.


### Interactive compiler
To run the interactive compiler, use the following command:

```bash
python vuln_compile/interpreter.py
```

## Components

### Frontend

Using D3.js, the frontend displays the stack and heap in a graph to help visualize the vulnerabilities.

### Backend

Flask is used to serve the frontend and provide an API for the frontend to interact with the backend.

### Compiler

The compiler is a python script that takes a c source file and add helper information for the program to identify the stack and heap layout. It also proxy to the gcc compiler to compile to a binary that's used to attach with ptrace.



## File Structure

- `app.py` - The main flask app
- `vuln_compile/` - The compiler
    - `vuln_compiler.py` - The compiler
    - `intepreter.py` - Interactive compiler test
- `template/` - The frontend
    - `index.html` - The main page
    - `d3_test.html` - A test for d3.js
    - `compile.html` - API for compiling
- `static/` - Static files
    - `js/` - Javascript files
        - `main.js` - The main javascript file
        - `d3.v3.min.js` - D3.js
    - `css/` - CSS files
        - `override.css` - The main css file

## TODO

- [ ] Compiler
    - [x] Proxy to gcc
    - [ ] Cross platform support
    - [ ] Add stack and heap information
    - [ ] Extend C syntax for easy vulnerability production / identification
- [ ] Backend
    - [x] Flask server
    - [ ] API
    - [ ] Disassembler
- [ ] Frontend
    - [ ] Code editor
    - [ ] Display assembly
    - [ ] Display stack and heap