from pymongo import MongoClient

server = "mongodb://root:example@db-mongo:27017/"
db = "65SA"

conn_pf_users = MongoClient(server)[db]["Platform_Users"]
conn_pf_log_auth = MongoClient(server)[db]["Platform_Log_Auth"]
conn_agt_ac_req = MongoClient(server)[db]["Agent_AC_Requests"]
