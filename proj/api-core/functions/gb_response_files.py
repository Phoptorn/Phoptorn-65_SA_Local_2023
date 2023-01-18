import os
from fastapi.responses import FileResponse

def response_files(file_path,file_name):

    file = os.path.join(file_path, file_name)
    return FileResponse(file)
