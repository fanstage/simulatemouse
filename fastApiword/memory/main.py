from typing import List
import os
from fastapi import Depends, FastAPI, HTTPException, Request, File, UploadFile
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from dateutil.parser import isoparse
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from .sendmail import sendmail
models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins="http://192.168.1.114:8081/",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_userphone(db, userphone=user.userphone)
#     if db_user:
#         raise HTTPException(status_code=400, detail="userphone already registered")
#     return crud.create_user(db=db, user=user)


@app.get("/users/ma")
def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=0, limit=100)
    return users


@app.get("/users/{uid}/errors", response_model=List[schemas.Error])
def read_errors(uid: int, db: Session = Depends(get_db)):
    errors = crud.get_user_errors(db, uid=uid)
    return errors


@app.get("/users/{user_phone}", response_model=schemas.User)
def read_user(user_phone: str, db: Session = Depends(get_db)):
    db_user = crud.get_user1(db, userphone=user_phone)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/{user_phone}/{password}")
def read_user(user_phone: str, password: str, db: Session = Depends(get_db)):
    db_user = crud.get_user2(db, userphone=user_phone, password=password)
    if db_user is None:
        return False
    else:
        return True


@app.get("/rank/")
def read_rank(db: Session = Depends(get_db)):
    rank = crud.get_users_rank(db)
    if rank is None:
        raise HTTPException(status_code=404, detail="ranker not found")
    return rank


@app.get("/users/{userid}/condition/day")
def get_user_day_condition(userid: int, db: Session = Depends(get_db)):
    condition = crud.get_user_medata(db, uid=userid)
    if condition is None:
        raise HTTPException(status_code=404, detail="condition not found")
    return condition


@app.get("/con/{userid}")
def get_user_con(userid: int, db: Session = Depends(get_db)):
    con = crud.get_medata(db, uid=userid)
    if con is None:
        raise HTTPException(status_code=404, detail="con not found")
    return con


#获取商品列表
@app.get("/goods")
def get_goods(db: Session = Depends(get_db)):
    goods = crud.get_goods(db)
    if goods is None:
        raise HTTPException(status_code=404, detail="goods not found")
    return goods


@app.post("/users/")
async def create_user(request: Request, user: schemas.UserCreate, db: Session = Depends(get_db)):
    data = await request.json()
    user.userphone = data['userphone']
    user.password = data['password']
    user.nickname = data['nickname']
    user.useraddress = data['useraddress']
    db_user = crud.create_user(db=db, user=user)
    return db_user


@app.post("/orders")
async def create_order(request: Request, order: schemas.OrderCreate, db: Session = Depends(get_db)):
    data = await request.json()
    order.otime = isoparse(data['otime'])
    order.ogoodsid = data['ogoodsid']
    order.ouserid = data['ouserid']
    order.ouserphone = data['ouserphone']
    order.oaddress = data['oaddress']
    db_order = crud.create_order(db=db, order=order)
    return db_order


@app.post("/users/{userid}/")
async def refresh_user(request: Request, userid: int, db: Session = Depends(get_db)):
    data = await request.json()
    usernickname = data['username']
    password = data['passworddata']
    useraddress = data['useraddress']
    user = db.query(models.Memory).filter(models.Memory.uid == userid).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.password = password
    user.nickname = usernickname
    user.useraddress = useraddress
    db.commit()
    db.refresh(user)
    return user


@app.post("/records")
async def create_record(request: Request, record: schemas.RecordCreate, db: Session = Depends(get_db)):
    data = await request.json()
    record.retime = isoparse(data['retime'])
    record.ruid = data['ruid']
    record.rwid = data['rwid']
    record.rwbid = data['rwbid']
    db_record = crud.create_record(db=db, record=record)
    return db_record


@app.post("/errors")
async def create_error(request: Request, error: schemas.ErrorCreate, db: Session = Depends(get_db)):
    data = await request.json()
    error.etime = isoparse(data['etime'])
    error.euid = data['euid']
    error.eword = data['eword']
    error.ebook = data['ebook']
    error.ecn = data['ecn']
    db_re = crud.get_word(db, eword=error.eword)
    if db_re is None:
        db_error = crud.create_error(db=db, error=error)
        return db_error
    else:
        return db_re


@app.post("/upload")
async def upload_file(file: UploadFile):
    sendmail()
    file_contents = await file.read()
    # 在这里，我们将文件内容保存到服务器的文件系统中
    # 首先，我们定义一个保存文件的目录
    upload_folder = "uploads"
    # 然后，我们创建这个目录（如果它不存在）
    os.makedirs(upload_folder, exist_ok=True)
    # 最后，我们将文件内容写入到这个目录中
    file_path = os.path.join(upload_folder, file.filename)
    with open(file_path, "wb") as f:
        f.write(file_contents)
    return {"filename": file.filename}


@app.get("/files/{userphone}")
async def download_file(userphone: str, db: Session = Depends(get_db)):
    # 在这里，我们定义了保存文件的目录
    upload_folder = "uploads"
    user = crud.get_user1(db, userphone=userphone)
    # 然后，我们构造文件的完整路径
    file_path = os.path.join(upload_folder, user.userimage)
    # 最后，我们使用 FileResponse 来返回文件
    return FileResponse(file_path)


@app.get("/files/books/{filename}")
async def dw_file(filename: str):
    upload_folder = "uploads"
    file_path = os.path.join(upload_folder, filename)
    return FileResponse(file_path)
@app.get("/files/goods/{gid}")
async def download_file(gid: int, db: Session = Depends(get_db)):
    # 在这里，我们定义了保存文件的目录
    upload_folder = "uploads"
    good = crud.get_good(db, gid=gid)
    # 然后，我们构造文件的完整路径
    file_path = os.path.join(upload_folder, good.gimg)
    # 最后，我们使用 FileResponse 来返回文件
    return FileResponse(file_path)


@app.get("/admin/{mphone}/{mpassword}")
def get_manager(mphone: str, mpassword: str, db: Session = Depends(get_db)):
    db_admin = crud.get_admin(db, mphone=mphone,mpassword=mpassword)
    if db_admin is None:
        return False
    else:
        return True

@app.get("/words/{uid}/{bid}",response_model=List[schemas.Word])
def get_words(uid: int, bid: str, db: Session = Depends(get_db)):
    words = crud.get_words(db, uid=uid, bid=bid, skip=0, limit=30)
    return words


@app.get("/orders/{userid}")
def get_user_orders(userid: int, db: Session = Depends(get_db)):
    orders = crud.get_orders(db, userid=userid)
    return orders


@app.get("/books/{userid}")
def get_user_books(userid: int, db: Session = Depends(get_db)):
    books = crud.get_books(db, userid=userid)
    return books


@app.get("/test/{userid}")
def get_user_test(userid: int, db: Session = Depends(get_db)):
    words = crud.get_test(db, uid=userid)
    return words