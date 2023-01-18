from fastapi import APIRouter, Form


from ..config import connections, schemas
from ..functions import gb_timestamp


ac_req = APIRouter(prefix="/ac_req", tags=["Agent-Crawler"])


@ac_req.post("/find")
def find():
    data_query = connections.conn_agt_ac_req.find()
    
    def Items(entity) -> list:
        return [Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "_id"                                : str(item["_id"]),
            "chat_User_id"                       : item["chat_User_id"],
            "agt_AC_Request_Timestamp"           : item["agt_AC_Request_Timestamp"],
            "agt_AC_Request_Topic"               : item["agt_AC_Request_Topic"],
            "agt_AC_Request_Target_URL"          : item["agt_AC_Request_Target_URL"],
        }
        
    data = Items(data_query)
    return data

#### create by api
# @ac_req.post("/create")
# def ac_create():
#     mydata = {
#             "_id"                                : "123",
#             "chat_User_id"                       : "123",
#             "agt_AC_Request_Timestamp"           : "123",
#             "agt_AC_Request_Topic"               : "Topic_123",
#             "agt_AC_Request_Target_URL"          : "https://www.mongodb.com/home"
#     }
#     oid = connections.conn_agt_ac_req.insert_one(dict(mydata)).inserted_id
    
#     condition = {"_id": oid}
#     data_query = connections.conn_pf_users.find_one(condition)

#     def Items(entity) -> list:
#         return [Item(item) for item in entity]
#     def Item(item) -> dict:
#         return {
#             "_id"                                : str(item["_id"]),
#             "chat_User_id"                       : item["chat_User_id"],
#             "agt_AC_Request_Timestamp"           : item["agt_AC_Request_Timestamp"],
#             "agt_AC_Request_Topic"               : item["agt_AC_Request_Topic"],
#             "agt_AC_Request_Target_URL"          : item["agt_AC_Request_Target_URL"],
#         }

#     data = Item(data_query)
#     return data


### create by Form-pip-python-multipart.
@ac_req.post("/create")
def ac_req_create(
        chat_User_id                      : str = Form(...),
        agt_AC_Request_Topic              : str = Form(""),
        agt_AC_Request_Timestamp          : str = Form(""),
        agt_AC_Request_Target_URL         : str = Form(...),
):
    
    data_acquired = {
        "chat_User_id"                       : chat_User_id,
        "agt_AC_Request_Timestamp"           : str(gb_timestamp.timestamp()),
        "agt_AC_Request_Topic"               : agt_AC_Request_Topic,
        "agt_AC_Request_Target_URL"          : agt_AC_Request_Target_URL,
    }
    
    id = connections.conn_agt_ac_req.insert_one(dict(data_acquired)).inserted_id
    
    data_query = connections.conn_agt_ac_req.find_one({'_id': id})
    
    def Items(entity) -> list:
        return [Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "_id"                                   : str(item["_id"]),
            "chat_User_id"                          : item["chat_User_id"],
            "agt_AC_Request_Timestamp"            : item["agt_AC_Request_Timestamp"],
            "agt_AC_Request_Topic"                : item["agt_AC_Request_Topic"],
            "agt_AC_Request_Target_URL"           : item["agt_AC_Request_Target_URL"],
        }
        
    data = Item(data_query)
    return data
