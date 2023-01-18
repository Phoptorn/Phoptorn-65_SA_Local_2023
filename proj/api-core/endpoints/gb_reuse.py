from fastapi import APIRouter

from fastapi.responses import FileResponse


import os


from ..config import status_codes
from ..functions import gb_response

reuse = APIRouter(prefix="/files", tags=["Global API for files"])


@reuse.get("/image/")
async def get_file_image(path):
    # file = "/code/app/files/pf_bot_images/bot1.png"
    if os.path.exists(path):
        return FileResponse(path)
    return gb_response.res(status_codes.code_204, None)
