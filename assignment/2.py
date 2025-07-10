"""
Het Mehta
500121861
R2142230828
B-21
"""

import re #regular expression-> to validate the data
import sys #system-> to access command-line arguments
import ast #abstract syntax tree-> in future to modify this code easily
import importlib #to check if a module exists
import types #to check if an object is a module
import builtins #to check if a name exists in built-in scope

#to read file path of regular expression
def find_unused_imports(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    imports = re.findall(r'^import\s+(\S+)|^from\s+(\S+)\s+import', content, re.MULTILINE)
    imports = [imp for tup in imports for imp in tup if imp]

    with open(file_path, 'r') as file:
        tree = ast.parse(file.read())

    used_imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            used_imports.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            used_imports.add(node.module)
    
    unused_imports = set(imports) - used_imports
    return unused_imports

#to find out the path of undefined variable in a file
def find_undefined_variables(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    tree = ast.parse(content)

    undefined_variables = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            undefined_variables.add(node.id)
    
    return undefined_variables

#to find out error
def find_syntax_errors(file_path):
    try:
        compile(open(file_path).read(), file_path, 'exec')
    except SyntaxError as e:
        return str(e)

def find_runtime_errors(file_path):
    with open(file_path, 'r') as file:
        try:
            exec(file.read())
        except Exception as e:
            return str(e)

def find_name_errors(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    tree = ast.parse(content)

    name_errors = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            if node.id not in dir(builtins) and node.id not in globals():
                name_errors.add(node.id)
    
    return name_errors

def find_type_errors(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    tree = ast.parse(content)

    type_errors = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if not isinstance(eval(compile(f"{target.id}", "<string>", "eval")), type(node.value)):
                        type_errors.add(target.id)
    
    return type_errors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python error_finder.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]

    unused_imports = find_unused_imports(file_path)
    if unused_imports:
        print("Unused imports found:")
        for imp in unused_imports:
            print(f"    {imp}")

    undefined_variables = find_undefined_variables(file_path)
    if undefined_variables:
        print("Undefined variables found:")
        for var in undefined_variables:
            print(f"    {var}")

    syntax_error = find_syntax_errors(file_path)
    if syntax_error:
        print("Syntax error found:")
        print(syntax_error)

    runtime_error = find_runtime_errors(file_path)
    if runtime_error:
        print("Runtime error found:")
        print(runtime_error)

    name_error = find_name_errors(file_path)
    if name_error:
        print("Name error found:")
        for name in name_error:
            print(f"    {name}")

    type_error = find_type_errors(file_path)
    if type_error:
        print("Type error found:")
        for var in type_error:
            print(f"    {var}")