from fastapi import APIRouter


from ..config import connections, schemas, status_codes, conf
from ..functions import gb_response, token_generate, gb_timestamp, gb_response_files


pf_auth = APIRouter(prefix="/auth", tags=["Platform Authentication"])


# # Test
# @auth.get("/")
# def read_root():
#     return {"Platform Login/Logout": "OK"}


@pf_auth.post("/login", response_model=schemas.res, response_model_exclude_unset=True, response_model_exclude_none=True)
def pf_login(req_login:schemas.req_login):

    condition = {"pf_user_Username": req_login.login_Username} # edit zone

    data_query = connections.conn_pf_users.find_one(condition)

    if (data_query) is not None:
        data_query["pf_user_ID"] = str(data_query["_id"])

        if (req_login.login_Username == data_query["pf_user_Username"] 
        and req_login.login_Password == data_query["pf_user_Password"]):

            def Items(entity) -> list:
                return [Item(item) for item in entity]
            def Item(item) -> dict:
                return {
                    # "pf_user_id"        : str(item["_id"]),
                    # "pf_user_Username"  : item["pf_user_Username"],
                    # "pf_user_Password"  : item["pf_user_Password"],
                    "pf_user_Firstname" : item["pf_user_Firstname"],
                    "pf_user_Lastname"  : item["pf_user_Lastname"],
                    # "pf_user_Email"     : item["pf_user_Email"],
                    # "pf_user_Picture"   : item["pf_user_Picture"],
                }

            data = Item(data_query)

            # Create Token
            token = token_generate.token_gen(req_login.login_UUID)
            data["user_Token"] = token

            # Get User Profile Image
            image_file = gb_response_files.response_files(conf.files_user_path, data_query["pf_user_Picture"])
            # data["user_Pic"] = gb_response_files.response_files(pf_conf.files_user_path, data_query["pf_user_Picture"])
            data["pf_user_Image_Path"] = conf.api_get_file + image_file.path

            # create log 
            log = { "pf_auth_User_ID":      data_query["pf_user_ID"], 
                    "pf_auth_Token":        token, 
                    "pf_auth_Type":         "login",
                    "pf_auth_Timestamp":    str(gb_timestamp.timestamp())
            }

            # Add log to database
            connections.conn_pf_log_auth.insert_one(dict(log)).inserted_id

            # Create Response (status & content)    
            res = gb_response.res(status_codes.code_200, data)

            return res
        return gb_response.res(status_codes.code_204, None)
    return gb_response.res(status_codes.code_204, None)
