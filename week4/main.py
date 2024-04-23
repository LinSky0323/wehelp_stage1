from fastapi import FastAPI, Form, Query, Path, status, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from typing import Annotated
from starlette.middleware.sessions import SessionMiddleware

app=FastAPI()
app.mount("/public",StaticFiles(directory="public"),name="public")
templates=Jinja2Templates(directory="templates")
app.add_middleware(SessionMiddleware,secret_key="dsuakfhlkauwjrhikr")
MEMBER_ACOUNT="test"
MEMBER_PASSWORD="test"



@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse(
        request=request,name="index.html",context={})

@app.post("/signin",response_class=RedirectResponse,status_code=303)
async def get(request:Request,acount:Annotated[str,Form()]=None,password:Annotated[str,Form()]=None):
    if not acount:
        return "/error?message=請輸入帳號"
    elif not password:
        return "/error?message=請輸入密碼"
    if acount != MEMBER_ACOUNT:
        return "/error?message=帳號輸入錯誤"
    elif password != MEMBER_PASSWORD:
        return "/error?message=密碼輸入錯誤"
    request.session["SIGNED-IN"]=True
    return "/member"
    
@app.get("/member")
async def log_ok(request:Request):
    if not request.session.get("SIGNED-IN",False):
        return RedirectResponse("/")
    return templates.TemplateResponse(
        request=request,name="member.html",context={}
    )


@app.get("/error")
async def log_err(message:str, request:Request):
    return templates.TemplateResponse(
         request=request,name="error.html", context={"message":message}
    )
@app.get("/signout")
async def sign_out(request:Request):
    request.session["SIGNED-IN"]=False
    return RedirectResponse("/")
@app.get("/square/{snumber}")
async def get_square(snumber:int,request:Request):
    return templates.TemplateResponse(
         request=request,name="square.html", context={"snumber":snumber}
    )