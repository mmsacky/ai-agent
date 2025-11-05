import os 
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_schema import available_functions
from config import system_prompt, MAX_ITERATIONS
from functions.call_function import call_function

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if len(sys.argv) == 1:
        print("Please provide a prompt")
        sys.exit(1)    

    verbose = "--verbose" in sys.argv
    user_prompt = sys.argv[1]
    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    # Do loop up here
    try: 
        for _ in range(MAX_ITERATIONS):
        
            response = client.models.generate_content(
            model='gemini-2.0-flash-001', 
            contents= messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt))

            if response.candidates:
                for candidate in response.candidates:
                    if candidate and candidate.content:
                        messages.append(candidate.content)
            
            if verbose:
                print(f"User prompt: {user_prompt}")
                print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
                print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

            if response.function_calls != None:

                for function_call_part in response.function_calls:  

                    result = call_function(function_call_part, verbose)

                    if len(result.parts) > 0 and hasattr(result.parts[0],'function_response') and hasattr(result.parts[0].function_response,'response'):
            
                        tool_output = (result.parts[0].function_response.response)
                        function_name = function_call_part.name

                        messages.append(types.Content(
                            role="user",
                            parts=[
                            types.Part.from_function_response(
                                name=function_name,
                                response = tool_output,
                                )
                            ],
                            ))
                    else:
                        raise Exception("The program fatally closed.")

                    if verbose:
                        print(f"-> {tool_output}")
            else:
                if response.function_calls is None:
                    if response.text:
                        messages.append(types.Content(role="model", parts=[types.Part(text=response.text)]))
                        print("Final response:")
                        print(response.text)
                        return
                    continue
           
        if response.text:
            print("Final response:")
            print(response.text)
            return
        
    except Exception as e:
        print(f"Fatal Error encountered: {e}")                                     
                    
if __name__ == "__main__":
    main()
    