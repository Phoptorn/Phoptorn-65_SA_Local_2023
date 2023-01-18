from bson.objectid import ObjectId

from fastapi import APIRouter, HTTPException, FastAPI, Query
from typing import List, Optional


from ..config import connections, conf
from ..functions import gb_file_upload

from fastapi import FastAPI, File, UploadFile
import shutil
import pathlib

pf_upload = APIRouter(
    prefix="/upload",
    tags=["test upload"]
)

@pf_upload.post("/files/")
async def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@pf_upload.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}


####### dev by aom #######
# @upload.post("/image")
# async def image(image: UploadFile = File(...)):
#     with open("{0}/{1}".format(conf.files_bot_path, image.filename), "wb") as buffer:
#         shutil.copyfileobj(image.file, buffer)

#     return {"filename": image.filename}

####### dev by aom-upgrade #######
# https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
# https://www.educative.io/answers/how-to-check-the-prefix-and-suffix-using-python
@pf_upload.post("/image")
async def up_image(image: UploadFile = File(...)):
    
    images = gb_file_upload.file_upload(image, conf.files_user_path, id)
    # return images
    data_query = connections.conn_pf_users.find_one({"pf_user_Picture": image["pf_user_Picture"]})

    def Items(entity) -> dict:
        return[Item(item) for item in entity]

    def Item(item) -> dict:
        return {
            "pf_user_id": str(item["_id"]),
            "pf_user_Picture": item["pf_user_Picture"],
        }
    data = Item(data_query)
    return data
    


