from fastapi import FastAPI, Form

from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# CORS (Cross-Origin Resource Sharing)
origins = ["*"]  # ["https://localhost","http://localhost","http://localhost:8080"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Test
@app.get("/")
def read_root():
    return {"65SA": "OK"}

# Test_Form
@app.post("/login_TestForm/")
async def login(username: str = Form(""), password: str = Form("")):
    return {"username": username}


# Routers (Platform)
from .endpoints import pf_auth, pf_users,pf_upload, agt_ac_requests, gb_reuse
app.include_router(pf_auth.pf_auth)
app.include_router(pf_users.pf_users)
app.include_router(pf_upload.pf_upload)
app.include_router(gb_reuse.reuse)
app.include_router(agt_ac_requests.ac_req)


# Routers (Chatbot)
