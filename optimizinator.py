
import main
import pyrbe
import decompiler

import standard


class Function:
    def __init__(self, name:str, input_variables:list[str], tokens:list[str]):
        self.name = name
        self.input_variables = input_variables
        self.tokens = tokens


if __name__ == '__main__':
    # run the C -> ir compiler
    program = main.Main()
    tokens, token_types = program.start(["main.py", "testcase.c"])

    the_types = {}
    for x in range(len(token_types)):
        the_types[f"#{x}"] = token_types[x]


    # run the optimizer
    rbe = pyrbe.RBE("test.rbe")

    for func in tokens:
        if issubclass(type(func), standard.Function):
            func.tokens = rbe.minimize_metric(0, [x.token for x in func.tokens])

    # run the ir -> C decompiler

    result = ""

    for func in tokens:
        print(func.name, func.return_type, func.args, func.arg_types, func.arg_constraints, func.tokens, func.declaration)
        print(the_types)
        if issubclass(type(func), standard.Function):
            the_function = Function(func.name, [x.token for x in func.args], func.tokens)
            the_included_libraries = []
            the_external_variables = {}

            compiled_code = decompiler.IRToCDecompiler(the_function, the_types, the_included_libraries, the_external_variables).generate_c_code()
            result += compiled_code

    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(result)



