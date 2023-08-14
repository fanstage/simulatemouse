from sqlalchemy.orm import Session
from sqlalchemy import exists
from datetime import datetime
from datetime import timedelta
from . import schemas, models
import random

today = datetime.now().date()
# 定义一个tomorrow变量，表示明天
tomorrow = today + timedelta(days=1)
week_start = today - timedelta(days=today.weekday())


def get_user_medata(db: Session, uid: int):
    #  统计当天记忆的单词数量
    dmenumber = db.query(models.Record).filter((models.Record.ruid == uid) & (models.Record.retime >= today) & (models.Record.retime <= tomorrow)).count()
    wmenumber = db.query(models.Record).filter((models.Record.ruid == uid) & (models.Record.retime >= week_start) & (models.Record.retime <= tomorrow)).count()
    dernumber = db.query(models.Error).filter((models.Error.euid == uid) & (models.Error.etime >= today) & (models.Error.etime <= tomorrow)).count()
    wernumber = db.query(models.Error).filter((models.Error.euid == uid) & (models.Error.etime >= week_start) & (models.Error.etime <= tomorrow)).count()
    drightnum = 30-dernumber
    wrighnum = 30 * today.weekday() - wernumber
    dnonum = 30-dmenumber
    wnonum = 30 * today.weekday() - wmenumber
    return [drightnum, dernumber, dnonum, wrighnum, wernumber, wnonum]


def get_user1(db: Session, userphone: str):
    return db.query(models.Memory).filter(models.Memory.userphone == userphone).first()


def get_user2(db: Session, userphone: str, password: str):
    return db.query(models.Memory).filter((models.Memory.userphone == userphone) & (models.Memory.password == password)).first()


def get_user_by_userphone(db: Session, userphone: str):
    return db.query(models.Memory).filter(models.Memory.userphone == userphone).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Memory).offset(skip).limit(limit).all()


def get_user_nickname(db: Session, userphone: str):
    return db.query(models.Memory).with_entities(models.Memory.nickname).filter(models.Memory.userphone == userphone).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.Memory(nickname=user.nickname, userphone=user.userphone, password=user.password, useraddress=user.useraddress, integral=0)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Orders(otime=order.otime, ogoodsid=order.ogoodsid, ouserid=order.ouserid, oaddress=order.oaddress, ouserphone=order.ouserphone)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order


def create_record(db: Session, record: schemas.RecordCreate):
    db_record = models.Record(ruid=record.ruid, rwid=record.rwid, rwbid=record.rwbid, retime=record.retime, state=0)
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record


def get_goods(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Good).offset(skip).limit(limit).all()


def get_good(db: Session, gid: int):
    return db.query(models.Good).filter(models.Good.gid == gid).first()


# 获得管理员的信息
def get_admin(db: Session, mphone: str, mpassword: str):
    return db.query(models.Manager).filter((models.Manager.mphone == mphone) & (models.Manager.mpassword == mpassword)).first()


def get_users_rank(db: Session):
    ranks_dict = [rank.to_dict() for rank in (db.query(models.Rank).all())]
    sorted_ranks = sorted(ranks_dict, key=lambda x: x['enumber'])
    return ranks_dict


def get_user_errors(db: Session, uid: int):
    return db.query(models.Error).filter(models.Error.euid == uid).all()


def get_words(db: Session, uid: int, bid: str, skip: int = 0, limit: int = 30):
    if(bid =='CET6_2'):
        return db.query(models.Word).filter(
            ~exists().where((models.Record.rwid == models.Word.wordRank) & (models.Record.ruid == uid))).offset(
            skip).limit(limit).all()
    else:
        return db.query(models.Word2).filter(
            (models.Word2.wordRank == bid) & (~exists().where((models.Record.rwid == models.Word.wordRank) & (models.Record.ruid == uid)))).offset(
            skip).limit(limit).all()


def get_word(db: Session, eword: str):
    return db.query(models.Error).filter(models.Error.eword == eword).first()


def create_error(db: Session, error: schemas.ErrorCreate):
    db_error = models.Error(eword=error.eword, ebook=error.ebook, ecn=error.ecn, euid=error.euid, etime=error.etime)
    db.add(db_error)
    db.commit()
    db.refresh(db_error)
    return db_error


def get_medata(db: Session, uid: int):
    #  统计当天记忆的单词数量
    dmenumber = db.query(models.Record).filter((models.Record.ruid == uid) & (models.Record.retime >= today) & (models.Record.retime <= tomorrow)).count()
    # 统计所有记忆的单词数量
    anumber = db.query(models.Record).filter((models.Record.rwbid == 'cet6_2')).count()
    drate = int((dmenumber / 30) * 100)
    arate = int((anumber / 2079) * 100)
    return [drate, arate]


def get_test(db: Session, uid: int):
    # 从记录表中读取本周该用户所有背过的单词
    results = db.query(models.Record).filter(models.Record.ruid == uid).all()
    # 从获取到的记录中随机抽取36个单词
    rrs = random.sample(results, 36)
    words = []
    for result in rrs:
        wid = result.rwid
        word = db.query(models.Word).filter(models.Word.wordRank == wid).first()
        words.append(word)
    random.shuffle(words)
    return words


def get_test(db: Session, uid: int):
    # 从记录表中读取本周该用户所有背过的单词
    results = db.query(models.Record).filter(models.Record.ruid == uid).all()
    words = []
    for result in results:
        wid = result.rwid
        word = db.query(models.Word).filter(models.Word.wordRank == wid).first()
        words.append(word)
    random.shuffle(words)
    return words


def get_orders(db: Session, userid: int):
    return db.query(models.Orders).filter(models.Orders.ouserid == userid).all()


def get_books(db: Session, userid: int):
    books = db.query(models.Book).all()
    for book in books:
        count = db.query(models.Record).filter((models.Record.ruid == userid) & (models.Record.rwbid == book.bid)).count()
        book.progress = int((count / book.bamount) * 100)
    return books