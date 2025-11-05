# from google import genai
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python
from functions.write_file_content import write_file_content

def call_function(function_call_part, verbose=False):

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")

    valid_functions = {'get_files_info' : get_files_info,
                       'get_file_content': get_file_content,
                       'run_python': run_python,
                       'write_file_content': write_file_content}

    if function_call_part.name in valid_functions:

        function_to_call = valid_functions.get(function_call_part.name)

        function_result = function_to_call(working_directory ='./calculator', **function_call_part.args)
        
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": function_result},
            )
            ],
        ) 
    else:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"},
                )
            ],
        )