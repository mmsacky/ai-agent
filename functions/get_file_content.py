import os
from config import MAX_CHARS
def get_file_content(working_directory, file_path):
    try:
        working_dir = os.path.abspath(working_directory) + os.sep
        target_path = os.path.abspath(os.path.join(working_directory, file_path))
        
        if not target_path.startswith(working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(target_path, "r", encoding="utf-8") as file:
            file_content_string = file.read(MAX_CHARS + 1)
        
        if len(file_content_string) > MAX_CHARS:
            truncated_text = file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return truncated_text
        return file_content_string

        
    except Exception as e:
        return f'Error: {e}'

