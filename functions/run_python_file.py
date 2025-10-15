import os, subprocess

def run_python_file(working_directory, file_path, args=[]):

    try:
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        abs_working_dir = os.path.abspath(working_directory) + os.sep

        if not target_path.startswith(abs_working_dir):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(target_path):
            return f'Error: File "{file_path}" not found.'
        
        if not target_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        
        
        result = subprocess.run(['python3',target_path, *args], cwd=abs_working_dir, capture_output=True, text=True, timeout=30)
        

        if result.returncode != 0:
            return f'Process exited with code {result.returncode}'
        
        if result.stdout == None:
            return 'No output produced.'

        return f'STDOUT: {result.stdout}STDERR: {result.stderr}'

    except Exception as e:
        return f"Error: executing Python file: {e}"
