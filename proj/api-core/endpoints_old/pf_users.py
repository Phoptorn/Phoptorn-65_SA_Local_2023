from fastapi import APIRouter

from bson.objectid import ObjectId


from ..config import connections


pf_users = APIRouter(prefix="/user")


# # Test
# @pf_users.get("/")
# def read_root():
#     return {"pf_users read_root": "OK"}


@pf_users.post("/find")
def find():
    data_query = connections.conn_pf_users.find()

    def Items(entity) -> list:
        return [Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "pf_user_id"        : str(item["_id"]),
            "pf_user_Username"  : item["pf_user_Username"],
            "pf_user_Password"  : item["pf_user_Password"],
            "pf_user_Firstname" : item["pf_user_Firstname"],
            "pf_user_Lastname"  : item["pf_user_Lastname"],
            "pf_user_Email"     : item["pf_user_Email"],
            "pf_user_Picture"   : item["pf_user_Picture"],
        }

    data = Items(data_query)
    return data


@pf_users.post("/find_one")
def find_one(id: str):
    condition = {"_id": ObjectId(id)}
    data_query = connections.conn_pf_users.find_one(condition)

    def Items(entity) -> list:
        return [Item(item) for item in entity]
    def Item(item) -> dict:
        return {
            "pf_user_id"        : str(item["_id"]),
            "pf_user_Username"  : item["pf_user_Username"],
            "pf_user_Password"  : item["pf_user_Password"],
            "pf_user_Firstname" : item["pf_user_Firstname"],
            "pf_user_Lastname"  : item["pf_user_Lastname"],
            "pf_user_Email"     : item["pf_user_Email"],
            "pf_user_Picture"   : item["pf_user_Picture"],
        }

    data = Item(data_query)
    return data


# @pf_users.get("/insert_one")
# def create():
#     mydict = {
#         "pf_user_Username": "user10",
#         "pf_user_Firstname": "Name10",
#         "pf_user_Lastname": "Sur10",
#         "pf_user_Email": "name10@email.com",
#         "pf_user_Picture": "user10.png",
#         "pf_user_Password": "pass10",
#     }
#     oid = connections.conn_pf_users.insert_one(dict(mydict)).inserted_id
    
#     condition = {"_id": oid}
#     data_query = connections.conn_pf_users.find_one(condition)

#     def Items(entity) -> list:
#         return [Item(item) for item in entity]
#     def Item(item) -> dict:
#         return {
#             "pf_user_id"        : str(item["_id"]),
#             "pf_user_Username"  : item["pf_user_Username"],
#             "pf_user_Password"  : item["pf_user_Password"],
#             "pf_user_Firstname" : item["pf_user_Firstname"],
#             "pf_user_Lastname"  : item["pf_user_Lastname"],
#             "pf_user_Email"     : item["pf_user_Email"],
#             "pf_user_Picture"   : item["pf_user_Picture"],
#         }

#     data = Item(data_query)
#     return data


# @pf_users.get("/update_one")
# def update(id: str):
#     condition = {"_id": ObjectId(id)}
#     mydict = {
#         "pf_user_Username": "newuser10",
#         "pf_user_Firstname": "newName10",
#         "pf_user_Lastname": "newSur10",
#         "pf_user_Email": "newname10@email.com",
#         "pf_user_Picture": "newuser10.png",
#         "pf_user_Password": "newpass10",
#     }

#     connections.conn_pf_users.update_one(condition, {"$set": dict(mydict)})

#     data_query = connections.conn_pf_users.find_one({"_id": ObjectId(id)})

#     def Items(entity) -> list:
#         return [Item(item) for item in entity]
#     def Item(item) -> dict:
#         return {
#             "pf_user_id"        : str(item["_id"]),
#             "pf_user_Username"  : item["pf_user_Username"],
#             "pf_user_Password"  : item["pf_user_Password"],
#             "pf_user_Firstname" : item["pf_user_Firstname"],
#             "pf_user_Lastname"  : item["pf_user_Lastname"],
#             "pf_user_Email"     : item["pf_user_Email"],
#             "pf_user_Picture"   : item["pf_user_Picture"],
#         }

#     data = Item(data_query)
#     return data


# @pf_users.get("/delete_one")
# def delete(id: str):
#     condition = {"_id": ObjectId(id)}
#     connections.conn_pf_users.delete_one(condition)

#     data_query = connections.conn_pf_users.find()

#     def Items(entity) -> list:
#         return [Item(item) for item in entity]
#     def Item(item) -> dict:
#         return {
#             "pf_user_id"        : str(item["_id"]),
#             "pf_user_Username"  : item["pf_user_Username"],
#             "pf_user_Password"  : item["pf_user_Password"],
#             "pf_user_Firstname" : item["pf_user_Firstname"],
#             "pf_user_Lastname"  : item["pf_user_Lastname"],
#             "pf_user_Email"     : item["pf_user_Email"],
#             "pf_user_Picture"   : item["pf_user_Picture"],
#         }

#     data = Items(data_query)
#     return data
