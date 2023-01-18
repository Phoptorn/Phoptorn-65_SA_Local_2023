from ..config import conf

from fastapi import FastAPI, File, UploadFile
import shutil
import pathlib


#### version_3_convert-img-name
def file_upload(image, path, nameid):
    suffix = pathlib.Path(image.filename).suffix
    
    if suffix not in conf.image_suffix:
        return {"message": "try!!"}
    else:
        
        with open("{0}/{1}".format(conf.files_conver_path,
            str(nameid) + "." + image.filename.split(".")[1]
            ), 
            "wb") as buffer:shutil.copyfileobj(image.file, buffer)
        
        data = {"file_ID": str(nameid)}
        
        return (image.filename, data)


#### version_2
def file_upload102(image, path):
    suffix = pathlib.Path(image.filename).suffix
    
    if suffix not in conf.image_suffix:
        return {"message": "try!!"}
    else:
        with open("{0}/{1}".format(path, image.filename), "wb") as buffer:
            shutil.copyfileobj(fsrc=image.file,
                               fdst=image.file)
    # pathlib.Path("/Users/pankaj/abc.txt").suffix
    return {"filename": image.filename} 


# https://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python
# https://www.educative.io/answers/how-to-check-the-prefix-and-suffix-using-python

#### version_1
# @upload.post("/image")
def file_upload101(image: UploadFile = File(...)):
    suffix = pathlib.Path(image.filename).suffix
    
    if suffix not in conf.image_suffix:
        return {"message": "try!!"}
    else:
        with open("{0}/{1}".format(conf.files_bot_path, image.filename), "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)
    # pathlib.Path("/Users/pankaj/abc.txt").suffix
    return {"filename": image.filename}

