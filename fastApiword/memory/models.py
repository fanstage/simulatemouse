from sqlalchemy import Boolean, Column, ForeignKey, Integer, Float, String, DateTime,LargeBinary
from .database import Base
from sqlalchemy.orm import relationship


class Memory(Base):
    __tablename__ = 'personal_userinfo'
    uid = Column(Integer, primary_key=True, index=True)  # 设置主键和索引
    nickname = Column(String(25))
    password = Column(String(25))
    userphone = Column(String(11))
    useraddress = Column(String(100))
    integral = Column(Integer)
    userimage = Column(String(255))

    order = relationship("Orders", back_populates="user")


class Orders(Base):
    __tablename__ = 'order'
    oid = Column(Integer, primary_key=True, index=True)
    otime = Column(DateTime)
    ouserid = Column(Integer, ForeignKey("personal_userinfo.uid"))
    ogoodsid = Column(Integer)
    oaddress = Column(String(100))
    ouserphone = Column(String(11))

    user = relationship("Memory", back_populates="order")


class Good(Base):
    __tablename__ = 'goods'
    gid = Column(Integer, primary_key=True, index=True)
    gname = Column(String(25))
    gprice = Column(Integer)
    gimg = Column(String(255))


class Word(Base):
    __tablename__ = 'cet6_2'
    wordRank = Column(String(255), primary_key=True, index=True)
    headWord = Column(String(255))
    wordID = Column(String(255))
    sContent1 = Column(String(255))
    sCn1 = Column(String(255))
    sContent2 = Column(String(255))
    sCn2 = Column(String(255))
    usphone = Column(String(255))
    pos1 = Column(String(255))
    tran1 = Column(String(255))
    pos2 = Column(String(255))
    tran2 = Column(String(255))
    pos3 = Column(String(255))
    tran3 = Column(String(255))
    pos4 = Column(String(255))
    tran4 = Column(String(255))
    pos5 = Column(String(255))
    tran5 = Column(String(255))
    pContent1 = Column(String(255))
    pCn1 = Column(String(255))
    pContent2 = Column(String(255))
    pCn2 = Column(String(255))
    pContent3 = Column(String(255))
    pCn3 = Column(String(255))
    bookId = Column(String(255))


class Word2(Base):
    __tablename__ = 'kaoyan_2'
    wordRank = Column(String(255), primary_key=True, index=True)
    headWord = Column(String(255))
    wordID = Column(String(255))
    sContent1 = Column(String(255))
    sCn1 = Column(String(255))
    sContent2 = Column(String(255))
    sCn2 = Column(String(255))
    usphone = Column(String(255))
    pos1 = Column(String(255))
    tran1 = Column(String(255))
    pos2 = Column(String(255))
    tran2 = Column(String(255))
    pos3 = Column(String(255))
    tran3 = Column(String(255))
    pos4 = Column(String(255))
    tran4 = Column(String(255))
    pos5 = Column(String(255))
    tran5 = Column(String(255))
    pContent1 = Column(String(255))
    pCn1 = Column(String(255))
    pContent2 = Column(String(255))
    pCn2 = Column(String(255))
    pContent3 = Column(String(255))
    pCn3 = Column(String(255))
    bookId = Column(String(255))


class Book(Base):
    __tablename__ = 'books'
    bid = Column(Integer, primary_key=True,index=True)
    bname = Column(String(50))
    bamount = Column(Integer)
    bookimage = Column(String(255))


class Record(Base):
    __tablename__ = 'records'
    rid = Column(Integer, primary_key=True, index=True)
    rwid = Column(Integer)
    ruid = Column(Integer)
    rwbid = Column(String(25))
    state = Column(Integer)
    retime = Column(Integer)



class Manager(Base):
    __tablename__ = 'managers'
    mid = Column(Integer, primary_key=True, index=True)
    mphone = Column(String(11))
    mpassword = Column(String(25))


class Error(Base):
    __tablename__ = 'errors'
    eid = Column(Integer, primary_key=True, index=True)
    eword = Column(String(255))
    ebook = Column(String(255))
    ecn = Column(String(255))
    euid = Column(Integer)
    etime = Column(DateTime)



class Rank(Base):
    __tablename__ = 'rank'
    rankid = Column(Integer, primary_key=True, index=True)
    rank = Column(Integer)
    ranknickname = Column(String(25))
    erate = Column(Float)
    enumber = Column(Integer)
    esid = Column(Integer)

    def to_dict(self):
        return {
            'rankid': self.rankid,
            'esid': self.esid,
            'rank': self.rank,
            'ranknickname': self.ranknickname,
            'enumber': self.enumber,
            'erate': self.erate
        }
