
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



    # run the optimizer
    rbe = pyrbe.RBE("test.rbe")

    for func in tokens:
        if issubclass(type(func), standard.Function):
            func.tokens = rbe.minimize_metric(0, [x.token for x in func.tokens])

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
        func.arg_types = [the_types[var.token] for var in func.args]
        i = 0
        print(func.name, func.return_type, func.args, func.arg_types, func.arg_constraints, func.tokens, func.declaration)
        print(the_types)
        if issubclass(type(func), standard.Function):
            the_function = Function(func.name, [x.token for x in func.args], func.tokens)
            the_included_libraries = []
            the_external_variables = {}

            compiled_code = decompiler.IRToCDecompiler(the_function, the_types, the_included_libraries, the_external_variables).generate_c_code()
            result += compiled_code

    print("\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(result)



