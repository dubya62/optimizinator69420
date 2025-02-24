
import main
import rbe_interface
import decompiler

import standard



class RBE:
    pass


class Function:
    def __init__(self, name:str, input_variables:list[str], tokens:list[str]):
        self.name = name
        self.input_variables = input_variables
        self.tokens = tokens


def split_rbe_output(tokens:str):
    result = []
    i = 0
    n = len(tokens)
    current = ""
    quotes = 0
    backslashes = 0
    while i < n:
        match(tokens[i]):
            case '"':
                if backslashes % 2 == 0:
                    quotes ^= 1
            case "\\":
                backslashes += 1
                if backslashes % 2 == 0:
                    backslashes = 0
            case " ":
                if not quotes:
                    result.append(current)
                    current = ""
                    i += 1
                    continue

        current += tokens[i]

        if tokens[i] != "\\":
            backslashes = 0

        i += 1

    if len(current) > 0: 
        result.append(current)
    return result

if __name__ == '__main__':
    # run the C -> ir compiler
    program = main.Main()
    #tokens, token_types = program.start(["main.py", "/home/dubya/Desktop/rule_based_engine/main.c"])
    tokens, token_types = program.start(["main.py", "testing.c"])

    # run the optimizer
    database_files = ["test.rbe"]

    # setup the optimizer to minimize metric 0
    process = rbe_interface.start_process(database_files, "0", "-1")

    for func in tokens:
        if issubclass(type(func), standard.Function):
            the_strings = [x.token for x in func.tokens]
            print("RBE INPUT:")
            print(the_strings)
            result = rbe_interface.optimize_tokens(process, the_strings)
            print("RBE OUTPUT:")
            print(result)
            func.tokens = split_rbe_output(result)

    # run the ir -> C decompiler

    result = ""


    the_types = {}
    for x in range(len(token_types)):
        if issubclass(type(token_types[x]), standard.Type):
            the_types[f"#{x}"] = token_types[x].type
            if issubclass(type(token_types[x]), standard.Type):
                the_types[f"#{x}"] = token_types[x].type.type
        else:
            the_types[f"#{x}"] = token_types[x]


    for func in tokens:
        if issubclass(type(func), standard.Function):
            print(func.args)
            func.arg_types = [the_types[var.token] for var in func.args]
            i = 0
            print(func.name, func.return_type, func.args, func.arg_types, func.arg_constraints, func.tokens, func.declaration)
            print(the_types)

            the_function = Function(func.name, [x.token for x in func.args], func.tokens)
            the_included_libraries = []
            the_external_variables = {}

            compiled_code = decompiler.IRToCDecompiler(the_function, the_types, the_included_libraries, the_external_variables).generate_c_code()
            result += compiled_code

    print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(result)



