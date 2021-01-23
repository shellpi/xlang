import scanner

def __x_code(code: str):
    interpreter = scanner.Xlang_interpreter()
    interpreter.scan(code)

def __x_file(path: str):
    content = open(path).read()
    __x_code(content)