from fastapi import FastAPI, Form, Query, Path, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware
from sql import get_all_data,get_member_data,update_member_data,update_message,delete_messages


app=FastAPI()
app.mount("/public",StaticFiles(directory="public"),name="public")
templates=Jinja2Templates(directory="templates")
app.add_middleware(SessionMiddleware,secret_key="dsuakfhlkauwjrhikr")



@app.get("/")
async def get_home(request:Request):
    return templates.TemplateResponse(request=request,name="index.html",context={})

@app.get("/error")
async def get_err(request:Request,message:str):
    return templates.TemplateResponse(request=request,name="error.html",context={"message":message})

@app.get("/member")
async def get_member(request:Request):
    if not request.session.get("name",False) :
        return RedirectResponse("/")
    return templates.TemplateResponse(request=request,name="member.html",context={"name":request.session["name"],"username":request.session["username"]})

@app.post("/signup" ,response_class=RedirectResponse,status_code=303)
async def signup(request:Request,signup_name:Annotated[str,Form()]=None,signup_acount:Annotated[str,Form()]=None,signup_password:Annotated[str,Form()]=None):
    data=get_member_data()
    for row in data:
        if signup_acount == row["username"]:
            return "/error?message=重複的帳號"
    update_member_data(signup_name,signup_acount,signup_password)
    return "/"

@app.post("/signin",response_class=RedirectResponse,status_code=303)
async def signin(request:Request,signin_acount:Annotated[str,Form()]=None,signin_password:Annotated[str,Form()]=None):
    data=get_member_data()
    for row in data:
        if signin_acount == row["username"] and signin_password == row["password"]:
            request.session["name"]=row["name"]
            request.session["username"]=row["username"]
            request.session["id"]=row["id"]
            return "/member"
    return "/error?message=錯誤的帳號或密碼"


@app.get("/signout")
async def signout(request:Request):
    request.session["name"]=False
    request.session["username"]=False
    request.session["id"]=False
    return RedirectResponse("/")


@app.post("/create_message",response_class=RedirectResponse,status_code=303)
async def create_message(request:Request,response:Annotated[str,Form()]=None):
    if response != None:
        update_message(request.session["id"],response)
    return "/member"

@app.get("/get_message")
async def get_message(request:Request):
    if request.session.get("username",False):
        return get_all_data()
    return RedirectResponse("/")

@app.post("/delete_message",response_class=RedirectResponse,status_code=303)
async def delete_message(request:Request,message_id:Annotated[int,Form()]=None,message_username:Annotated[str,Form()]=None):
    print(message_username)
    print(request.session["username"])
    if message_username != request.session["username"]:
        return "/member"
    delete_messages(message_id)
    return "/member"

