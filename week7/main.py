from fastapi import FastAPI, Form, Query, Path, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware
from sql import get_all_data,get_member_data,update_member_data,update_message,delete_messages,check_acount,check_acount_password,check_member,updata_name


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
    data=get_all_data()
    if not request.session.get("name",False) :
        return RedirectResponse("/")
    return templates.TemplateResponse(request=request,name="member.html",context={"name":request.session["name"],"username":request.session["username"],"data":data})
    # 多回傳一個data 用樣板引擎的迴圈控制直接渲染
@app.post("/signup" ,response_class=RedirectResponse,status_code=303)
async def signup(request:Request,signup_name:Annotated[str,Form()]=None,signup_acount:Annotated[str,Form()]=None,signup_password:Annotated[str,Form()]=None):
    data=check_acount(signup_acount)
    if data:
        return "/error?message=重複的帳號"
    update_member_data(signup_name,signup_acount,signup_password)
    return "/"

    # 從取出資料比對 改成 直接用SQL語句確認是否有符合的資料

    # data=get_member_data()
    # for row in data:
    #     if signup_acount == row["username"]:
    #         return "/error?message=重複的帳號"
    # update_member_data(signup_name,signup_acount,signup_password)
    # return "/"

@app.post("/signin",response_class=RedirectResponse,status_code=303)
async def signin(request:Request,signin_acount:Annotated[str,Form()]=None,signin_password:Annotated[str,Form()]=None):
    data=check_acount_password(signin_acount,signin_password)
    if data:
        request.session["name"]=data["name"]
        request.session["username"]=data["username"]
        request.session["id"]=data["id"]
        return "/member"
    return "/error?message=錯誤的帳號或密碼"

     # 從取出資料比對 改成 直接用SQL語句確認是否有符合的資料

    # data=get_member_data()
    # for row in data:
    #     if signin_acount == row["username"] and signin_password == row["password"]:
    #         request.session["name"]=row["name"]
    #         request.session["username"]=row["username"]
    #         request.session["id"]=row["id"]
    #         return "/member"
    # return "/error?message=錯誤的帳號或密碼"


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

# 從「利用JS對後端請求取得資料」 改成 使用後段直接傳data給樣板引擎html做渲染

# @app.get("/get_message")
# async def get_message(request:Request):
#     if request.session.get("username",False):
#         return get_all_data()
#     return RedirectResponse("/")

@app.post("/delete_message",response_class=RedirectResponse,status_code=303)
async def delete_message(request:Request,message_id:Annotated[int,Form()]=None,message_username:Annotated[str,Form()]=None):
    if message_username != request.session["username"]:
        return "/member"
    delete_messages(message_id)
    return "/member"

# week7確認是否登入後，把參數username丟進函式拿答案
@app.get("/api/member")
async def check_members(request:Request,username:str):
   if not request.session.get("name",False) :
       return  JSONResponse({"data":None})
   return JSONResponse(check_member(username))

# week7確認是否登入後，把當前session的username跟request body中的資料傳進函式 同時修改session name
@app.patch("/api/member")
async def update_names(request:Request):
    signin=request.session.get("username",False)
    data=await request.json()
    if signin:
        name=data.get("name")
        result=updata_name(name,signin)
        request.session["name"]=data["name"]
        return JSONResponse(result)
    return {"error":True}
    
