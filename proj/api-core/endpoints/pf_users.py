from fastapi import APIRouter, Form, UploadFile, File

import os
import shutil 
from fastapi.responses import FileResponse
from bson.objectid import ObjectId
from ..config import connections, schemas, conf
from ..functions import gb_file_upload, gb_response_files

pf_users = APIRouter(prefix='/users', tags=["User-Manage"])



# เรียกดูข้อมูลมั้งหมด
@pf_users.post("/find_all")
def find():
    data_query = connections.conn_pf_users.find() #ดึงข้อมูลใน Colleation ทั้งหมด
    
    def Items(entity) -> dict:
        return[Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "pf_user_id"        : str(item["_id"]),
            "pf_user_Username"  : item["pf_user_Username"],
            "pf_user_Password"  : item["pf_user_Password"],
            "pf_user_Firstname" : item["pf_user_Firstname"],
            "pf_user_Lastname"  : item["pf_user_Lastname"],
            "pf_user_Email"     : item["pf_user_Email"],
            "pf_user_Picture"   : item["pf_user_Picture"],
            "active_status"     : item["active_status"],
    }

    data = Items(data_query)
    return data


# เรียกดูข้อมูล 1 รายการ
@pf_users.post("/find_one", )
def find_one( userFind:schemas.user_selectID):
    data_query = connections.conn_pf_users.find_one({"_id" : ObjectId(userFind.user_id)})
    
    def Items(entity) -> dict:
        return[Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "pf_user_id"        : str(item["_id"]),
            "pf_user_Username"  : item["pf_user_Username"],
            "pf_user_Password"  : item["pf_user_Password"],
            "pf_user_Firstname" : item["pf_user_Firstname"],
            "pf_user_Lastname"  : item["pf_user_Lastname"],
            "pf_user_Email"     : item["pf_user_Email"],
            "pf_user_Picture"   : item["pf_user_Picture"],
            "active_status": item["active_status"],
    }
    data = Item(data_query)
    return data


# การสร้างข้อมูลใหม่ Create
@pf_users.post("/create")
def Create_User(
        pf_user_Username: str = Form(...),
        pf_user_Password: str = Form(...),
        pf_user_Firstname: str = Form(...),
        pf_user_Lastname: str = Form(...),
        pf_user_Email: str = Form(...),
        pf_user_Picture: UploadFile = File(...),
        active_status: bool = Form(...),
        ):

    UserInfo = {
        "pf_user_Username": pf_user_Username,
        "pf_user_Firstname": pf_user_Firstname,
        "pf_user_Lastname": pf_user_Lastname,
        "pf_user_Email": pf_user_Email,
        "pf_user_Picture": pf_user_Picture.filename,
        "pf_user_Password": pf_user_Password,
        "active_status" : active_status
    }

    

    id = connections.conn_pf_users.insert_one(dict(UserInfo)).inserted_id
        
    gb_file_upload.file_upload(pf_user_Picture, conf.files_user_path,id)
    data_query = connections.conn_pf_users.find_one({"_id": id})

    def Items(entity) -> dict:
        return[Item(item) for item in entity]

    def Item(item) -> dict:
        return {
            "pf_user_id": str(item["_id"]),
            "pf_user_Username": item["pf_user_Username"],
            "pf_user_Password": item["pf_user_Password"],
            "pf_user_Firstname": item["pf_user_Firstname"],
            "pf_user_Lastname": item["pf_user_Lastname"],
            "pf_user_Email": item["pf_user_Email"],
            "pf_user_Picture": item["pf_user_Picture"],
            "active_status": item["active_status"]
        }
    data = Item(data_query)
    return data

# การอัพเดท/แก้ไข ข้อมูล Update
@pf_users.post("/update")
def Update( userUpdate:schemas.user_update):
    update_data = connections.conn_pf_users.update_many({"_id":ObjectId(userUpdate.user_id)},

    {"$set":{
        "pf_user_Username"  :userUpdate.pf_user_Username,
        "pf_user_Password"  :userUpdate.pf_user_Password,
        "pf_user_Lastname"  :userUpdate.pf_user_Lastname,
        "pf_user_Firstname" :userUpdate.pf_user_Firstname,
        "pf_user_Email"     :userUpdate.pf_user_Email,
        "pf_user_Picture"   :userUpdate.pf_user_Picture,
        "active_status"     :userUpdate.active_status,
        }})

    data_query = connections.conn_pf_users.find_one({"_id":ObjectId(userUpdate.user_id)})
    def Items(entity) -> dict:
        return[Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "pf_user_id"        : str(item["_id"]),
            "pf_user_Username"  : item["pf_user_Username"],
            "pf_user_Password"  : item["pf_user_Password"],
            "pf_user_Firstname" : item["pf_user_Firstname"],
            "pf_user_Lastname"  : item["pf_user_Lastname"],
            "pf_user_Email"     : item["pf_user_Email"],
            "pf_user_Picture"   : item["pf_user_Picture"],
            "active_status"     : item["active_status"],
    }
    data = Item(data_query)
    return data


# การลบข้อมูล Delete
# @pf_users.post("/delete")
# def Delete(userDelete:schemas.user_selectID):
#     condition = {"_id": ObjectId(userDelete.user_id)}
#     delete_data = connections.conn_pf_users.delete_one(condition)
#     data_query = connections.conn_pf_users.find()

#     def Items(entity) -> dict:
#         return[Item(item) for item in entity]
#     def Item(item) -> dict:
#         return {
#             "deleted_จัดการผู้ใช้"
#     }

#     data = Items(data_query)
#     return data

##############

@pf_users.post("/delete")
def Delete(userDelete:schemas.user_selectID):
    # condition = {"_id": ObjectId(userDelete.user_id)}
    # delete_data = connections.conn_pf_users.delete_one(condition)
    
    try:
        condition = {"_id": ObjectId(userDelete.user_id)}
        delete_data = connections.conn_pf_users.delete_one(condition)
        
        location = conf.files_conver_path
        file = '63bfdbbe80e303a0786dc599.jpg'
        path = os.path.join(location, file)
        os.remove(path)
    except FileNotFoundError:
        print("File not")
    
    return ("%s has been deleted_user and img_profile" %file)




