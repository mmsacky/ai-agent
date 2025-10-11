import os

def get_files_info(working_directory, directory="."):
    try:    
        files_info = []
        target_path = os.path.abspath(os.path.join(working_directory, directory))
        working_dir = os.path.abspath(working_directory)

        if not target_path.startswith(working_dir): 
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'
        
        for item in os.listdir(target_path):    
            file_path = os.path.join(target_path,item)
            files_info.append(f'- {item}: {os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}')
        return "\n".join(files_info)
    
    except Exception as e:
        return f'Error: {e}'