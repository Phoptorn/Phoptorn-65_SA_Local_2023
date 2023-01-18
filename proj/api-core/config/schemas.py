from pydantic import BaseModel

from bson.objectid import ObjectId

from typing import Union


class res(BaseModel):
    status          : dict
    data            : Union[dict,list,str, None]= None


class req_login(BaseModel):
    login_UUID      : str
    login_Username  : str
    login_Password  : str


class ac_req(BaseModel):
    ac_id                       : str
    chat_User_id                : str
    agt_AC_Request_Target_URL   : str
    agt_AC_Request_Topic        : Union[str ,None] = None
    agt_AC_Request_Timestamp    : str

class ac_req_selectID(BaseModel):
    ac_id               : str


class user_update(BaseModel):
    user_id             : str
    pf_user_Username    : str
    pf_user_Password    : str
    pf_user_Firstname   : str
    pf_user_Lastname    : str
    pf_user_Email       : str
    pf_user_Picture     : str
    active_status       : bool

class user_selectID(BaseModel):
    user_id    : str



