import datetime
from typing import List, Union
from pydantic import BaseModel
from typing import Optional


class UserBase(BaseModel):
    userphone: str


class UserCreate(UserBase):
    nickname: str
    userphone: str
    password: str
    useraddress: str


class User(UserBase):
    uid: int
    nickname: str
    useraddress: str
    password: str
    integral: int
    userimage: str

    class Config:
        orm_mode = True


class ManagerBase(BaseModel):
    mphone: str


class ManagerCreate(ManagerBase):
    mpassword: str


class Manager(UserBase):
    mid: int
    mphone: str
    mpassword: str

    class Config:
        orm_mode = True


class ErrorBase(BaseModel):
    euid: int


class ErrorCreate(ErrorBase):
    eword: str
    ebook: str
    ecn: str
    euid: int
    etime: datetime.datetime


class Error(ErrorBase):
    eword: str
    ecn: str

    class Config:
        orm_mode = True


class RankBase(BaseModel):
    ranknickname: str


class RankCreate(RankBase):
    rank: int


class Rank(RankBase):
    rank: int
    ranknickname: str
    enumber: int
    erate: float

    class Config:
        orm_mode = True


class OrderBase(BaseModel):
    otime: datetime.datetime


class OrderCreate(OrderBase):
    otime: datetime.datetime
    ogoodsid: int
    ouserid: int
    oaddress: str
    ouserphone: str


class Order(OrderBase):
    oid: int
    otime: datetime.datetime
    ogoodsid: int
    ouserid: int
    oaddress: str
    ouserphone: str

    class Config:
        orm_mode = True


class WordBase(BaseModel):
    headWord: int


class Word(WordBase):
    wordRank: int
    headWord: Optional[str]
    wordID: Optional[str]
    usphone: Optional[str]
    pos1: Optional[str]
    pos2: Optional[str]
    pos3: Optional[str]
    tran1: Optional[str]
    tran2: Optional[str]
    tran3: Optional[str]
    pContent1: Optional[str]
    pContent2: Optional[str]
    pCn1: Optional[str]
    pCn2: Optional[str]
    sContent1: Optional[str]
    sContent2: Optional[str]
    sCn1: Optional[str]
    sCn2: Optional[str]
    bookId: Optional[str]

    class Config:
        orm_mode = True


class RecordBase(BaseModel):
    ruid: int


class RecordCreate(RecordBase):
    ruid: int
    rwid: int
    rwbid: str
    retime: datetime.datetime

