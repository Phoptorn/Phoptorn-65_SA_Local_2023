from fastapi import APIRouter, Form

from bson.objectid import ObjectId

from ..config import connections,schemas

from ..functions import  gb_timestamp


ac_req = APIRouter(prefix="/ac_req", tags=["Agent-Crawler"])

# find all 
@ac_req.post("/find")
def find():
    data_query = connections.conn_agt_ac_req.find()
    
    def Items(entity) -> list:
        return [Item(item) for item in entity]
    def Item(item) -> dict:
        return {
              "_id"                              : str(item["_id"]),
            "chat_User_id"                       : item["chat_User_id"],
            "agt_AC_Request_Timestamp"           : item["agt_AC_Request_Timestamp"],
            "agt_AC_Request_Topic"               : item["agt_AC_Request_Topic"],
            "agt_AC_Request_Target_URL"          : item["agt_AC_Request_Target_URL"],
            "priority"                           : item["priority"],
        }
        
    data = Items(data_query)
    return data

# เรียกดูข้อมูล 1 รายการ
@ac_req.post("/find_one")
def find_one(reqID:schemas.ac_req_selectID):
    data_query = connections.conn_agt_ac_req.find_one({"_id" : ObjectId(reqID.ac_id) })
    
    def Items(entity) -> dict:
        return[Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "_id"                                : str(item["_id"]),
            "chat_User_id"                       : item["chat_User_id"],
            "agt_AC_Request_Timestamp"           : item["agt_AC_Request_Timestamp"],
            "agt_AC_Request_Topic"               : item["agt_AC_Request_Topic"],
            "agt_AC_Request_Target_URL"          : item["agt_AC_Request_Target_URL"],
            "priority"                           : item["priority"],
        }
    data = Item(data_query)
    return data


# create
@ac_req.post("/create")
def ac_req_create(
    chat_User_id             : str = Form(...),
    agt_AC_Request_Topic     : str = Form(""),
    agt_AC_Request_Target_URL: str = Form(...),
    priority                 : str = Form(...),
):
    data_acquired = {
            "chat_User_id"                       : chat_User_id,
            "agt_AC_Request_Timestamp"           : str(gb_timestamp.timestamp()),
            "agt_AC_Request_Topic"               : agt_AC_Request_Topic,
            "agt_AC_Request_Target_URL"          : agt_AC_Request_Target_URL,
            "priority"                           : priority,
    }

    id = connections.conn_agt_ac_req.insert_one(dict(data_acquired)).inserted_id
    
    data_query = connections.conn_agt_ac_req.find_one({"_id":id})
    
    def Items(entity) -> dict:
        return[Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "_id"                                : str(item["_id"]),
            "chat_User_id"                       : item["chat_User_id"],
            "agt_AC_Request_Timestamp"           : item["agt_AC_Request_Timestamp"],
            "agt_AC_Request_Topic"               : item["agt_AC_Request_Topic"],
            "agt_AC_Request_Target_URL"          : item["agt_AC_Request_Target_URL"],
            "priority"                           : item["priority"],
    }
    data = Item(data_query)
    return data


# การอัพเดท/แก้ไข ข้อมูล Update
@ac_req.post("/update")
def Update( reqID:schemas.ac_req):
    update_data = connections.conn_agt_ac_req.update_many({"_id": ObjectId(reqID.ac_id)},

    {"$set":{
            "chat_User_id"                       : reqID.chat_User_id,
            "agt_AC_Request_Topic"               : reqID.agt_AC_Request_Topic,
            "agt_AC_Request_Target_URL"          : reqID.agt_AC_Request_Target_URL,
            "agt_AC_Request_Timestamp"           : reqID.agt_AC_Request_Timestamp
        }})

    data_query = connections.conn_agt_ac_req.find_one({"_id": ObjectId(reqID.ac_id)})
    def Items(entity) -> dict:
        return[Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "chat_User_id"               : str(item["_id"]),
            "agt_AC_Request_Topic"       : item["agt_AC_Request_Topic"],
            "agt_AC_Request_Target_URL"  : item["agt_AC_Request_Target_URL"],
            "agt_AC_Request_Timestamp"   : item["agt_AC_Request_Timestamp"],
    }
    data = Item(data_query)
    return data

# Delete Request
@ac_req.post("/delete")
def Delete(acReqDelete:schemas.ac_req_selectID):
    condition ={"_id": ObjectId(acReqDelete.ac_id)}
    delete_data = connections.conn_agt_ac_req.delete_one(condition)
    data_query = connections.conn_agt_ac_req.find()

    def Items(entity) -> dict:
        return[Item(item) for item in entity]
    def Item(item) -> dict:
        return {
    "Delete" : "OK"
    }

    data = Item(data_query)
    return data

# from fastapi import APIRouter, Form


# from ..config import connections, schemas

# from ..functions import gb_timestamp


# ac_req = APIRouter(prefix="/ac_req", tags=["Agent-Crawler"])


# @ac_req.post("/find")
# def find():
#     data_query = connections.conn_agt_ac_req.find()

#     def Items(entity) -> list:
#         return [Item(item) for item in entity]

#     def Item(item) -> dict:
#         return {
#             "_id": str(item["_id"]),
#             "chat_User_id": item["chat_User_id"],
#             "agt_AC_Request_Timestamp": item["agt_AC_Request_Timestamp"],
#             "agt_AC_Request_Topic": item["agt_AC_Request_Topic"],
#             "agt_AC_Request_Target_URL": item["agt_AC_Request_Target_URL"],
#         }

#     data = Items(data_query)
#     return data


# @ac_req.post("/create")
# def ac_req_create(
#     chat_User_id: str = Form(...),
#     agt_AC_Request_Topic: str = Form(""),
#     agt_AC_Request_Target_URL: str = Form(...),
# ):
#     data_acquired = {
#         "chat_User_id": chat_User_id,
#         "agt_AC_Request_Timestamp": str(gb_timestamp.timestamp()),
#         "agt_AC_Request_Topic": agt_AC_Request_Topic,
#         "agt_AC_Request_Target_URL": agt_AC_Request_Target_URL,
#     }

#     id = connections.conn_agt_ac_req.insert_one(dict(data_acquired)).inserted_id
#     data_query = connections.conn_agt_ac_req.find_one({"_id": id})

#     def Items(entity) -> dict:
#         return [Item(item) for item in entity]

#     def Item(item) -> dict:
#         return {
#             "_id": str(item["_id"]),
#             "chat_User_id": item["chat_User_id"],
#             "agt_AC_Request_Timestamp": item["agt_AC_Request_Timestamp"],
#             "agt_AC_Request_Topic": item["agt_AC_Request_Topic"],
#             "agt_AC_Request_Target_URL": item["agt_AC_Request_Target_URL"],
#         }

#     data = Item(data_query)
#     return data


# # การอัพเดท/แก้ไข ข้อมูล Update
# @ac_req.post("/update")
# def Update(acUpdate: schemas.ac_req_update):
#     update_data = connections.conn_agt_ac_req.update_many(
#         {"chat_User_id": acUpdate.chat_User_id},
#         {
#             "$set": {
#                 # "_id"                           : acUpdate._id,
#                 "chat_User_id"                  : acUpdate.chat_User_id,
#                 # "agt_AC_Request_Timestamp"      : acUpdate.agt_AC_Request_Timestamp,
#                 "agt_AC_Request_Topic"          : acUpdate.agt_AC_Request_Topic,
#                 "agt_AC_Request_Target_URL"     : acUpdate.agt_AC_Request_Target_URL,
#             }
#         },
#     )

#     data_query = connections.conn_agt_ac_req.find_one(
#         {"chat_User_id": acUpdate.chat_User_id}
#     )

#     def Items(entity) -> dict:
#         return [Item(item) for item in entity]

#     def Item(item) -> dict:
#         return {
#             # "_id"                           : str(item["_id"]),
#             "chat_User_id"                  : item["chat_User_id"],
#             # "agt_AC_Request_Timestamp"      : item["agt_AC_Request_Timestamp"],
#             "agt_AC_Request_Topic"          : item["agt_AC_Request_Topic"],
#             "agt_AC_Request_Target_URL"     : item["agt_AC_Request_Target_URL"],
#         }

#     data = Item(data_query)
#     return data


# # การลบข้อมูล Delete
# @ac_req.post("/delete")
# def Delete(acFind: schemas.ac_findone):
#     condition = {"chat_User_id": acFind.pf_user_Username}
#     delete_data = connections.conn_agt_ac_req.delete_one(condition)
#     data_query = connections.conn_agt_ac_req.find()

#     def Items(entity) -> dict:
#         return [Item(item) for item in entity]

#     def Item(item) -> dict:
#         return {"deleted_จัดการคำร้อง"}

#     data = Items(data_query)
#     return data



